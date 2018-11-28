#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

#define SET(v,x) memset(v,x,sizeof v)

int prod[255][255], opp[255][255];
char s[111],ans[111];

void print(int p)
{
	printf("[");
	for(int i=0;i<p;i++)
	{
		if(i>0) printf(", ");
		printf("%c",ans[i]);
	}
	printf("]\n");
}

void solve()
{

	int pn, on, N;
	
	SET(prod,-1); SET(opp,0);
	
	for(scanf("%d",&pn);pn--;)
	{
		scanf("%s",s);
		int x=s[0], y=s[1], z=s[2];
		prod[x][y]=prod[y][x]=z;
	}
	
	for(scanf("%d",&on);on--;)
	{
		scanf("%s",s);
		int x=s[0], y=s[1];
		opp[x][y]=opp[y][x]=1;
	}
	
	int p = 1;
	scanf("%d %s",&N,s);
	ans[0]=s[0];
	
	for(int i=1;i<N;i++)
	{
		ans[p++] = s[i];
		
		while(1)
		{
			if(p<=1) break;
			int x = ans[p-2], y = ans[p-1];
			if(prod[x][y]!=-1){ ans[p-2]=(char)prod[x][y]; p--; }
			else
			{
				bool isOpp=false;
				for(int i=0;i<p&&!isOpp;i++) for(int j=0;j<i&&!isOpp;j++)
					if(opp[ans[i]][ans[j]]) isOpp=true;
				if(isOpp) p=0;
				break;	
			}
		}
		
		//print(p);
	}
	
	print(p);
}

int main()
{
	//freopen("B-small-attempt0.in","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	
	int kases; scanf("%d",&kases);
	
	for(int kase=1;kase<=kases;kase++)
	{
		printf("Case #%d: ",kase);
		solve();
	}
	
	return 0;
}
