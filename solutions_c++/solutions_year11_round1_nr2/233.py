#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<complex>
#define mp make_pair
#define pb push_back
#define all(x) (x.begin(),x.end())
using namespace std;
string s[12000];
char o[30];
int n,m;
int rev[300];
int match(string x,string y)
{
	if (x.length()!=y.length())return 0;
	for (int i=0;i<x.length();i++)
	{
		if (y[i]=='-')
		{
			if (rev[x[i]])return 0;
			continue;
		}
		if (x[i]!=y[i])return 0;
	}
	return 1;
}
int nt[300];
bool nope(string x)
{
	for (int i=0;i<x.length();i++)
	{
		if (nt[x[i]])return 1;
	}
	return 0;
}
int gao()
{
	int i,j,k,ans=-1,pos=-1;
	for (i=0;i<n;i++)
	{
		int tl=s[i].length();
		string tar(tl,'-');
		memset(nt,0,sizeof(nt));
		memset(rev,0,sizeof(rev));
		int wr=0;
		for (j=0;j<26;j++)
		{
			int has=0,now=0;
			for (k=0;k<n;k++)
			{
				if (!match(s[k],tar))continue;
				if (nope(s[k]))continue;
				now++;
				if (s[k].find(o[j])!=string::npos)++has;
			}
			if (has==0)continue;
			int fd=0;
			for (k=0;k<tl;k++)
			{
				if (s[i][k]==o[j])
				{
					fd=1;
					tar[k]=o[j];
				}
			}
			if (!fd)
			{
				wr++;
				nt[o[j]]=1;
			}
			else 
			{
				rev[o[j]]=1;
			}
			if (tar.find('-')==string::npos)break;
		}
		if (wr>ans)
		{
			ans=wr;
			pos=i;
		}
	}
	//printf("%d\n",ans);
	return pos;
}
int main()
{
	freopen("C:\\Users\\daizhy\\Documents\\output.txt","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++)
		{
			char ss[20]={0};
			scanf("%s",ss);
			s[i]=(string)ss;
		}
		printf("Case #%d:",++cc);
		for (i=0;i<m;i++)
		{
			scanf("%s",o);
			printf(" %s",s[gao()].c_str());
		}
		puts("");
	}
	return 0;
}
		
