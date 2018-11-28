#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;


#define INFIN 1000000000

int test_num,n,V;

struct point{
	int value;
	int change;
} arr[10100];
int f[10100];


void out(int res)
{
	if(res==INFIN)
		printf("Case #%d: IMPOSSIBLE\n",test_num);
	else
		printf("Case #%d: %d\n",test_num,res);
}


void inp()
{
	scanf("%d%d",&n,&V);
	for(int i=1; i<=(n-1)/2; i++)
		scanf("%d%d",&arr[i].value,&arr[i].change);
	for(int i=1; i<=(n+1)/2; i++)
	{
		scanf("%d",&arr[i+(n-1)/2].value);
		arr[i+(n-1)/2].change=INFIN;
	}
}


int calc(int v)
{
	if(arr[v].change==INFIN)
		f[v]=arr[v].value;
	else
	{
		if(arr[v].value==1)
			f[v]=calc(2*v)&calc(2*v+1);
		else
			f[v]=calc(2*v)|calc(2*v+1);
	}
	return f[v];
}

int tree(int l,int r,int sign,int value, int eps)
{
	int res;
	if(sign==0)		
	{
		if((l|r)==value)
			return eps;
		else
			return INFIN;
	}
	else
	{
		if((l&r)==value)
			return eps;
		else
			return INFIN;
	}
}


int rec(int v, int value)
{
	if(f[v]==value)
		return 0;
	if(arr[v].change==INFIN)
		return INFIN;
	int l0 = rec(2*v,0);
	int l1 = rec(2*v,1);
	int r0 = rec(2*v+1,0);
	int r1 = rec(2*v+1,1);
	int eps = 0;
	if(arr[v].value==1)
		eps=1;

	int res = INFIN;
	if(arr[v].change==1 || arr[v].value==0)
	{
		res = min( res, tree(0,0,0,value,l0+r0+eps) );
		res = min( res, tree(0,1,0,value,l0+r1+eps) );
		res = min( res, tree(1,0,0,value,l1+r0+eps) );
		res = min( res, tree(1,1,0,value,l1+r1+eps) );
	}
	eps = 0;
	if(arr[v].value==0)
		eps=1;
	if(arr[v].change==1 || arr[v].value==1)
	{
		res = min( res, tree(0,0,1,value,l0+r0+eps) );
		res = min( res, tree(0,1,1,value,l0+r1+eps) );
		res = min( res, tree(1,0,1,value,l1+r0+eps) );
		res = min( res, tree(1,1,1,value,l1+r1+eps) );
	}
	return res;
}



void run()
{
	calc(1);
	int res = rec(1,V);
	out(res);
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test_count;
	scanf("%d",&test_count);
	for(test_num=1; test_num<=test_count; test_num++)
	{
		inp();
		run();
	}
	return 0;
}