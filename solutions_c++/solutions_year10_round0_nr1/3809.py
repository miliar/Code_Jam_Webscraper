// codejam1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "stdio.h"
#include "iostream"

using namespace std;


int check(int n,int k)
{
	int s=1;
	for(int i=1;i<=n;i++)
	{
		s=s*2;
	}
	if((k%s)==(s-1)) return 1;
	else return 0;
}


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n,k;
		cin>>n>>k;
		int j=check(n,k);
		if(j) cout<<"Case #"<<i<<": ON"<<endl;
		else cout<<"Case #"<<i<<": OFF"<<endl;
	}
	return 0;
}
