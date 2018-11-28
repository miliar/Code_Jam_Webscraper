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
	freopen("C:\\Users\\Pzjay\\Downloads\\A-large.in", "rt", stdin);
	freopen("C:\\Users\\Pzjay\\Downloads\\A-large-practice.out", "wt", stdout);
#endif
#ifdef SMALL
	freopen("C:\\Users\\Pzjay\\Downloads\\A-small-attempt3.in", "rt", stdin);
	freopen("C:\\Users\\Pzjay\\Downloads\\A-small-practice.out", "wt", stdout);
#endif
	int T, n;
	/*
	记录o和b的上个位置，同时记录上次移动的角色和当前花费时间
	,
	*/
	scanf("%d", &T);
	char rol1, rol2;
	for(int pz = 1; pz <= T; ++ pz)
	{
		rol2 = '1';
		int cur;
		scanf("%d", &n);
		int span = 0;
		int poso = 1, posb = 1;
		int ans = 0;
		while(n --)
		{
			getchar();
			scanf("%c %d", &rol1, &cur);
			//cout<<rol1<<"\t"<<cur<<endl;
			if(rol2 == rol1)
			{
				if('B' == rol1)
				{
					span += abs(cur - posb) + 1;
					ans += abs(cur - posb) + 1;
				}
				else if('O' == rol1)
				{
					span += abs(cur - poso) + 1;
					ans += abs(cur - poso) + 1;
				}
			}
			else
			{
				if('O' == rol1)
				{
					if(abs(cur - poso) > span)
					{
						ans += abs(cur - poso) - span;
						span = abs(cur - poso) - span + 1;
					}
					else span = 1; 
				}
				else if('B' == rol1)
				{
					if(abs(cur - posb) > span)
					{
						ans += abs(cur - posb) - span;
						span = abs(cur - posb) - span + 1;
					}
					else span = 1;
				}
				++ ans;
			}
			//cout<<ans<<" "<<span<<endl;
			if('O' == rol1) poso = cur;
			else if('B' == rol1)  posb = cur;
			rol2 = rol1;
		}
		gcj_out(pz);
		printf("%d\n", ans);
	}
	return 0;
}