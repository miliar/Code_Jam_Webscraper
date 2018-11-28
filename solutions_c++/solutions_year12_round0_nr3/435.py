#include <iostream>
#include <algorithm>
#include<functional>
#include <string>
#include <stdio.h>
#include <set>
using namespace std;
char s1[20];
int a,b;
set<int> col;
//int arr[100];
//int vis[2000000];
int f(int st,int len)
{
	col.clear();
	for(int i=0;i<len;++i)
		s1[i+len]=s1[i];
	for(int i=1;i<len;++i)
	{
		int s=0;
		for(int j=i;j<i+len;++j)
			s=s*10+(s1[j]-'0');
		if(s>st&&s<=b)
		{
			//vis[]
			col.insert(s);
		}
	}
	return col.size();
}
int main()
{
	//freopen("D:\\Visual Studio 2008\\google code jam\\C-large.in", "r", stdin ) ;

	//freopen("D:\\Visual Studio 2008\\google code jam\\C-large.out", "w", stdout ) ;


	int t;
	scanf("%d ",&t);
	for(int k=1;k<=t;++k)
	{
		int ans=0;
		cin>>a>>b;
		for(int i=a;i<=b;++i)
		{
			sprintf(s1,"%d",i);
			int len=strlen(s1);
			ans+=f(i,len);
		}
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}