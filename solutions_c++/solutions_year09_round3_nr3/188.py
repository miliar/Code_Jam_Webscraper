
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
int memo[10001][10001];
vector<int>arr;
int func(int start, int end)
{
  if(start >= end)
    return 0;
  if(memo[start][end] != -1)
    return memo[start][end];
  int ret = INT_MAX / 2;
  FOREACH(it, arr)
  {
    if(*it >= start && *it < end)
    {
      int val = func(start, *it) + func(*it + 1, end) + end - start - 1;
      ret = min(ret, val);
    }
  }
  if(ret == INT_MAX/2)
    return memo[start][end] = 0;
  else return memo[start][end] = ret;
}
int main()
{
  int T = GI;
  FORZ(testcase, T)
  {
    CLR(memo, -1);
    dbg(testcase);
    printf("Case #%d: ", testcase  +1);
    int P = GI, Q = GI;
    arr.clear();
    FORZ(i, Q)
    {
      int tmp = GI;
      arr.push_back(tmp-1);
    }
    cout << func(0, P) << endl;
  }
	return 0;
}
//Powered by Siddharth
