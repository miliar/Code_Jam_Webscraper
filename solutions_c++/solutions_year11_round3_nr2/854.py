#include <cstdio>
#include <iostream>
#include <memory.h>
#include <vector>
using namespace std;

const int MAX_C = 1024;
const int MAX_N = 1<<20;

int L, t, N, C;
int a[MAX_C];
int sum[MAX_N];

void input()
{
	scanf("%d%d%d%d", &L, &t, &N, &C);

	for(int i=0; i<C; i++)
		scanf("%d", &a[i]);
		
	sum[0] = 0;
	for(int i=1; i<=N; i++)
		sum[i] = sum[i-1] + a[(i-1)%C];
		
	for(int i=1; i<=N; i++) {
		sum[i] *= 2;
		//printf("%d: %d\n", i, sum[i]);
	}
}

int gain(int i, int yetgain)
{
	return ((sum[i+1]-yetgain) - max(t, sum[i]-yetgain)) / 2;
}

int solve()
{
	int i, j, g, gi, ans=0;
	
	if(L==0) ;
	else if (L==1) {
		for(i=0; i<N; i++) {
			gi = gain(i,0);
			if(gi>ans) ans=gi;
		}
	} if(L==2) {
		for(i=0; i<N; i++) {
			gi = gain(i,0);
			for(j=i+1; j<N; j++) {
					g = gi + gain(j,gi);
					if(g>ans) ans=g;
				}	
		}
	}
	
	return (sum[N]-ans);
}

void output(int t, int ans)
{
	printf("Case #%d: ", t);
	
	if(ans==-1) printf("NO\n");
	else printf("%d\n", ans);
}

int main()
{
	int i, t;
	scanf("%d", &t);

	for(i=1; i<=t; i++) {
		input();
		output(i, solve());
	}
	
	return 0;
}
