#include <iostream>
#include <vector>
#include <string>

using namespace std;


double calc_wp(vector<string> const &s, unsigned team, unsigned reject)
{
  unsigned wins = 0, games = 0;
  for ( unsigned j = 0; j < s[team].length(); ++j )
    if ( j != reject )
    {
      if ( s[team][j] == '1' )
        ++wins;
      if ( s[team][j] != '.' )
        ++games;
    }
  return games > 0 ? double(wins)/games : 0;
}


vector<double> calc_rpi(vector<string> const &s)
{
  vector<double> owps(s.size());
  vector<double> wps(s.size());
  for ( unsigned i = 0; i < s.size(); ++i )
  {
    wps[i] = calc_wp(s, i, unsigned(-1));
    double owp = 0;
    unsigned nop = 0;
    for ( unsigned j = 0; j < s[i].length(); ++j )
    {
      if ( s[i][j] != '.' )
      {
        owp += calc_wp(s, j, i);
        ++nop;
      }
    }
    owps[i] = nop > 0 ? owp/nop : 0;
  }
  vector<double> res(s.size());
  for ( unsigned i = 0; i < s.size(); ++i )
  {
    double oowp = 0;
    unsigned nop = 0;
    for ( unsigned j = 0; j < s[i].length(); ++j )
    {
      if ( s[i][j] != '.' )
      {
        ++nop;
        oowp += owps[j];
      }
    }
    double rpi = 0.25*wps[i] + 0.50*owps[i] + 0.25*(nop > 0 ? oowp/nop : 0.0);
    res[i] = rpi;
  }
  return res;
}


vector<string> load_data()
{
  unsigned N;
  cin >> N;
  vector<string> res;
  for ( unsigned i = 0; i < N; ++i )
  {
    string line;
    cin >> line;
    res.push_back(line);
  }
  return res;
}


int main()
{
  cout.precision(15);
  int T;
  cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    vector<string> s = load_data();
    vector<double> r = calc_rpi(s);
    cout << "Case #" << t << ":\n";
    for ( unsigned i = 0; i < r.size(); ++i )
      cout << r[i] << '\n';
  }
  return 0;
}
