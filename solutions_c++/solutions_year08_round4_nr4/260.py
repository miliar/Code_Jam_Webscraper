#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <vector>
#include <algorithm>

using namespace std;

#define PI 3.1415926535897932384626433832795
#define INF (int)1e9
#define EPS 1e-9

#define SQR(a) ((a)*(a))

#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define SORT(a) sort(a.begin(), a.end())
#define CLEAR(a) a.clear()
#define FILL(a) memset(a, 0, sizeof(a))
#define SIZE(a) (int)a.size()
#define LEN(a) (int)a.length()
#define SUBSTR(i,j) substr(i,j-i+1)
#define PB push_back
#define MP make_pair
#define VI vector<int>
#define VS vector<string>

stringstream foo("");
string buf;

#define READ getline(cin, buf), foo.clear(), foo.str(buf)

int tests;

#define K 6

int k;
string str;
int len;
bool mark[K];
int p[K];
int ans;

void check()
{
  string pstr = "";
  for (int i = 0; i < len; i += k)
  {
    string cur = str.substr(i,k);
//    cout << "shuffle " << cur << endl;
    FOR(j,0,k-1)
      pstr += cur[p[j]];
  }
//  cout << pstr << endl;
  int s = 1;
  FOR(i,1,len-1)
    if (pstr[i] != pstr[i - 1])
      s++;
  ans = min(ans, s);
}
void perm( int pos )
{
  if (pos == k)
  {
    check();
    return;
  }
  FOR(i,0,k-1)
    if (!mark[i])
    {
      p[pos] = i;
      mark[i] = true;
      perm(pos + 1);
      mark[i] = false;
    }
}

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  READ;
  foo >> tests;
  FOR(test,1,tests)
  {
    scanf("%i\n", &k);
    getline(cin, str);
    len = LEN(str);
    FILL(mark);
    ans = INF;
    perm(0);
    cout << "Case #" << test << ": " << ans << endl;
  }

  return 0;
}
