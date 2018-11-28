#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#define INF 1000000007
#define EPS 0.000000001
using namespace std;

int T,i,j,k;
char s[11][11];

int f(int x,int y,int k,int p)
{
	int a[256];
	memset(a,0,sizeof(a));
	for(int i=0;i<4;i++)
		a[s[x+i*k][y+i*p]]++;
	if(a['X']==4 || (a['X']==3 && a['T']==1))
		return 2;
	if(a['O']==4 || (a['O']==3 && a['T']==1))
		return 3;
	if(a['.']>0)
		return 1;
	return 0;
}

int main()
{
//	freopen("1.in","r",stdin);
//	freopen("1.out","w",stdout);
	scanf("%d\n",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		for(i=0;i<4;i++)
			scanf("%s\n",s[i]);
		scanf("\n");
		k = max(f(0,0,1,1),f(3,0,-1,1));
		for(i=0;i<4;i++)
			k = max(k,max(f(i,0,0,1),f(0,i,1,0)));
		if(k==0)
			printf ("Draw\n"); else
		if(k==1)
			printf("Game has not completed\n"); else
		if(k==2)
			printf("X won\n"); else
		if(k==3)
			printf("O won\n"); 
	}
	return 0;
}