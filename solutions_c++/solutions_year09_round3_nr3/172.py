#include <iostream>
#include <cstring>
#include <sstream>
#include <cmath>
using namespace std;
#define MAXN 100000000
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

int ans,t;
int P,Q;
int pos[105];
int f[105][105];
bool hash[105][105];

int Dp(int s, int t)
{
	if(hash[s][t])
		return f[s][t];
	int tmp;
	hash[s][t] = true;
	f[s][t] = MAXN;
	for(int i = s+1; i < t; i++)
	{
		tmp = pos[i]-pos[s]+pos[t]-pos[i]-2;
		if(i>s)
			tmp += Dp(s,i);
		if(i<t)
			tmp += Dp(i,t);
		f[s][t] = MIN(f[s][t],tmp);
	}
	return f[s][t];
}

void init()
{
	scanf("%d %d",&P,&Q);
	pos[0] = 0, pos[Q+1] = P+1;
	for(int i = 1; i <= Q; i++)
		scanf("%d",&pos[i]);
	Q++;
	memset(hash,0,sizeof(hash));
	for(int i = 0; i <= Q; i++)
		f[i][i] = 0, hash[i][i] = true;
	for(int i = 0; i < Q; i++)
		f[i][i+1] = 0, hash[i][i+1] = true;
}

void solve()
{
	ans = Dp(0,Q);
}

void print()
{
	printf("Case #%d: %d\n",t+1,ans);
}

int main(void)
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
	int T;
	scanf("%d\n",&T);
	for(t = 0; t < T; t++)
	{
		init();
		solve();
		print();
	}
    return 0;
}
