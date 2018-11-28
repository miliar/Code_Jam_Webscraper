/*
 * main.cpp
 *
 *  Created on: 2013-4-9
 *      Author: whd
 */
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#define pb push_back
#define mp make_pair
#define x first
#define y second
using namespace std;

typedef long long big;
const double eps=1e-9,PI=acos(-1.0);
int sgn(double x)
{
	if(fabs(x)<eps)return 0;
	return x>0?1:-1;
}
struct P
{
	double x,y;
	P(){}
	P(double _x,double _y):x(_x),y(_y){}
};
P operator+(const P &a,const P &b)
{
	return P(a.x+b.x,a.y+b.y);
}
P operator-(const P &a,const P &b)
{
	return P(a.x-b.x,a.y-b.y);
}
P operator*(const P &a,double d)
{
	return P(a.x*d,a.y*d);
}
double det(const P &a,const P &b)
{
	return a.x*b.y-a.y*b.x;
}
double det(const P &s,const P &a,const P &b)
{
	return det(a-s,b-s);
}
double dot(const P &a,const P &b)
{
	return a.x*b.x+a.y*b.y;
}
bool ckjoint(const P &a,const P &b,const P &c,const P &d)
{
	return sgn(det(a,b,c))*sgn(det(a,b,d))<0&&
			sgn(det(c,d,a))*sgn(det(c,d,b))<0;
}
P joint(const P &a,const P &b,const P &c,const P &d)
{
	static double u,v;
	u=det(a,b,c);
	v=det(a,b,d);
	return P((v*c.x-u*d.x)/(v-u),(v*c.y-u*d.y)/(v-u));
}
char str[5][5];
void check()
{
	int i,j,k=0;
	for(i=0;i<4;i++)
	{
		k=0;
		for(j=0;j<4;j++)
			k+=(str[i][j]=='X'||str[i][j]=='T');
		if(k==4)
		{
			puts("X won");
			return ;
		}
		k=0;
		for(j=0;j<4;j++)
			k+=(str[i][j]=='O'||str[i][j]=='T');
		if(k==4)
		{
			puts("O won");
			return ;
		}
	}
	for(i=0;i<4;i++)
		{
			k=0;
			for(j=0;j<4;j++)
				k+=(str[j][i]=='X'||str[j][i]=='T');
			if(k==4)
			{
				puts("X won");
				return ;
			}
			k=0;
			for(j=0;j<4;j++)
				k+=(str[j][i]=='O'||str[j][i]=='T');
			if(k==4)
			{
				puts("O won");
				return ;
			}
		}
	k=0;
	for(i=0;i<4;i++)
		k+=(str[i][i]=='X'||str[i][i]=='T');
	if(k==4)
	{
		puts("X won");
		return ;
	}
	k=0;
		for(i=0;i<4;i++)
			k+=(str[i][i]=='O'||str[i][i]=='T');
		if(k==4)
		{
			puts("O won");
			return ;
		}
	k=0;
	for(i=0;i<4;i++)
		k+=(str[i][3-i]=='X'||str[i][3-i]=='T');
	if(k==4)
	{
		puts("X won");
		return ;
	}
	k=0;
		for(i=0;i<4;i++)
			k+=(str[i][3-i]=='O'||str[i][3-i]=='T');
		if(k==4)
		{
			puts("O won");
			return ;
		}
		k=0;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			k+=(str[i][j]=='.');
	if(k)
	{
		puts("Game has not completed");
		return ;
	}
	puts("Draw");
}
int main()
{
	int i,cas,cass,j;
	freopen("a.out","w",stdout);
	scanf("%d",&cas);
	for(cass=1;cass<=cas;cass++)
	{
		for(i=0;i<4;i++)
			scanf("%s",str[i]);
		printf("Case #%d: ",cass);
		check();
	}
}

