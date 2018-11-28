#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

int n,p;
int m[1100];
int price[1100];
bool visit[1100];

void solve();
void init()
{
	cin>>p;
	n=1<<p;
	for(int i=0;i<n;i++)
	{
		cin>>m[i];
	}
	int t;
	for(int i=0;i<1100;i++)
		visit[i]=0;
	for(int i=0,k=n/2;i<p;i++,k/=2)
	{
		for(int j=0;j<k;j++)
			cin>>t;
	}
	solve();
}

bool check()
{
	for(int i=0;i<n;i++)
		if(m[i]!=3000)
			return true;
	return false;
}
void solve()
{
	int sum=0;
	
	for(int i=0;i<n;i++)
	{
		int j=m[i];
		for(;j<p;j++){
			unsigned base=i>>1;
		base>>=j;
		visit[base]=1;
		}
	}
	for(int i=0;i<1100;i++)
	{
		if(visit[i])
			sum++;
	}
	cout<<sum<<endl;
}
int main()
{
	freopen("out.txt","w",stdout);
	int cs;
	cin>>cs;
	for(int i=0;i<1100;i++)
		price[i]=1;
	for(int ii=1;ii<=cs;ii++)
	{
		cout<<"Case #"<<ii<<": ";
		init();
	}
	return 0;

}