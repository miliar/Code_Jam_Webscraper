#include<iostream>
#include <string.h>
#include <map>
#include <algorithm>
#include <vector>
#include <stdio.h>

using namespace std;

int work(int a,int p,int &s)
{
	// 先看a 是否能组成p
	int x,y,z;
	x = p;
	y = p-1;
	// 
	if(a - x - y >= y && x >= 0 && y >= 0) return 1; // 不需要使用s
	if(s <= 0) return 0;

	y = p-2;
	if(y < 0) return 0;
	if(a - x - y >= y) 
	{
		s --;
		return 1;
	}
	return 0;
	if(a - x - y == y-1 && x >= 0 && y >= 1)
	{
		s --;
		return 1;
	}
	y --;
	if(a - x - y == y && x >= 0 && y >= 0)
	{
		s --;
		return 1;
	}
	return 0;
}

int work2(int a,int p,int &s)
{
	if(a % 3 == 0)
	{
		int bas = a / 3;
		if(bas >= p) return 1;
		if(s > 0 && bas -1 >= 0 && bas + 1 >= p)
		{
			s --;
			return 1;
		}
	}
	else if(a % 3 == 1)
	{
		int bas = a / 3;
		if(bas + 1 >= p) return 1;
		if(s > 0 && bas + 1 >= p)
		{
			s --;
			return 1;
		}
	}
	else
	{
		int bas = a / 3;
		if(bas + 1 >= p) return 1;
		if(s > 0 && bas + 2 >= p)
		{
			s --;
			return 1;
		}
	}
	return 0;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t;
	int cas = 1;
	cin>>t;
	int a [110];
	while(t--)
	{
		int n,s,p;
		cin>>n>>s>>p;
		for(int i = 0 ; i < n; i ++)
			cin>>a[i];
		sort(a,a+n);
		int ans = 0;
		for(int i = n-1; i >= 0; i --)
		{
			ans = ans + work2(a[i],p,s);
		}
		cout<<"Case #"<<cas++<<": "<<ans<<endl;
//		Case #1: 3

	}
	return 0;
}