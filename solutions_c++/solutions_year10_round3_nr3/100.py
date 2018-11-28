#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>
#define mp make_pair
#define pb push_back                     
#define int64 long long
#define ld long double  
#define setval(a,v) memset(a,v,sizeof(a))
using namespace std;

int ans[32][32];

int a[32][32];
int szkol[32];
int n,m;  

void use(int lx,int rx,int ly,int ry){
	for (int i=0;i<rx;i++)
		for (int j=0;j<ry;j++){
			int tmp=lx-i;
			tmp=max(tmp,ly-j);
			tmp=max(tmp,0);
			ans[i][j]=min(ans[i][j],tmp);
		}
}

void cnt(int i,int j){
	ans[i][j]=1;
	int mind=min(n-i,m-j);
	for (int di=0;di<mind;di++)
		for (int dj=0;dj<mind;dj++)
			if ((a[i][j]^a[i+di][j+dj])!=((di+dj)&1))
				mind=max(di,dj);
	ans[i][j]=mind;		
}

void solve(int tnum){
	scanf("%d %d",&n,&m);
	for (int i=0;i<n;i++)
		for (int j=0;j<m/4;j++){	
			char c;
			scanf(" %c ",&c);
			int tmp=0;
			if ('0'<=c && c<='9')
				tmp=c-'0';
			else
				tmp=c-'A'+10;
			for (int k=3;k>=0;k--)
			{
				a[i][j*4+k]=tmp&1;
				tmp>>=1;
			}
		}

	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
			cnt(i,j);
	
	int tans=0;
	int kol=32;
	for (;kol;--kol){
		szkol[kol]=0;
		bool q=false;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				if (ans[i][j]==kol)
				{
					use(i,i+kol,j,j+kol);
					szkol[kol]++;
					q=true;
				}
		if (q)
			++tans;
	}
	printf("Case #%d: %d\n",tnum,tans);
	for (int i=32;i>=0;--i)
		if (szkol[i]!=0)
			printf("%d %d\n",i,szkol[i]);
}

int main()
{
  //freopen("input.txt","r",stdin);
//  freopen("output.txt","w",stdout);
  int t;
  cin>>t;
  for (int i=1;i<=t;i++)
  	solve(i);
  
  return 0;
}