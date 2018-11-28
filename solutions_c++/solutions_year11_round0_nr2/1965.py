//============================================================================
// Name        : GCJ.cpp
// Author      : yb
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
using namespace std;

int getid(char s)
{
	if(s=='Q')return 0;
	if(s=='W')return 1;
	if(s=='E')return 2;
	if(s=='R')return 3;
	if(s=='A')return 4;
	if(s=='S')return 5;
	if(s=='D')return 6;
	if(s=='F')return 7;
	return 8;
}
char s[105];
char unit[10][10];
int map[10][10];
int main()
{
	freopen("b.out","w",stdout);
	char temp[4],ans[105],cas=1;
	int n,m,l,txt,len,j;
	scanf("%d",&txt);
	while(txt--)
	{
		len=0;
		memset(map,0,sizeof(map));
		for(int i=0;i<9;i++)
			for(int j=0;j<9;j++)unit[i][j]='.';
		scanf("%d",&n);
		while(n--)
		{
			scanf(" %s",temp);
			unit[getid(temp[0])][getid(temp[1])]=temp[2];
			unit[getid(temp[1])][getid(temp[0])]=temp[2];
		}
		scanf("%d",&m);
		while(m--)
		{
			scanf(" %s",temp);
			map[getid(temp[0])][getid(temp[1])]=1;
			map[getid(temp[1])][getid(temp[0])]=1;
		}
		scanf("%d",&l);
		scanf(" %s",s);
		ans[++len]=s[0];
		for(int i=1;i<l;i++)
		{
			if(len&&unit[getid(s[i])][getid(ans[len])]!='.')
			{
				ans[len]=unit[getid(s[i])][getid(ans[len])];
			}
			else
			{
				for(j=1;j<=len;j++)
					if(map[getid(s[i])][getid(ans[j])])break;
				if(j>len){ans[++len]=s[i];}
				else len=0;
			}
		}
		printf("Case #%d: ",cas++);
		printf("[");
		for(int i=1;i<=len;i++)
		{
			if(i>1)printf(", ");
			printf("%c",ans[i]);
		}
		puts("]");
	}
	return 0;
}

