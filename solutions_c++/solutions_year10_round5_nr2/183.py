#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <string>
#include <iostream>
#include <queue>
#include <cmath>
#include <set>
#include <memory.h>

#define dat cin
#define sol cout
#define ll long long

using namespace std;

int a,b,d,x,y;

void gcdext(int a,int b, int *d, int *x, int *y)
{
  int s;
  if (b == 0)
  {
    *d = a; *x = 1; *y = 0;
    return;
  }
  gcdext(b,a % b,d,x,y);
  s = *y;
  *y = *x - (a / b) * (*y);
  *x = s;
}

ll gcd(ll a,ll b) {return (b==0) ? a : gcd(b,a%b);}

ll ans[100102]={0};

int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	int T;
	dat >> T;
	for(int t=1;t<=T;t++)
	{
		ll l,n,dist[101]={0};
		dat >> l >> n;
		memset(ans,-1,sizeof(ans));
		for(int i=0;i<n;i++)
		{
			dat >> dist[i];
			ans[dist[i]]=1;
		}
		ll K=100000,Ans=-1;
		for(int i=0;i<=K;i++)
			if (ans[i]!=-1)
			{
				for(int j=0;j<n;j++)
				{
					if (ans[i+dist[j]]==-1||ans[i+dist[j]]>ans[i]+1) ans[i+dist[j]]=ans[i]+1;
				}
			}
		for(int i=0;i<=K;i++)
		{
			if (ans[i]!=-1)
			{
				for(int j=0;j<n;j++)
				{
					if ((l-i)%dist[j]==0)
					{
						if (Ans==-1||Ans>ans[i]+(l-i)/dist[j]) Ans=ans[i]+(l-i)/dist[j];
					}
				}
			}
		}
		/*int g=dist[0];
		for(int i=1;i<n;i++)
		{
			gcdext(g,dist[i],&d,&x,&y);
			sol << g << "	" << dist[i] << "	" << d << "	" << x << "	" << y << endl;
			g=gcd(g,dist[i]);
		}*/
		sol << "Case #" << t <<": ";
		if (Ans==-1) sol << "IMPOSSIBLE";
		else sol << Ans;
		sol << endl;
	}
	return 0;
}

