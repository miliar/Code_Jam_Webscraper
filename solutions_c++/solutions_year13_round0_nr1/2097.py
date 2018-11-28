#include<iostream>
#include<algorithm>
#include<iomanip>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<deque>
#include<cctype>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<stack>
#include<sstream>
using namespace std;
#define FOR(i, a, b) for(int i=a; i<b; ++i)
#define FORC(i, a, b) for(int i=a; i<=b; ++i)
#define FORD(i, a, b) for(int i=a-1; i>=b; --i)
#define FORDC(i, a, b) for(int i=a; i>=b; --i)
#define endl '\n'
#define pb push_back
#define size(v) (int)((v).size())
#define all(v) (v).begin(), (v).end()
#define DREP(v) sort(all(v)); v.erase(unique(all(v)), (v).end())
#define F first
#define S second
#define mp make_pair
#define VI vector<int>
#define index(arr, val) lower_bound(all(a), val)-(a).begin()
#define iter(i, c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define PII pair<int, int>
#define ll long long
#define ini(arr, val) memset(arr, val, sizeof(arr))
#define debug(a) cerr<<"DEBUG: "<<#a<<" = "<<a<<endl
#define deb debug("gauss")
int t, tx, ty; string a[4];
bool fin, xwin, owin, check;
int main()
{
   int t; cin>>t;
   FORC(u, 1, t)
   {
      FOR(i, 0, 4) cin>>a[i];
      tx = ty = -1; fin = xwin = owin = false;
      FOR(i, 0, 4) FOR(j, 0, 4)
      {
	 if(a[i][j] == 'T') tx = i, ty = j;
	 if(a[i][j] == '.') fin = true;
      }
      
      if(tx != -1) a[tx][ty] = 'X';
      FOR(i, 0, 4) if(a[i] == "XXXX") xwin |= true;
      FOR(j, 0, 4)
      {
	 check = true;
	 FOR(i, 0, 4) if(a[i][j] != 'X') check = false;
	 xwin |= check;
      }
      check = true;
      FOR(i, 0, 4) if(a[i][i] != 'X') check = false;
      xwin |= check;
      check = true;
      FOR(i, 0, 4) if(a[i][3-i] != 'X') check = false;
      xwin |= check;

      if(tx != -1) a[tx][ty] = 'O';
      FOR(i, 0, 4) if(a[i] == "OOOO") owin |= true;
      FOR(j, 0, 4)
      {
	 check = true;
	 FOR(i, 0, 4) if(a[i][j] != 'O') check = false;
	 owin |= check;
      }
      check = true;
      FOR(i, 0, 4) if(a[i][i] != 'O') check = false;
      owin |= check;
      check = true;
      FOR(i, 0, 4) if(a[i][3-i] != 'O') check = false;
      owin |= check;

      if(xwin and !owin)
	 printf("Case #%d: X won\n", u);
      else if(owin and !xwin)
	 printf("Case #%d: O won\n", u);
      else if((xwin and owin) or !fin)
	 printf("Case #%d: Draw\n", u);
      else
	 printf("Case #%d: Game has not completed\n", u);
   }
}