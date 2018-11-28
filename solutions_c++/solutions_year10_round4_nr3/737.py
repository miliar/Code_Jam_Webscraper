#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<iterator>
using namespace std;

#define i64 __int64
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf ((i64)1<<30)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define eps 1e-11
#define NCOUNT 110

char mat[110][110],tmp[110][110];
int r,n,m;

bool alldead()
{
	int i,j;
	for(i=1;i<=NCOUNT;i++)
	{
		for(j=1;j<=NCOUNT;j++)
		{
			if(mat[i][j]=='1')
				return false;
		}
	}
	return true;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,i,j,ax,ay,bx,by,k,css=1,t;
	cin>>cs;
	while(cs--)
	{
		cin>>r;
		for(i=0;i<=NCOUNT;i++)
		{
			for(j=0;j<=NCOUNT;j++)
			{
				mat[i][j]='0';
				tmp[i][j]='0';
			}
		}
		while(r--)
		{
			cin>>ax>>ay>>bx>>by;
			for(i=ax;i<=bx;i++)
			{
				for(j=ay;j<=by;j++)
				{
					mat[j][i]='1';
				}
			}
		}
		for(t=0;;t++)
		{
			if(alldead())
			{
				break;
			}
			for(i=1;i<=NCOUNT;i++)
			{
				for(j=1;j<=NCOUNT;j++)
				{
					if(mat[j][i-1]=='0' && mat[j-1][i]=='0')
						tmp[j][i]='0';
					else if(mat[j][i-1]=='1' && mat[j-1][i]=='1')
						tmp[j][i]='1';
					else
						tmp[j][i]=mat[j][i];
				}
			}
			for(i=1;i<=NCOUNT;i++)
			{
				for(j=1;j<=NCOUNT;j++)
				{
					mat[j][i]=tmp[j][i];
				}
			}
		}
		printf("Case #%d: %d\n",css++,t);
	}
	return 0;
}


