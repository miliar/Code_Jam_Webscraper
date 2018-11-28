#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define M 110

bool g[M][M];
int n,K;

int data[M][M];

void read_data()
{
	cin >> n >> K;
	int i,j;
	for (i=1;i<=n;i++)
		for (j=1;j<=K;j++) cin >> data[i][j];
}

bool check(int a,int b)
{
	if (data[a][1] <= data[b][1]) return false;
	int i;
	for (i=2;i<=K;i++) if (data[a][i] <= data[b][i]) return false;
}

void init()
{
	int i,j;
	for (i=1;i<=n;i++)
		for (j=1;j<=n;j++) if (i != j) g[i][j] = check(i,j);
}

bool y[M];
int lk[M];

bool Find(int s)
{
	int i;
	for (i=1;i<=n;i++) if (g[s][i] && !y[i])
	{
		y[i] = true;
		if (lk[i] == -1 || Find(lk[i]))
		{
			lk[i] = s;
			return true;
		}
	}
	return false;
}

int work_ans()
{
	int i,res = 0;
	memset(lk,-1,sizeof(lk));
	for (i=1;i<=n;i++)
	{
		memset(y,false,sizeof(y));
		if (Find(i)) res++;
	}
	return n - res;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int ans,t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		read_data();
		init();
		ans = work_ans();
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
