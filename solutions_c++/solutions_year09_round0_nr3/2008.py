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
#define MOD 10000
string PAT = "welcome to code jam";
int main()
{
  int N = GI;
  FORZ(testcase, N)
  {
    printf("Case #%d: ", testcase + 1);
    getchar();
    char line[1000];
    int dp[1000][1000] = {0};
    scanf("%[^\n]", line);
    for(int i=0;line[i];i++)
      if(line[i] == PAT[PAT.size() - 1])
        dp[i][1] = 1;
    int sum = 0;
    for(int suffix = 2; suffix <= PAT.size(); suffix++)
    {
      char startChar = PAT[PAT.size() - suffix];
      for(int i=0; line[i]; i++)
      {
        sum = 0;
        if(startChar == line[i])
        {
          for(int j = i+1; line[j]; j++)
          {
            sum = ((sum%MOD) + (dp[j][suffix - 1])%MOD)%MOD;
          }
        }
        dp[i][suffix] = sum;
      }
    }
    int ans = 0;
    for(int i=0;line[i];i++)
      ans = (ans%MOD + dp[i][PAT.size()]%MOD)%MOD;
    printf("%04d\n", ans);
  }
	return 0;
}
//Powered by Siddharth
