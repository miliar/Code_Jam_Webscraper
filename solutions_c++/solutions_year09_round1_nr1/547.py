#include "stdafx.h"
#include <string>
#include <cmath>
#include <queue>
#include <algorithm>
#include <iostream>
#define PI 3.14159265358979323846264338327950288
#define _clr(a,b) memset(a,b,sizeof(a))
template<class T> T _abs(T a)
{ if(a<0) return -a;return a;}
template<class T> void Get_Min(T& a,T b)
{ if(a>b) a=b;}
template<class T> void Get_Max(T& a,T b)
{ if(a<b) a=b;}
using namespace std;
bool used[100000];
bool Cal(int t,int base)
{
	int m=t;
	int result=t;
	int d;
	while(!used[m])
	{
		used[m]=true;
		result=0;
		while(m>0)
		{
			d=m%base;
			result+=d*d;
			m=m/base;
		}
		if(result==1) return true;
		m=result;
	}
	return false;
}
int base[10];
int main()
{
	freopen("e:\\1.in","r",stdin);
	//freopen("e:\\1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int n=0;
		char temp;
		while(1)
		{
			if(scanf("%d",&base[n])==EOF)
			{
				n--;
				break;
			}
			scanf("%c",&temp);
			if(temp!=' ') break;
			n++;
		}
		
		for(int i=2;;i++)
		{
			int j=0;
			for(;j<=n;j++)
			{
				_clr(used,0);
				if(!Cal(i,base[j])) break;
			}
			if(j==n+1)
			{
				printf("Case #%d: %d\n",t,i);
				break;
			}
		}
	}
	return 0;
}
