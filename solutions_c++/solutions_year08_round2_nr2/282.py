#include <stdio.h>
#include <memory.h>
#include <algorithm>

using namespace std;

const int LP=1000000;
bool isprime[LP];

int prime[LP];
int pn=0;

void initprime()
{
	memset(isprime, 1, sizeof(isprime));
	isprime[0]=isprime[1]=false;
	for (int i=2; i<LP;i++)
		if (isprime[i])
		{
			prime[pn++] = i;
			for (int j=2; i*j<LP; j++)
				isprime[i*j] = false;
		}
				/*
	for (int i=0; i<30; i++)
		if (isprime[i])
			printf("%d\n", i);
			*/
	
}

static bool share(int x, int y, int p)
{
	int m = min(x, y);
	for (int i=0; i<pn; i++)
	{
		if (prime[i]>=p && x%prime[i]==0 && y%prime[i]==0)
			return true;
		if (prime[i]>m)
			break;
	}
	return false;
}

int main()
{
	initprime();
	
	int c;
	scanf("%d", &c);
	for (int ca=1; ca<=c; ca++)
	{
		int a,b,p;
		scanf("%d%d%d", &a,&b,&p);
		
		int n = b-a+1;
		
		bool g[1000][1000];
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				g[i][j] = share(a+i, a+j, p);
				
		//printf("1 done\n");
		for (int k=0; k<n; k++)
			for (int i=0; i<n; i++)
				for (int j=0; j<n; j++)
					if (g[i][k] && g[k][j])
						g[i][j] = true;
		bool ok[1000]={0};
		int cnt=0;
		for (int i=0; i<n; i++)
			if (!ok[i])
			{
				cnt++;
				for (int j=i+1; j<n; j++)
					if (g[i][j])
						ok[j]=1;
			}
		printf("Case #%d: %d\n", ca, cnt);
	}
}

