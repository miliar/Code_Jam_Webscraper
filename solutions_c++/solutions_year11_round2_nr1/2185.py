#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>

using namespace std;

string makeOutName(string inName)
{
  auto outName = inName;
  auto length = inName.size();
  outName[length - 2] = 'o';
  outName[length - 1] = 'u';
  outName += 't';
  return outName;
}

//#define SMALL
#ifdef SMALL
  static const uint32_t MAX_TEAMS(10);
#else
  static const uint32_t MAX_TEAMS(100);
#endif

uint32_t n;
int8_t stats[MAX_TEAMS][MAX_TEAMS];
double games[MAX_TEAMS];
double wins[MAX_TEAMS];
double wp[MAX_TEAMS];
double owp[MAX_TEAMS];
double oowp[MAX_TEAMS];
double rpi[MAX_TEAMS];

double fillWP()
{
  for (uint8_t r=0; r<n; ++r)
  {
    games[r] = 0.0F;
    wins[r] = 0.0F;
    for (uint8_t c=0; c<n; ++c)
    {
      if (stats[r][c] != 0) { games[r] += 1.0; }
      if (stats[r][c] == 1) { wins[r] += 1.0; }
    }
    assert( games[r] >= wins[r] );
    wp[r] = wins[r] / games[r];
  }
}

double fillOWP()
{
  for (uint32_t team=0; team<n; ++team)
  {
    double total_wp = 0.0F;
    for (uint32_t opp=0; opp<n; ++opp)
    {
      if (opp == team) { continue; }
      if (stats[opp][team] == 0) { continue; }
      double adj_wins = (stats[opp][team] == -1) ? wins[opp] : wins[opp] - 1.0F;
      double adj_games = games[opp] - 1.0F;
      if (adj_games != 0)
      {
        double adj_wp = (adj_wins / adj_games);
        total_wp += adj_wp;
      }
    }
    owp[team] = total_wp / games[team];
    assert (owp[team] <= 1.0F);
  }
}

double fillOOWP()
{
  for (uint8_t r=0; r<n; ++r)
  {
    oowp[r] = 0.0F;
    for (uint8_t c=0; c<n; ++c)
    {
      if (stats[r][c] != 0) { oowp[r] += owp[c]; }
    }
    oowp[r] /= games[r];
    assert( 1.0F >= oowp[r] );
  }
}

// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
double fillRPI()
{
  for (uint8_t r=0; r<n; ++r)
  {
    rpi[r] = (0.25F * wp[r]) + (0.5F * owp[r]) + (0.25F * oowp[r]);
  }
}

int main(int argc, char* argv[])
{
  // Open input file
  fstream inFile(argv[1], fstream::in);
  if (!inFile.is_open())
  {
    cout << "Failed to open " << argv[1] << endl;
    return -1;
  }

  // Open output file
  auto outName = makeOutName(argv[1]);
  fstream outFile(outName, fstream::out);
  if (!outFile.is_open())
  {
    cout << "Failed to open " << outName << endl;
    return -1;
  }

  uint32_t numCases(0);
  inFile >> numCases;

  for (auto i = 0; i < numCases; ++i)
  {
//    cout << "Case #" << i+1 << endl;
    outFile << "Case #" << i+1 << ":" << endl;

    inFile >> n;

    // Read in data
    for (auto row = 0; row < n; ++row)
    {
      string rowString;
      inFile >> rowString;
      for (auto col = 0; col < n; ++col)
      {
        switch (rowString[col])
        {
          case '1' : { stats[row][col] = 1;  break; }
          case '0' : { stats[row][col] = -1; break; }
          case '.' : { stats[row][col] = 0;  break; }
          default:
          {
            cout << "Malformed input" << endl;
            return -1;
          }
        }
      }
    }

    fillWP();
    fillOWP();
    fillOOWP();
    fillRPI();

    for (auto ii = 0; ii < n; ++ii)
    {
//      cout.precision(10);
//      cout << rpi[ii] << endl;
      outFile.precision(10);
      outFile << rpi[ii] << endl;
    }
  }

  inFile.close();
  outFile.close();
  return 0;
}
