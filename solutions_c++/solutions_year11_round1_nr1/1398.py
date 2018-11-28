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

const int INF = 1000;
int ary1[INF], ary2[INF];
//template <class T>
bool cmp(const int &a, const int &b)
{
	return a > b;
}
int qcmp(const void* a, const void* b)
{
	return *(int*)b - *(int*)a;
}
int gcd(int a, int b)
{
	int r = 1;
	while(r)
	{
		r = a % b;
		a = b;
		b = r;
	}
	return a;
}
int main(void)
{
	//baby_jean;
	int n, T, I;
	//#define LARGE
	#define SMALL
#ifdef LARGE
	freopen("C:\\Users\\Pzjay\\Downloads\\A-large-practice.in", "rt", stdin);
	freopen("C:\\Users\\Pzjay\\Downloads\\A-large-practice.out", "wt", stdout);
#endif
#ifdef SMALL
	freopen("C:\\Users\\Pzjay\\Downloads\\A-small-attempt0.in", "rt", stdin);
	freopen("C:\\Users\\Pzjay\\Downloads\\A-small.out", "wt", stdout);
#endif
	scanf("%d", &T);
	int pg, pd;
	for(int pz = 1; pz <= T; ++ pz)
	{
		scanf("%d %d %d", &n, &pd, &pg);	
		gcj_out(pz);
		if(100 != pd)
			if(100 == pg)
			{
				puts("Broken");
				continue;
			}
		if(pd > 0 && 0 == pg)
		{
			puts("Broken");
			continue;
		}
		int GCD = gcd(pd, 100);
		pd /= GCD;
		if(100 / GCD > n) puts("Broken");
		else  puts("Possible");
	}
	return 0;
}