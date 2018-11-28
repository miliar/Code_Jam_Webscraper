// File Name: a.cpp
// Author: Zlbing
// Created Time: 2013/4/13 11:00:26

#include<iostream>
#include<string>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<set>
#include<map>
#include<vector>
#include<cstring>
#include<stack>
#include<cmath>
#include<queue>
using namespace std;
#define CL(x,v); memset(x,v,sizeof(x));
#define INF 0x3f3f3f3f
#define LL long long
#define REP(i,r,n) for(int i=r;i<=n;i++)
#define RREP(i,n,r) for(int i=n;i>=r;i--)

char ch[10][10];
int main()
{
	int n;
	scanf("%d",&n);
	REP(cas,1,n)
	{
		REP(i,0,3)
			scanf("%s",ch[i]);
		printf("Case #%d: ",cas);
		int win=-1;
		bool flag=false;
		bool ct=false;
		REP(i,0,3)
			REP(j,0,3)
			if(ch[i][j]=='.')
				flag=true;
		REP(i,0,3)
		{
			int j;
			int kk,jj;
			if(ch[i][0]=='T')
			{
				jj=2;
				kk=1;
			}
			else {
				jj=1;kk=0;
			}
			if(ch[i][kk]=='.')continue;

			for(j=jj;j<4;j++)
			{
				if(ch[i][kk]!=ch[i][j]&&ch[i][j]!='T')
					break;
			}
			if(j==4)
			{
				ct=true;
				win=ch[i][kk]=='X'?0:1;
				break;
			}
		}
		REP(i,0,3)
		{
			int j;
			int kk,jj;
			if(ch[i][0]=='T')
			{
				jj=2;
				kk=1;
			}
			else {
				jj=1;kk=0;
			}
			if(ch[i][kk]=='.')continue;
			for(j=jj;j<=4;j++)
			{
				if(ch[kk][i]!=ch[j][i]&&ch[j][i]!='T')
					break;
			}
			if(j==4)
			{
				ct=true;
				win=ch[kk][i]=='X'?0:1;
				break;
			}
		}
		int k;
		int kk,ii;
		if(ch[0][0]=='T')
		{
			kk=2;
			ii=1;
		}
		else {
			kk=1;
			ii=0;
		}
		for(k=kk;k<4;k++)
			if(ch[ii][ii]!=ch[k][k]&&ch[k][k]!='T')
				break;
		if(k==4&&ch[ii][ii]!='.')
		{
			ct=true;
			win=ch[ii][ii]=='X'?0:1;
		}
		int j=2;
		kk=1;ii=0;
		if(ch[0][3]=='T')
		{
			kk=2;
			ii=1;
			j=1;
		}
		for(k=kk;k<4;k++)
		{
			if(ch[ii][3-ii]!=ch[k][j]&&ch[k][j]!='T')
				break;
			j--;
		}
		if(k==4&&ch[ii][3-ii]!='.')
		{
			ct=true;
			win=ch[ii][3-ii]=='X'?0:1;
		}
		if(ct)
		{
			if(win==0)printf("X");
			else printf("O");
			printf(" won");
		}
		else{
			if(!flag)printf("Draw");
			else printf("Game has not completed");
		}
		printf("\n");
	}
    return 0;
}
