#include<stdio.h>
#include<cstring>
using namespace std;
inline int gn()
{
	char c=getchar();
	int a=0;bool f=false;
	while(c>='0'&&c<='9')
	{
		f=true;
		a*=10;a+=(c-'0');
		if((c=getchar())==EOF)break;
	}
	return f?a:gn();
}
int t,r,k,n,nu[1001];
bool nn[1001];
int du[1001],nextt[1001];
int main()
{
	freopen("aaa.out","w",stdout);
	freopen("C-large.in","r",stdin);
	t=gn();
	int co=0;
	while(t--)
	{
		co++;
		r=gn();k=gn();n=gn();
		for(int i=0;i<n;i++)
			nu[i]=gn();
		memset(nn,false,sizeof(nn));
		memset(du,0,sizeof(du));
		memset(nextt,-1,sizeof(nextt));
		int tt=0,nt=0;
		long long income=0;
		long long ca=0;
		for(int i=0;i<r;i++)
		{
			if(!nn[tt])
			{
			nn[tt]=true;
			ca=0;nt=0;int a=tt;
			while(ca+nu[tt]<=k&&nt<n){ca+=nu[tt++];tt%=n;nt++;}
			nextt[a]=tt;
			du[a]=ca;
			income+=ca;
			}
			else
			{
				income+=du[tt];tt=nextt[tt];
			}
		}
		printf("Case #%d: %I64d\n",co,income);
	}
	scanf(" ");
	return 0;
}
