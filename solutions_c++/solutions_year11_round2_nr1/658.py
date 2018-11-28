#include<stdio.h>
#include<string>
#include<queue>
#include<set>
#include<cstring>
#include<assert.h>
#include<iostream>
#include<map>
#include<algorithm>
#define sf scanf
#define pf printf
#define clr(key) memset(key,0,sizeof(key))
using namespace std;
#define ll long long

string str[200];
double wp[200],op[200],oop[200];
double wwp[200];
int n;


int getoop()
{
	for(int i=0;i<n;++i)
	{
		double sum =0;
		int tot = 0;
		for(int j=0;j<str[i].size();++j)
		{
			if( str[i][j]!='.' )
			{
				sum += op[j];	
				tot++;
			}
		}
		oop[i]=sum/tot;
		//printf("oop %d:%lf\n",i,oop[i]);
	}
}

int getop()
{
	for(int i=0;i<n;++i)
	{
		memset(wwp,0,sizeof(wwp));
		for(int k=0;k<n;++k)
		{
			int sum =0;
			int tot = 0;
			for(int j=0;j<str[k].size();++j)
			{
				if( i == j ) continue;

				if( str[k][j]!='.' )
				{
					if( str[k][j] == '1' )
						sum ++;
					tot++;
				}
			}
			wwp[k] = (double)sum/tot;
		}
		double sum = 0;
		int tot = 0;
		for(int k=0;k<n;++k)
		{
			if( str[k][i] != '.' )
			{
				sum += wwp[k];
				tot++;
			}
		}
		op[i]=sum/tot;
		//printf("op %d:%lf\n",i,op[i]);
	}
}

int getwp()
{
	for(int i=0;i<n;++i)
	{
		int tot=0,ret=0;
		for(int j=0;j<str[i].size();++j)
		{
			if( str[i][j] == '0' || str[i][j] == '1' ) 
				tot++;
			if( str[i][j] == '1' )
				ret++;
		}
		wp[i]=(double)ret/tot;
		//printf("wp %d:%lf\n",i,wp[i]);
	}
}
int main()
{
	int T;
	scanf("%d",&T);
	int ca=0;
	while(T--)
	{
		scanf("%d",&n);
		for(int i=0;i<n;++i)
		{
			cin>>str[i];
		}
		getwp();
		getop();
		getoop();
		printf("Case #%d:\n",++ca);
		for(int i=0;i<n;++i)
		{
			printf("%.9lf\n",0.25*wp[i]+0.5*op[i]+0.25*oop[i]);
		}
	}
}

