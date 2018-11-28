#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
using namespace std;

map<int, int> vis;

int anum, bnum;
#define MAXN 10
int a[MAXN], b[MAXN], now[MAXN];

int getn(int x)
{
	int i = 0;
	for(; x; i++, x/=10);
	return i;
}
void getnum(int x[], int y)
{
	int n = getn(y);
	for(int i=n-1; i>=0; i--, y/=10)
	{
		x[i] = y%10;
	}
}
int main()
{
	int t;
	scanf("%d", &t);
	for(int T=1; T<=t; T++)
	{
		int ans = 0;
		printf("Case #%d: ", T);
		scanf("%d%d", &anum, &bnum);
		getnum(a, anum);
		getnum(b, bnum);
		int nb = getn(bnum);
		int na = getn(anum);
		for(int i=anum; i<=bnum; i++)	//产生n
		{
			vis.clear();
			getnum(now, i);
			int n = getn(i);

			for(int j=1; j<n; j++)	//start，产生m
			{
				int isa=0, isb=0;
				int isc=0;
				for(int k=0; k<n; k++)	//枚举每位
				{
					int idx = (j+k)%n;
					if(!isa) 
					{
						if(now[idx]>a[k])
							isa=1;
						else if(now[idx]<a[k])
						{
							isa = -1;
							break;
						}
					}
					if(!isb)
					{
						if(n<nb || now[idx]<b[k])
							isb=1;
						else if(now[idx]>b[k])
						{
							isb = -1;
							break;
						}
					}
					if(!isc)
					{
						if(now[idx]>now[k])
							isc=1;
						else if(now[idx]<now[k])
							break;
					}
					if(isa && isb && isc) break;
				}

				if(isa == -1 || isb == -1) continue;
				if(isc)
				{
					//printf("(%d, ", i);
					int re=0;
					for(int k=0; k<n; k++)
					{
						int idx = (j+k)%n;
						//printf("%d", now[idx]);
						re = re*10+now[idx];
					}
					if(!vis[re]) ans++;
					vis[re] = 1;
					//printf("%d", re);
					//printf(")\n");
					//break;
				}
			}
		}
		printf("%d\n", ans);
	}
}