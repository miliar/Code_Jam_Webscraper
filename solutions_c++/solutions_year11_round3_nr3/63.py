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

	int n,l,h,i,j;
	int a[105];
	scanf("%d%d%d",&n,&l,&h);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	for(i=l;i<=h;i++)
	{
		for(j=0;j<n;j++)
		{
			if(i>=a[j]&&i%a[j]==0||i<a[j]&&a[j]%i==0)
				continue;
			else
				break;
		}
		if(j==n)
			break;
	}
	if(i>h)
		ans="NO";
	else
	{
		char tmp[1005];
		sprintf(tmp,"%d",i);
		ans=tmp;
	}

	return ans;
}

int main()
{
	init(1,"C");

	int T,cs;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		printf("Case #%d: %s\n",cs,solve().data());
		fflush(stdout);
	}
}