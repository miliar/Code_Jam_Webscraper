
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
#define MAX 1005
int main()
{
  int arr[MAX];
  int T=GI;
  int testcase = 0;
  while(T--)
  {
    testcase ++;
    int N = GI;
    int sum = 0;
    FORZ(i, N)
    {
      arr[i] = GI;
      sum ^= arr[i];
    }
    if(sum)
    {
      printf("Case #%d: NO\n", testcase);
      continue;
    }
    int ans = -1;
    FORZ(i, (1<<N))
    {
      int cnt = 0;
      int mask = i;
      int sum1 = 0, sum2 = 0;
      int actualSum1 = 0, actualSum2 = 0;
      while(mask)
      {
        int d = mask & 1;
        if(d)
          sum1 ^= arr[cnt], actualSum1 += arr[cnt];
        else
          sum2 ^= arr[cnt], actualSum2 += arr[cnt];
        mask >>= 1;
        cnt++;
      }
      if(actualSum1 != 0 && actualSum2 != 0 && !(sum1 ^ sum2))
        ans = max(ans, max(actualSum1, actualSum2));
    }
    printf("Case #%d: %d\n", testcase, ans);
  }
	return 0;
}
//Powered by Siddharth
