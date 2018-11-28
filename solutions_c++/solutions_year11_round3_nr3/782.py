#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<math.h>
#include<cmath>
#define eps 1e-11
#define INF (2<<31)-1
#define siz 500000

using namespace std;

int max(int a, int b) {
	if(a>b) return a;
	return b;
}
int min(int a, int b){
	if(a<b) return a;
	return b;
}

int gcd(int a, int b)
{
	int c;
	if(a>b)
		swap(a, b);
	if(a==b)
		return b;
	while(a>0)
	{
		c=b%a;
		b=a;
		a=c;
	}
	return b;
}

vector<int> adj[siz];
int t, n, m, a, b, c, ct=1;
int h, l;
int har[100000];


int main()
{
	freopen("c.in","r",stdin);
		freopen("out.txt","w",stdout);
	int i, j, res, m1, m2;
	int gd=1;
	scanf("%d", &t);
	while(t--)
	{
		gd=0;
		m1=0;
		m2=INF;
		scanf("%d %d %d", &n, &l, &h);
		for(i=0;i<n;i++)
		{
			scanf("%d", &har[i] );
			m1=max(m2, har[i] );
			m2=min(m2, har[i] );
		}
		int w=0;
		res=0;
		for(j=l;j<=h;j++)
		{
			res=0;
			for(i=0;i<n;i++)
			{
				if(har[i]>=j)
				{
					if( (har[i]%j)==0 )
						res++;
				}
				else
				{
					if( (j%har[i])==0 )
						res++;
				}
			}
			if(res==n)
			{
				w=j;
				break;
			}
			else
				res=0;
		}
		
		if(res==0)
			printf("Case #%d: NO\n", ct++);
		else
			printf("Case #%d: %d\n", ct++, w);
		
	}
	
	return 0;
	
}
