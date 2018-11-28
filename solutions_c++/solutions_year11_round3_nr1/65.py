#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<ctime>
#include<map>
#include<vector>
#include<queue>
#include<sstream>
#include<stack>
using namespace std;

#define INF 0x7fffffff
#define EPS 1e-8

typedef long long LL;

void init(int mode,string problem)
{
	string infile="C:\\Users\\LaiLi\\Desktop\\GCJ\\";
	string outfile="C:\\Users\\LaiLi\\Desktop\\GCJ\\";
	if(mode==0)
		return;
	if(mode==1)
	{
		infile+=problem+"-small.in";
		outfile+=problem+"-small.out";
	}
	if(mode==2)
	{
		infile+=problem+"-large.in";
		outfile+=problem+"-large.out";
	}
	freopen(infile.c_str(),"r",stdin);
	freopen(outfile.c_str(),"w",stdout);
}

string solve()
{
	string ans;
	
	int n,m,i,j;
	char mp[105][105];
	scanf("%d%d",&n,&m);
	for(i=0;i<n;i++)
	{
		scanf("%s",mp[i]);
	}
	bool flag=0;
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			if(mp[i][j]!='#')
				continue;
			if(i==n-1||j==m-1||mp[i][j+1]!='#'||mp[i+1][j]!='#'||mp[i+1][j+1]!='#')
			{
				flag=1;
			}
			if(flag)
			{
				goto res;
			}
			mp[i][j]='/';
			mp[i][j+1]='\\';
			mp[i+1][j]='\\';
			mp[i+1][j+1]='/';
		}
	}
	ans='\n';
res:if(flag)
	{
		ans='\n';
		ans+="Impossible\n";
	}
	else
	{
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
				ans+=mp[i][j];
			ans+='\n';
		}
	}

	return ans;
}

int main()
{
	init(2,"A");

	int T,cs;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		printf("Case #%d: %s",cs,solve().data());
		fflush(stdout);
	}
}