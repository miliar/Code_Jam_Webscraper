// program.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#pragma warning(disable:4786)
#include <stdafx.h>
// END CUT HERE
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <numeric>
using namespace std;

int m,n;
string s[20];
int a[20][2000];

bool canput(int r,int v)
{
	int b[20];

	for(int i=0;i<n;i++) b[i]=(v>>i)&1;
	for(int i=0;i<n-1;i++) if(b[i]==1&&b[i+1]==1) return false;
	for(int i=0;i<n;i++) if(b[i]==1&&s[r][i]=='x') return false;
	return true;
}

int calcnum(int v)
{
	int ans=0;
	for(int i=0;i<n;i++) ans+=(v>>i)&1;
	return ans;
}

bool isgood(int v1,int v2)
{
	int bb[20],cc[20];

	for(int i=0;i<n;i++) bb[i]=(v1>>i)&1;
	for(int i=0;i<n;i++) cc[i]=(v2>>i)&1;
	for(int i=0;i<n;i++)
	{
		if(bb[i]==1)
		{
			if(i-1>=0&&i-1<n&&cc[i-1]==1) return false;
			if(i+1>=0&&i+1<n&&cc[i+1]==1) return false;
		}
	}
	return true;
}

void process(int num)
{
	cin>>m>>n;
	for(int i=0;i<m;i++) cin>>s[m-1-i];
	memset(a,0,sizeof(a));

	for(int i=0;i<(1<<n);i++)
		if(canput(0,i))
			a[0][i]=calcnum(i);
	for(int i=1;i<m;i++)
	{
		for(int j=0;j<(1<<n);j++)
			if(canput(i,j))
			{
				for(int k=0;k<(1<<n);k++) if(isgood(k,j))
				{
					int now=a[i-1][k]+calcnum(j);
					if(now>a[i][j]) a[i][j]=now;
				}
			}
	}

	int ans=0;
	for(int i=0;i<(1<<n);i++) if(a[m-1][i]>ans) ans=a[m-1][i];
	cout<<"Case #"<<num<<": "<<ans<<endl;
}

int main(void)
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++) process(i);
	return 0;
}