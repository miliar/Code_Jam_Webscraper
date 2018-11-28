#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

struct T
{
	int n;
	int a[10];
	int &operator [](int i){return a[i];}
}t;

vector<T>v;
int T,ts,m,n,i,j,k,ans,i1,i2,s,q;
int am[10];
bool u[10];
int b[10];

struct TT
{
	int x,y;
}a[10];

int main()
{
	freopen("c.in","r",stdin);	freopen("c.out","w",stdout);	scanf("%d",&T);
	//T=1;
	while(T--)
	{
		ans=0;
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++)
			scanf("%d",&a[i].x);
		for(i=0;i<m;i++)
			scanf("%d",&a[i].y);
		for(i=0;i<m;i++)
		{
			a[i].x--;
			a[i].y--;
		}
		for(i=0;i<n;i++)
			t[i]=i;
		t.n=n;
		v.clear();
		v.push_back(t);
		for(i=0;i<m;i++)
		{
			for(j=0;j<v.size();j++)
			{
				i1=i2=-1;
				for(k=0;k<v[j].n;k++)
				{
					if(v[j][k]==a[i].x)
						i1=k;
					if(v[j][k]==a[i].y)
						i2=k;
				}
				if(i1!=-1 && i2!=-1)
					break;
			}
			t=v[j];
			if(i1>i2)
				i1^=i2^=i1^=i2;
			for(k=i1;k<=i2;k++)
				t[k-i1]=v[j][k];
			t.n=i2-i1+1;
			v.push_back(t);
			for(k=i2;k<v[j].n;k++)
				v[j][k-i2+i1+1]=v[j][k];
			v[j].n-=i2-i1-1;
		}
		for(i=0;i<n;i++)
			b[i]=0;
		while(1)
		{
			memset(u,0,sizeof(u));
			for(i=0;i<n;i++)
				u[b[i]]=1;
			s=0;
			for(i=0;i<n;i++)
				s+=u[i];
			for(i=0;i<v.size();i++)
			{
				q=0;
				memset(u,0,sizeof(u));
				for(j=0;j<v[i].n;j++)
					u[b[v[i][j]]]=1;
				for(j=0;j<n;j++)
					q+=u[j];
				if(q<s)
					break;
			}
			if(i==v.size())
				if(s>ans)
				{
					ans=s;
					for(j=0;j<n;j++)
						am[j]=b[j];
				}
			for(i=n-1;i>=0;i--)
				if(b[i]!=n-1)
					break;
			if(i==-1)
				break;
			b[i]++;
			for(i++;i<n;i++)
				b[i]=0;
		}
		printf("Case #%d: %d\n",++ts,ans);
		for(i=0;i<n;i++)
		{
			printf("%d",am[i]+1);
			if(i==n-1)
				printf("\n");
			else
				printf(" ");
		}
	}
	return 0;
}