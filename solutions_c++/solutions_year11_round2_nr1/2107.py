#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

class team_stat
{
  public:
    int w, l, g;
    double wp, owp;
    vector<int> wins, losses;

    team_stat(string s);
    team_stat& operator=(team_stat &other);
};

team_stat::team_stat(string s)
{
  int len = (int)s.length();
  w = l = 0;
  for (int i = 0; i < len; i++)
    if (s[i] == '1')
    {
      w++;
      wins.push_back(i);
    }
    else if (s[i] == '0')
    {
      l++;
      losses.push_back(i);
    }
  g = w + l;
  wp = (double)w / (double)g;
//  cout << s << ":" << w << ":" << g << ":" << wp << endl;
  owp = 0;
}

team_stat& team_stat::operator=(team_stat &other)
{
  l = other.l;
  w = other.w;
  g = other.g;
  wp = other.wp;
  owp = other.owp;
  wins = other.wins;
  losses = other.losses;
//  cout << ":" << w << ":" << g << ":" << wp << endl;
  return *this;
}

int main(int argc, char *argv[])
{
  int T, N;
  string s;
  vector<team_stat> ts;
  vector<int>::iterator it;
  double x;

  ifstream in;
  ofstream out;

  if (argc == 3)
  {
    in.open(argv[1]);
    if (!in.is_open())
    {
      cerr << "Error opening " << argv[1] << endl;
      return 0;
    }
    out.open(argv[2]);
    if (!out.is_open())
    {
      in.close();
      cerr << "Error opening " << argv[2] << endl;
      return 0;
    }
  }
  else
  {
    in.open("in.txt");
    if (!in.is_open())
    {
      cerr << "Error opening in.txt" << endl;
      return 0;
    }
    out.open("out.txt");
    if (!out.is_open())
    {
      in.close();
      cerr << "Error opening out.txt" << endl;
      return 0;
    }
  }

  out.precision(12);
  in >> T;
  for (int i = 0; i < T; i++)
  {
    out << "Case #" << i + 1 << ":" << endl;
//    cout << "Case #" << i + 1 << ":" << endl;
    in >> N;
    ts.clear();
    for (int j = 0; j < N; j++)
    {
      in >> s;
      ts.push_back(team_stat(s));
    }

    for (int j = 0; j < N; j++)
    {
      x = 0;
      for (it = ts[j].wins.begin(); it != ts[j].wins.end(); it++)
        x += (double)ts[*it].w / (double)(ts[*it].g - 1);
      for (it = ts[j].losses.begin(); it != ts[j].losses.end(); it++)
        x += (double)(ts[*it].w - 1) / (double)(ts[*it].g - 1);
      x /= ts[j].wins.size() + ts[j].losses.size();
      ts[j].owp = x;
    }

    for (int j = 0; j < N; j++)
    {
      x = 0;
      for (it = ts[j].wins.begin(); it != ts[j].wins.end(); it++)
        x += ts[*it].owp;
      for (it = ts[j].losses.begin(); it != ts[j].losses.end(); it++)
        x += ts[*it].owp;
      x /= ts[j].wins.size() + ts[j].losses.size();

//      cout << "Team #" << j + 1 << ": WP=" << ts[j].wp << " OWP=" << ts[j].owp << " OOWP=" << x;

      x = 0.25 * ts[j].wp + 0.50 * ts[j].owp + 0.25 * x;

//      cout << " RPI=" << x << endl;
      out << x << endl;
    }
  }

  return 0;
}

