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
  for (t = 1; t <= tt; t++) {
      printf("Case #%d: ", t);
      // write code here
      ll N = nll();
      int PD = ni();
      int PG = ni();

      if (PG == 100 && PD < PG)
          printf("Broken\n");
      else if (PG == 0 && PD > PG)
          printf("Broken\n");
      else if (PD == 0 && PG == 0)
          printf("Possible\n");
      else {
          m = 100;
          for (n = 2; n <= PD;) {
              if (m % n == 0 && PD % n == 0) {
                  m /= n;
                  PD /= n;
              }
              else {
                  n++;
              }
              // cout << n << " " << m << " " << PD << endl;
          }
          if (m <= N)
              printf("Possible\n");
          else
              printf("Broken\n");
          
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
