#include<cstdio>
#include<cstring>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int n,M,t,A,B,C,D,x0,y0,ans;
int a[1010],f[1010];

int gcd(int a,int b)
{
	return b?gcd(b,a%b):a;
}

void init(int n)
{
	for(int i=0;i<=n;i++)f[i]=i;
}

int fr(int a)
{
	if(f[a]!=a)f[a]=fr(f[a]);
	return f[a];
}

void unio(int a, int b)
{
	int ra=fr(a),rb=fr(b);
	if(ra!=rb) f[ra]=rb;
}

bool judge(int x)
{
	for(int i=2;i<M;i++)
	{
		while(x%i==0)x/=i;
	}
	if(x>1)return 1;
	return 0;
}

int main()
{
	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		scanf("%d%d%d",&A,&B,&M);
		init(1001);
//		for(int i=0;i<1010;i++)
//		    a[i]=i;
		for(int i=A;i<=B;i++)
		{
			for(int j=A;j<=B;j++)if(j!=i)
			{
				if(judge(gcd(i,j)))
				{
					unio(i,j);
				}
			}
		}
		ans=0;
		for(int i=A;i<=B;i++)
		{
			if(f[i]==i)ans++;
		//	printf("%d\n",a[i]);
		}
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}
