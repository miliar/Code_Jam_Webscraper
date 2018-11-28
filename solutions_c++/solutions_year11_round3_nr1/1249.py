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
	char ary[INF][INF];
	scanf("%d", &T);
	
	for(int pz = 1; pz <= T; ++ pz)
	{
		bool ext = true;
		int R, C;
		scanf("%d %d", &R, &C);
		for(int i = 1; i <= R; ++ i)  scanf("%s", ary[i]);
		for(int i = 1; i <= R; ++ i)
			for(int j = 0; j < C; ++ j)
				if('#' == ary[i][j])
				{
					if(C == j + 1
						|| '#' != ary[i][j + 1]
					|| i == R
						|| '#' != ary[i + 1][j]
						|| '#' != ary[i + 1][j + 1])
					{
						ext = false;
						break;
					}
					else
					{
						ary[i][j] = '/', ary[i + 1][j] = '\\';
						ary[i][j + 1] = '\\';
						ary[i + 1][j + 1] = '/';
					}
				}
				gcj_out(pz);
				puts("");
				if(ext){
					for(int i = 1; i <= R; ++ i)  puts(ary[i]);
				}else puts("Impossible");
	}
	return 0;
}