#include "stdafx.h"
  
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <list>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
#define forr(i,a,b) for (int i=a; i<=b; i++)
#define ford(i,a,b) for (int i=a; i>=b; i--)
#define mset(a,b) memset(a,b,sizeof(a))
#define sz(a) int( a.size() )
#define all(A) A.begin(),A.end()
#define sqr(q) q*q
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define X first
#define Y second

typedef long long i64;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef pair<int,int> PII;
typedef vector<string> VS;


int col[10000];
int a[120][120];
int ans[120][120];
int n,m;
int bk[10000];
int count1;

void hid(int i,int j, int cl)
{
	ans[i][j]=cl;
	int min=100000;
	if (i>0 && a[i-1][j]<min) min=a[i-1][j];
	if (j>0 && a[i][j-1]<min) min=a[i][j-1];
	if (i<n-1 && a[i+1][j]<min) min=a[i+1][j];
	if (j<m-1 && a[i][j+1]<min) min=a[i][j+1];

	if (min>=a[i][j])  { col[cl]=cl; return ;}
	
	if (i>0 && a[i-1][j]==min)
	{
		if (ans[i-1][j]) col[cl]=ans[i-1][j];
		else hid(i-1,j,cl);
		return ;
	}


	if (j>0 && a[i][j-1]==min)
	{
		if (ans[i][j-1]) col[cl]=ans[i][j-1];
		else hid(i,j-1,cl);
		return ;
	}

	if (i<n-1 && a[i+1][j]==min)
	{
		if (ans[i+1][j]) col[cl]=ans[i+1][j];
		else hid(i+1,j,cl);
		return ;
	}

	if (j<m-1 && a[i][j+1]==min)
	{
		if (ans[i][j+1]) col[cl]=ans[i][j+1];
		else hid(i,j+1,cl);
		return ;
	}
}


int cod(int cl)
{
	if (col[cl]!=cl) 
	{
		col[ cl ]=col[ col[cl] ];
		return cod(col[cl]);
	}

	if (!bk[cl]) {bk[cl]=count1+1; count1++; }

	return bk[cl]-1;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc;

	scanf("%d",&tc);
	

	rep(ti,tc)
	{
		mset(ans,0);
		mset(col,0);
		mset(bk,0);
		count1=0;
		scanf("%d %d",&n,&m);
		rep(i,n) rep(j,m) scanf("%d",&a[i][j]);
		int kil=1;
		rep(i,n) rep(j,m) if (!ans[i][j]) hid(i,j,kil++);
		printf("Case #%d:\n",ti+1);

		rep(i,n)
		{
			rep(j,m) printf("%c ",cod(ans[i][j])+'a');
			//rep(j,m) printf("%d ",ans[i][j]);

			printf("\n");
		}
		/*rep(i,kil+1) printf("%d ",i); printf("\n");
		rep(i,kil+1) printf("%d ",col[i]);
		printf("\n");*/

		



	}
	
	return 0;
}

