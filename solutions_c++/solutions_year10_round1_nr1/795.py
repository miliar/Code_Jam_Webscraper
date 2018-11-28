#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdio>
#include<iomanip>
#include<map>
#include<set>
#include<vector>
#include<list>
#include<deque>
#include<cstdlib>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

const int N=55;

int n,gk;
int mtx[N][N];
char ss[N][N];

void myin()
{
	int i;
	cin>>n>>gk;
	for(i=1;i<=n;i++)
		cin>>(ss[i]+1);
}

void pre_set()
{
	int i,j,k;
	memset(mtx,0,sizeof(mtx));
	for(i=1;i<=n;i++)
	{
		for(j=n,k=n;j>=1;j--)
		{
			if(ss[i][j]!='.')
				mtx[i][k--]=ss[i][j]=='R'?1:2;
		}
	}
}

bool check(int col,int bgnx,int bgny)
{
	int i;
	for(i=1;i<=gk&&bgny+i-1<=n;i++)
		if(mtx[bgnx][bgny+i-1]!=col)
			break;
	if(i>gk)
		return true;

	for(i=1;i<=gk&&bgnx+i-1<=n;i++)
		if(mtx[bgnx+i-1][bgny]!=col)
			break;
	if(i>gk)
		return true;

	for(i=1;i<=gk&&bgnx+i-1<=n&&bgny+i-1<=n;i++)
		if(mtx[bgnx+i-1][bgny+i-1]!=col)
			break;
	if(i>gk)
		return true;

	for(i=1;i<=gk&&bgnx+i-1<=n&&bgny-i+1>=1;i++)
		if(mtx[bgnx+i-1][bgny-i+1]!=col)
			break;
	if(i>gk)
		return true;

	return false;
}

void work()
{
	int i,j;
	bool lab1=false,lab2=false;
	pre_set();
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
			if(check(1,i,j))
				lab1=true;
			if(check(2,i,j))
				lab2=true;
		}
	}
	if(!lab1&&!lab2)
		cout<<"Neither"<<endl;
	else if(lab1&&lab2)
		cout<<"Both"<<endl;
	else if(lab1)
		cout<<"Red"<<endl;
	else
		cout<<"Blue"<<endl;
}

int main()
{
	freopen("t1.in","r",stdin);
	freopen("t1.out","w",stdout);
	int i,tests;
	cin>>tests;
	for(i=1;i<=tests;i++)
	{
		myin();
		cout<<"Case #"<<i<<": ";
		work();
	}
return 0;
}