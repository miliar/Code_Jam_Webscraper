#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;
int to[30],deg[40];
int _,ca,n,K,i,j,x,y,ret,ct;
int co[40][40];
char s[12000];
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	memset(to,-1,sizeof(to));
	to['o'-'a']=26;
	to['i'-'a']=27;
	to['e'-'a']=28;
	to['a'-'a']=29;
	to['s'-'a']=30;
	to['t'-'a']=31;
	to['b'-'a']=32;
	to['g'-'a']=33;
	scanf("%d",&_);
	for(ca=1;ca<=_;ca++)
	{
		memset(deg,0,sizeof(deg));
		memset(co,0,sizeof(co));
		scanf("%d",&K);
		scanf("%s",s);
		n=strlen(s);
		for(i=1;i<n;i++)
		{
			x=s[i-1]-'a';
			y=s[i]-'a';
			if(!co[x][y])
			deg[x]++,deg[y]--,co[x][y]=1;
			if(to[x]!=-1&&!co[to[x]][y])
			deg[to[x]]++,deg[y]--,co[to[x]][y]=1;
			if(to[y]!=-1&&!co[x][to[y]])
			deg[x]++,deg[to[y]]--,co[x][to[y]]=1;
			if(to[x]!=-1&&to[y]!=-1&&!co[to[x]][to[y]])
			deg[to[x]]++,deg[to[y]]--,co[to[x]][to[y]]=1;
		}
		ret=1;
		for(i=0;i<34;i++)
		for(j=0;j<34;j++)
		if(co[i][j])ret++;
		ct=0;
		//for(i=0;i<34;i++)printf("%d ",deg[i]);puts("");
		for(i=0;i<34;i++)
		if(deg[i]>0)ct+=deg[i];
	//	printf("%d %d\n",ret,ct);
		ret+=max(0,ct-1);
		printf("Case #%d: %d\n",ca,ret);
	}
}
