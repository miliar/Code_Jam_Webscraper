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
#define INF 100000000000000001LL
#define EPS 1e-4

#define SQR(a) ((a)*(a))

#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define SORT(a) sort(a.begin(), a.end())
#define CLEAR(a) a.clear()
#define FILL(a) memset(a, 0, sizeof(a))
#define SIZE(a) (int)a.size()
#define LEN(a) (int)a.length()
#define SUBSTR(i,j) substr((i),(j)-(i)+1)
#define PB push_back


stringstream foo("");
string buf;

#define READ getline(cin, buf), foo.clear(), foo.str(buf)

int tests;

#define N 400
#define L 10000


int n;
int clr_n;
string clr[N];
int a[N], b[N], c[N];
int longest[N][L];
int ans;
int start[L];

int get_index( string str )
{
  FOR(i, 0, clr_n - 1)
    if (clr[i] == str)
      return i;
  clr[clr_n++] = str;
  return clr_n - 1;
}

void process3( int i, int j, int k )
{
  int pref = -1;
  int cnt = 0;
  while (pref != L - 1)
  {
    if (cnt > ans)
      return;
    int next_pref = max(longest[i][pref + 1], max(longest[j][pref + 1], longest[k][pref + 1]));
    if (next_pref <= pref)
      return;
    pref = next_pref;
    cnt++;
  }
  ans = min(ans, cnt);
}
void process2( int i, int j )
{
  int pref = -1;
  int cnt = 0;
  while (pref != L - 1)
  {
    if (cnt > ans)
      return;
    int next_pref = max(longest[i][pref + 1], longest[j][pref + 1]);
    if (next_pref <= pref)
      return;
    pref = next_pref;
    cnt++;
  }
  ans = min(ans, cnt);
}
void process1( int i )
{
  int pref = -1;
  int cnt = 0;
  while (pref != L - 1)
  {
    if (cnt > ans)
      return;
    int next_pref = longest[i][pref + 1];
    if (next_pref <= pref)
      return;
    pref = next_pref;
    cnt++;
  }
  ans = min(ans, cnt);
}
bool check_impossible()
{
  int pref = -1;
  while (pref != L - 1)
  {
    int next_pref = start[pref + 1];
    if (next_pref <= pref)
      return false;
    pref = next_pref;
  }
  return true;
}

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  READ;
  foo >> tests;
  FOR(test,1,tests)
  {
    scanf("%i\n", &n);
    clr_n = 0;
    FOR(i,0,n-1)
    {
      string str;
      READ;
      foo >> str >> a[i] >> b[i];
      a[i]--, b[i]--;
      c[i] = get_index(str);
    }

    FOR(i, 0, L - 1)
      start[i] = -1;
    FOR(i, 0, n - 1)
      start[a[i]] = max(start[a[i]], b[i]);
    FOR(i, 1, L - 1)
      start[i] = max(start[i], start[i - 1]);
    if (!check_impossible())
    {
       cout << "Case #" << test << ": IMPOSSIBLE\n";
       fprintf(stderr, "test %i (%i) complited!\n", test, n);
       continue;
    }
    ans = n + 1;
    FILL(longest);
    FOR(i, 0, clr_n - 1)
    {
      FOR(j, 0, L - 1)
        longest[i][j] = -1;
      FOR(j, 0, n - 1)
        if (c[j] == i)
          longest[i][a[j]] = max(longest[i][a[j]], b[j]);
      FOR(j, 1, L - 1)
        longest[i][j] = max(longest[i][j], longest[i][j - 1]);
    }
    if (clr_n >= 3)
    {
      FOR(i, 0, clr_n - 1)
        FOR(j, i + 1, clr_n - 1)
          FOR(k, j + 1, clr_n - 1)
            process3(i, j, k);    
    }
    else
    if (clr_n == 2)
    {
      FOR(i, 0, clr_n - 1)
        FOR(j, i + 1, clr_n - 1)
            process2(i, j);    
    }
    else
    {
      process1(0);
    }

    cout << "Case #" << test << ":";
    if (ans == n + 1)
      printf(" IMPOSSIBLE\n");
    else 
      printf(" %i\n", ans);
    fprintf(stderr, "test %i (%i) complited!\n", test, n);
  }

  return 0;
}
