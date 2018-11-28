#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

#define MAXN 50

int n,ans,data[MAXN];

inline bool check()
{
	int i;
	for (i=1;i<=n;i++)
		if (data[i]>i)
			return false;
	return true;
}

inline void swap(int &a,int &b)
{
	int zan=a;
	a=b;
	b=zan;
}


void run()
{
	int i,k,p;
	for (i=1;i<=n;i++)
	{
		if (data[i]<=i)
			continue;
		else
			for (k=i+1;k<=n;k++)
			{
				if (data[k]<=i)
				{
					for (p=k;p>i;p--)
					{
						swap(data[p],data[p-1]);
						ans++;
					}
					break;
				}
			}
	}
}


void ini()
{
	int k,i,j,last,T;
	char c;
	cin>>T;
	for (k=1;k<=T;k++)
	{
		ans=0;
		memset(data,0,sizeof(data));
		scanf("%d\n",&n);
		for (i=1;i<=n;i++)
		{
			last=0;
			for (j=1;j<=n;j++)
			{
				scanf("%c",&c);
				if (c=='1')
					last=j;	
			}
			data[i]=last;
			scanf("\n");
		}
		run();
		printf("Case #%d: %d\n",k,ans);
	}
}


int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	ini();
	return 0;
}
