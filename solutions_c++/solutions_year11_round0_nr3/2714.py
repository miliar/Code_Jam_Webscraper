// codeforces.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
//#include <map>
#include <queue>
#include <vector>
#include <stdlib.h>
#include <set>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#define MAX 2100000000
#define eps 1e-9
using namespace std;
//freopen("C:\\Users\\tkdsheep\\Desktop\\out.txt","w",stdout);


int a[16];
int mark[16];
int n,ans;

void dfs(int x)
{
	if(x==n)
	{
		int i1,i2,t1,t2,i;
		i1=i2=0;
		for(i=0;i<n;i++)
		{
			if(mark[i]==1)
				i1++;
			else i2++;
		}
		if(i1==n||i2==n)
			return;
		i1=i2=t1=t2=0;
		for(i=0;i<n;i++)
		{
			if(mark[i]==1)
			{
				i1+=a[i];
				t1=t1^a[i];
			}
			else
			{
				i2+=a[i];
				t2=t2^a[i];
			}
		}
		if(t1==t2)
		{
			ans=max(max(i1,i2),ans);
		}
		return;
	}
	mark[x]=1;
	dfs(x+1);
	mark[x]=2;
	dfs(x+1);

}

int main()
{
	freopen("C:\\Users\\tkdsheep\\Desktop\\out.txt","w",stdout);
	int repeat,i;
	int cases=1;
	cin>>repeat;
	while(repeat--)
	{
		cout<<"Case #"<<cases++<<": ";
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		ans=-1;
		dfs(0);
		if(ans==-1)
			cout<<"NO"<<endl;
		else cout<<ans<<endl;

	}
}