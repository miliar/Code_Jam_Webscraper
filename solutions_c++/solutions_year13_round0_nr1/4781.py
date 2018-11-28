#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

char a[4][5];
char* os[]={"O won","X won","Draw","Game has not completed"};
int sr[20];
int sc[20];
int dr[20];
int dc[20];
int p;

inline bool equal(char x,char y)
{
	return (x!='.'&&y!='.')&&(x==y||x=='T'||y=='T');
}

void add(int r,int c,int ar,int ac)
{
	p++;
	sr[p]=r;
	sc[p]=c;
	dr[p]=ar;
	dc[p]=ac;
}

void init()
{
	p=-1;
	for(int i=0;i<4;i++)
	{
		add(0,i,1,0);
		add(i,0,0,1);
	}
	add(0,0,1,1);
	add(3,0,-1,1);
}

int check()
{
	for(int i=0;i<=p;i++)
	{
		char x=a[sr[i]][sc[i]];
		if(x=='.') continue;
		bool flag=true;
		for(int j=1;j<4;j++)
		{
			int r=sr[i]+j*dr[i];
			int c=sc[i]+j*dc[i];
			if(equal(a[r][c],x)==false)
			{
				flag=false;
				break;
			}
			if(x=='T')
				x=a[r][c];
		}
		if(flag==true)
		{
	//		printf("true %d %d %d %d %d",i,sr[i],sc[i],dr[i],dc[i]);
			if(x=='O') return 0;
			else return 1;
		}
	}

	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(a[i][j]=='.')
				return 3;
	
	return 2;
}

int main()
{
	int csnum;
	//freopen("A-large.in","r",stdin);
	//freopen("out","w",stdout);
	scanf("%d",&csnum);
	init();
	for(int cs=1;cs<=csnum;cs++)
	{
		for(int i=0;i<4;i++)
			scanf("%s",a[i]);
		int ans=check();
		printf("Case #%d: %s\n",cs,os[ans]);
	}
	return 0;
}