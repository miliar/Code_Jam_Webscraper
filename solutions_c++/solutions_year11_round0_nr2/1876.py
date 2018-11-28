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
#include <assert.h>
using namespace std;

#define baby_jean std::cout<<"jean"[1]<<std::endl
#define gcj_out(idx)  printf("Case #%d: ", idx)
#define memcls(ary, val) memset(ary, val, sizeof ary)
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

const int INF = 205;
/*
dp[i][j]表示前i个字母0--j[welcome to code jam]出现多少次//wwweellccoommee
if(gcj[j] == str[i + 1]) 
dp[i + 1][j] = dp[i][j - 1] + dp[i][j]
else
dp[i + 1][j] = dp[i][j]
边界：dp[0-->n][0]
*/
void debugg(vector<char> tp)
{
	puts("debug");
	cout<<tp.size()<<endl;
	for(int i = 0; i < tp.size(); ++ i)  printf("%c ", tp[i]);
	puts("");
}
vector <char> ans;
int main(void)
{
	#define LARGE
//#define SMALL

#ifdef LARGE
	freopen("C:\\Users\\Pzjay\\Downloads\\B-large.in", "rt", stdin);
	freopen("C:\\Users\\Pzjay\\Downloads\\B-large-practice.out", "wt", stdout);
#endif
#ifdef SMALL
	freopen("C:\\Users\\Pzjay\\Downloads\\B-small-attempt4.in", "rt", stdin);
	freopen("C:\\Users\\Pzjay\\Downloads\\B-small.out", "wt", stdout);
#endif
	char opt[INF];
	int T, n;
	char comp[INF][INF];
	bool oppo[INF][INF];
	/*
	两堆数做抑或，值相等，但一个最大，一个最小
	{Q, W, E, R, A, S, D, F}
	*/
	int com, opp;
	char tp[5];
	scanf("%d", &T);
	
	for(int pz = 1; pz <= T; ++ pz)
	{
		ans.clear();
		for(int i = 0; i < INF; ++ i)
			for(int j = 0; j < INF; ++ j)  
			{
				oppo[i][j] = false;
				comp[i][j] = '$';
			}
		//memcls(oppo, false);
		scanf("%d", &com);
		//strcpy(opt, "");
		int ct = 0;
		while(com --)
		{
			scanf("%s", tp);
			comp[tp[0] - 'A' + 1][tp[1] - 'A' + 1] = tp[2];
			comp[tp[1] - 'A' + 1][tp[0] - 'A' + 1] = tp[2];
		}
		scanf("%d", &opp);
		while(opp --)
		{
			scanf("%s", tp);
			oppo[tp[0] - 'A' + 1][tp[1] - 'A' + 1] = true;
			oppo[tp[1] - 'A' + 1][tp[0] - 'A' + 1] = true;
		}
		scanf("%d %s", &n, opt);
		for(int i = 0; i < n; ++ i)
		{
			char pzj = '$';
//cout<<"opt["<<i<<"] "<<opt[i]<<endl;
			ans.push_back(opt[i]);
//debugg(ans);
			int jj = ans.size() - 1;

//if(jj > 0) {cout<<"chekc jj = "<<jj<<" "<<ans[jj]<<"  "<<ans[jj - 1]<<endl;
//cout<<ans[jj] - 'A' + 1<<" next "<<ans[jj - 1] - 'A' + 1<<endl;}
			
			if(jj > 0) pzj = comp[ans[jj] - 'A' + 1][ans[jj - 1] - 'A' + 1];
			if('$' != pzj && jj > 0)
			{
//cout<<"\t\ttou "<<ans.size()<<endl;
//cout<<"neibu "<<endl;
//debugg(ans);
				ans.pop_back();
				ans.pop_back();
				ans.push_back(pzj);
				continue;
			}

			for(int j = ans.size() - 1; j >=0; -- j)
			{
				for(int k = j - 1; k >= 0; -- k)
				{
					if(oppo[ans[j] - 'A' + 1][ans[k] - 'A' + 1])
					{
//debugg(ans);
						//cout<<"j "<<j<<" k "<<k<<endl;
						/*ans.erase(ans.begin() + k, 
							ans.begin() + j + 1);*/
						ans.clear();
//debugg(ans);
						break;
					}
				}
				if(ans.size() <= j) j = ans.size() - 1;
				if(j <= 0)  break;
				//cout<<"\t\t\tthgis\n";
			}
		}
		gcj_out(pz);
		putchar('[');
		if(0 == ans.size()) 
		{
			puts("]");
			continue;
		}
		//cout<<"size "<<ans.size()<<" "<<ans[ans.size() - 1]<<endl;
		for(int i = 0; i < ans.size() - 1; ++ i)	
		{
			putchar(ans[i]);
			putchar(',');
			putchar(' ');
		}
		putchar(ans[ans.size() - 1]);
		puts("]");
//debugg(ans);
	}
	return 0;
}