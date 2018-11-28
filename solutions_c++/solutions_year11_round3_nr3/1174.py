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
#include "windows.h"
using namespace std;

#define baby_jean std::cout<<"jean"[1]<<std::endl
#define gcj_out(idx)  printf("Case #%d: ", idx)
#define memcls(ary, val) memset(ary, val, sizeof ary)
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

const int INF = 1010;
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
int ary[INF];
bool ok(int MOD, int n)
{
	for(int i = 1; i <= n; ++ i)
		if(0 != ary[i] % MOD)
			if(0 != MOD % ary[i])  return 0;
	return 1;
}
int main(void)
{
	//baby_jean;
	int n, T, I;
	//#define LARGE
	#define SMALL
#ifdef LARGE
	freopen("C:\\Users\\Pzjay\\Downloads\\A-large.in", "rt", stdin);
	freopen("C:\\Users\\Pzjay\\Downloads\\A-large.out", "wt", stdout);
#endif
#ifdef SMALL
	freopen("C:\\Users\\Pzjay\\Downloads\\C-small-attempt0.in", "rt", stdin);
	//freopen("C:\\Users\\Pzjay\\Downloads\\C-small.out", "wt", stdout);
#endif
	/*
	__int64 ll = 2;
	ll <<= 23;
	cout<<ll<<endl;
*/
	scanf("%d", &T);
	int L, H;
	
	for(int pz = 1; pz <= T; ++ pz)
	{
		bool ext = false;
		int R, C;
		scanf("%d", &n);
		scanf("%d %d", &R, &C);
		for(int i = 1; i <= n; ++ i)  scanf("%d", ary + i);
		gcj_out(pz);
		for(int i = R; i <= C; ++ i) if(ok(i, n))
			{
				printf("%d\n", i);
				ext = true;
				break;
			}
		if(!ext)  puts("NO");
	}
	return 0;
}