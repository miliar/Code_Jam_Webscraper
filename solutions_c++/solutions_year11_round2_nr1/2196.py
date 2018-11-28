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

const int INF = 10010;
//template <class T>
bool cmp(const int &a, const int &b)
{
	return a > b;
}
int qcmp(const void* a, const void* b)
{
	return *(int*)b - *(int*)a;
}
/*
dp[i][j]
*/
class cls
{
public:
	int opera;
	int nxt;
}pero[INF];
double wp[INF / 100], owp[INF / 100], oowp[INF / 100];
int main(void)
{
	//baby_jean;
	int n, T, I;
	#define LARGE
	//#define SMALL
#ifdef LARGE
	freopen("C:\\Users\\Pzjay\\Downloads\\A-large.in", "rt", stdin);
	freopen("C:\\Users\\Pzjay\\Downloads\\A-large.out", "wt", stdout);
#endif
#ifdef SMALL
	freopen("C:\\Users\\Pzjay\\Downloads\\A-small-attempt0.in", "rt", stdin);
	freopen("C:\\Users\\Pzjay\\Downloads\\A-small.out", "wt", stdout);
#endif
	int c, d;
	char ary[INF / 100][INF / 100];
	int opt[INF / 100];
	scanf("%d", &T);
	int a[INF / 100], cnt[INF / 100];
	for(int pz = 1; pz <= T; ++ pz)
	{
		double RPI;
		memcls(oowp, 0), memcls(owp, 0);
		memcls(opt, -1), memcls(a, 0);
		memcls(cnt, 0);
		scanf("%d", &n);
		int dge = 0;
		for(int i = 0; i < n; ++ i) 
			scanf("%s", ary + i);
		int ege = 0;
		gcj_out(pz);
		for(int i = 0; i < n; ++ i)
		{
			for(int j = i + 1; j < n; ++ j)
			{
				if('.' != ary[i][j])
				{
					pero[ege].opera = j;
					pero[ege].nxt = opt[i];
					opt[i] = ege;
				    pero[++ ege].opera = i;
					pero[ege].nxt = opt[j];
					opt[j] = ege;
					++ cnt[i], ++ cnt[j];
					++ ege;
					if('1' != ary[i][j])  ++ a[j];
					else ++ a[i];
				}
			}
			wp[i] = (double)a[i] / cnt[i];
		}
		for(int i = 0; i < n; ++ i)
		{
			int tp = 0;
			for(int j = opt[i];-1 != j; j = pero[j].nxt)
			{
				++ tp;
				if('0' == ary[i][pero[j].opera]) 
					owp[i] += 1.0 * (a[pero[j].opera] - 1) / (cnt[pero[j].opera] - 1);
				else  owp[i] += a[pero[j].opera] / (double)(cnt[pero[j].opera] - 1);
			}
			owp[i] /= tp;
		}
		puts("");
		for(int i = 0; i < n;++ i)
		{
			int tp = 0;
			for(int j = opt[i];-1 != j;j = pero[j].nxt)
			{
				++ tp;
				oowp[i] += owp[pero[j].opera];
			}
			oowp[i] /= tp;
		
		}
		for(int i = 0;i < n; ++ i)
		{
			RPI = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf("%.12f\n",RPI);
		}
	}
	return 0;
}