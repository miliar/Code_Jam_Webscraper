#pragma warning(disable: 4996)
#pragma warning(disable: 4010)
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <cmath>
#include <list>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <complex>
#include <climits>
using namespace std;

#define baby_jean std::cout<<"jean"[1]<<std::endl
#define gcj_out(idx)  printf("Case #%d: ", idx)
#define memcls(ary, val) memset(ary, val, sizeof ary)
const double PI = 2 * acos(0.0);
const double eps = 1e-9;
void debug(...)
{
}
char gcj[] = "welcome to code jam";
const int INF = 505;
/*
dp[i][j]表示前i个字母0--j[welcome to code jam]出现多少次//wwweellccoommee
if(gcj[j] == str[i + 1]) 
dp[i + 1][j] = dp[i][j - 1] + dp[i][j]
else
dp[i + 1][j] = dp[i][j]
边界：dp[0-->n][0]
*/
int main(void)
{
	#define LARGE
	
	//#define SMALL
#ifdef LARGE
	freopen("C:\\Users\\Pzjay\\Downloads\\C-large.in", "rt", stdin);
	freopen("C:\\Users\\Pzjay\\Downloads\\C-large-practice.out", "wt", stdout);
#endif
#ifdef SMALL
	freopen("C:\\Users\\Pzjay\\Downloads\\C-small-attempt0.in", "rt", stdin);
	freopen("C:\\Users\\Pzjay\\Downloads\\C-small-practice.out", "wt", stdout);
#endif
	int T, n;
	/*
	两堆数做抑或，值相等，但一个最大，一个最小
	*/
	scanf("%d", &T);
	int test;
	
	for(int pz = 1; pz <= T; ++ pz)
	{
		int ans = 1e7;
		//cout<<ans<<endl;
		scanf("%d", &n);
		scanf("%d", &test);
		int sum = test;
		int val = 0;
		ans = test;
		while(-- n)
		{
			scanf("%d", &val);
			if(ans > val)  ans = val;
			test ^= val;
			sum += val;
		}
		gcj_out(pz);
		if(0 == test)  printf("%d\n", sum - ans);
		else puts("NO");
	}
	return 0;
}