

//Murugan Thunai !
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>  
using namespace std;

#define pb push_back
#define mp make_pair
#define v(x) vector< x >
#define sz size()
#define FOR(i, first, last) for (int i = (first); i != (last); ++i)
#define FORZ(i,n) FOR(i,0,n)
#define FORO(i,o) FORZ(i,((o).sz))
#define FOREACH(itr, x) for(__typeof(x.begin()) itr = x.begin(); itr != x.end(); itr++)
#define ALL(a) (a).begin(),(a).end()
#define SORT(a) sort(ALL(a))
#define ss stringstream
#define dbg(x) (cerr << #x << ": " << x<<'\n')
#define GI ({int t ; scanf("%d",&t);t;})
#define CLR(x, v) memset(x, v, sizeof(x));
typedef long long ll;
typedef unsigned long long ull;
typedef v(int) vi;
typedef v(vi) vvi;
typedef v(string) vs;
typedef v(vs) vvs;
typedef pair<int,int> ii;
typedef v(ii) vii;
vs arr;
map<vs, int> dic;
set<vs> vis;
int check(vs& a)
{
  for(int i=0;i<a.size();i++)
  {
    for(int j=i+1;j<a[i].size();j++)
    {
      if(a[i][j] == '1')
        return 0;
    }
  }
  return 1;
}
int findLastOne(string & str)
{
  for(int i = str.size() - 1; i>= 0 ;i--)
    if(str[i] == '1')
      return i;
  return 0;
}
int main()
{
  int T = GI;
  for(int testcase = 1; testcase <= T; testcase++)
  {
    dbg(testcase);
    printf("Case #%d: ", testcase);
    int N = GI;
    arr = vs(N);
    FORO(i, arr)
      cin >> arr[i];
    int ans = 0;
    vector<pair<string, ii> > s;
    for(int i=0;i<arr.size();i++)
    {
      cerr << arr[i] << " : " << findLastOne(arr[i]) << endl;
      s.push_back(mp(arr[i], ii(findLastOne(arr[i]), i)));
    }
    for(int i=0;i<arr.size();i++)
    {
      FORO(j, s)
      {
        if(s[j].second.first <= i)
        {
          s[j].second.first = INT_MAX/2;
          ans += s[j].second.second;
          FOR(k, j+1, s.size())
          {
            s[k].second.second --;
          }
          break;
        }
      }
    }
    cout << ans << endl;
  }
	return 0;
}
//Powered by Siddharth
