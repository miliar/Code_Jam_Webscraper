#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#define MAX 1000000
#define BIT(x) (1<<(x-1))
using namespace std;
#define min(a,b) (((a) < (b)) ? (a) : (b))
__int64 L,t,N,C;
int B;
int dis[MAX+1];
__int64 rev;
__int64 total;
void readdata()
{
	int i;
	__int64 sum=0;
	int flag = 1;
	total = 0;
	memset(dis, 0, sizeof(dis));
	rev = 0;

	scanf("%lld%lld%lld%lld", &L, &t, &N, &C);
	for (i=0; i<C; ++i) {
		scanf("%d", &dis[i]);		
	}
	
	for (i=0; i<N; ++i) {
		dis[i] = dis[i%C];
		total += dis[i]*2;
		if (total > t && flag) {
			B = i;
			flag = 0;
			rev = total;
		}
	}

}

void solve()
{
	int i,j,index;
	int mmax,x;
	for (i=0; i<L; ++i) {
		mmax = rev - t;
		x = B;
		for (index = B+1; index <N; ++index) {
			if (dis[index]*2 > mmax) {
				x = index;
				mmax = dis[index]*2;
			}
		}

		total -= mmax/2;
		dis[x] = 0;
	}
}

void output()
{
	printf("%lld\n", total);
}
int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("small.out", "w", stdout);
	int nt, it;
	
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		readdata();
		solve();
		printf("Case #%d: ",it);
		output();
		
	}
	return 0;
}