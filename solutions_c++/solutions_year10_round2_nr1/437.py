#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#define maxw 40
#define maxp 100001
using namespace std;
int res,n,m,tim;
int s[maxp][maxw];
int con;
int len;
char ss[maxp];
int now;
inline void addp(int &p,char ch)
{
	int temp;
	if('a'<=ch&&ch<='z')	temp=ch-'a';
	else
	if('0'<=ch&&ch<='9')	temp=ch-'0'+27;
	else
	temp=maxw-1;
	if(!s[p][temp])
		s[p][temp]=++con;
	p=s[p][temp];
}
inline void checkp(int &p,char ch)
{
	int temp;
	if('a'<=ch&&ch<='z')	temp=ch-'a';
	else
	if('0'<=ch&&ch<='9')	temp=ch-'0'+27;
	else
	temp=maxw-1;
	if(!s[p][temp])
	{
		s[p][temp]=++con;
		if(temp==maxw-1)
			res++;
	}
	p=s[p][temp];
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d\n",&tim);
	for(int tt=1;tt<=tim;tt++)
	{
		printf("Case #%d: ",tt);
		scanf("%d %d",&n,&m);
		res=0;
		con=0;
		memset(s,0,sizeof(s));
		for(int i=1;i<=n;i++)
		{
			scanf("%s\n",&ss);
			len=strlen(ss);
			ss[len++]='/';
			now=0;
			for(int j=1;j<len;j++)
				addp(now,ss[j]);
		}
		for(int i=1;i<=m;i++)
		{
			scanf("%s\n",&ss);
			len=strlen(ss);
			ss[len++]='/';
			now=0;
			for(int j=1;j<len;j++)
				checkp(now,ss[j]);
		}
		printf("%d\n",res);
	}
	return 0;
}
