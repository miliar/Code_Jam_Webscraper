#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

using namespace std;

int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

vector <string> split(const string _s, const string del);
int toInt(string s) {int r = 0; istringstream ss(s); ss >> r; return r;}
string toStr(int n) {ostringstream ss; ss << n; return ss.str();}

int n, m;

int main(int argc, char ** argv)
{
  if (argc != 2)
  {
    cout << "Usage " << argv[0] << " <input file name>\n";
    return 0;
  }

  int i, j, k, t, tt;

  freopen(argv[1], "r", stdin);
  // freopen("output.txt", "w", stdout);

  scanf("%d\n", &tt);
  for (t = 1; t <= tt; ++t) {
      printf("Case #%d:\n", t);
      // write code here
      int nteam = ni();
      vector<string> gres;
      vector<double> wp;
      vector<double> owp;
      vector<double> oowp;

      fi(nteam) {
          gres.pb(ns());
      }
      
      // WP
      fi(nteam) {
          int ngame = 0;
          int nwin = 0;
          fj(gres[i].length()) {
              if (gres[i][j] != '.')
                  ngame++;
              if (gres[i][j] == '1')
                  nwin++;
          }
          wp.pb((double)nwin / ngame);
      }
      // fi(wp.size())
      //     cout << wp[i] << endl;
      // OWP
      fi(nteam) {
          int ngame = 0;
          double nwin = 0.0;
          fj(gres[i].length()) {
              if (gres[i][j] != '.') {
                  ngame++;
                  int ogame = 0;
                  int owin = 0;
                  fk(gres[j].length()) {
                      if (k == i)
                          continue;
                      if (gres[j][k] != '.')
                          ogame++;
                      if (gres[j][k] == '1')
                          owin++;
                  }
                  nwin += (double)owin / ogame;
              }
          }
          owp.pb(nwin / ngame);
      }
      // fi(owp.size())
      //     cout << owp[i] << endl;
      // OOWP
      fi(nteam) {
          int ngame = 0;
          double nwin = 0.0;
          fj(gres[i].length()) {
              if(gres[i][j] != '.') {
                  ngame++;
                  nwin += owp[j];
              }
          }
          oowp.pb(nwin / ngame);
      }
      // fi(oowp.size())
      //     cout << oowp[i] << endl;
      fi(nteam) {
          double rip = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
          printf("%.12g\n", rip);
      }
  }

  return 0;
}

vector <string> split(const string _s, const string del)
{
  vector <string> ret;
  string s = _s;

  while (!s.empty())
    {
      size_t pos = s.find(del);
      string sub = "";
      sub = s.substr(0, pos);
      ret.push_back(sub);
      if (pos != string::npos)
        pos += del.size();
      s.erase(0, pos);
    }

  return ret;
}
