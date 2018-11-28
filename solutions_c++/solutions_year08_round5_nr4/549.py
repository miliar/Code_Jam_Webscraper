#include <cstdio>
#include <string>
#include <cstring>
#include <functional>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
using namespace std;
const int MAXN=10+10;
int ax[MAXN];
int ay[MAXN];
const int MOD=10007;
int px[]={1,2};
int py[]={2,1};
const int MAXM=100+10;
int a[MAXM][MAXM];
void solution(int num)
{
	printf("Case #%d: ",num);
		int n,m,r;
	scanf("%d %d %d",&n,&m,&r);
	int i;
	for(i=0;i<r;i++)
		scanf("%d %d",&ax[i],&ay[i]);
	int j,k;
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
		{
			if(i==1&&j==1) {a[i][j]=1;continue;}
			a[i][j]=0;
			for(k=0;k<r;k++)
				if(i==ax[k]&&j==ay[k]) break;
			if(k!=r) continue;
			if(i>1&&j>2) a[i][j]+=a[i-1][j-2];
			if(i>2&&j>1) a[i][j]+=a[i-2][j-1];
			a[i][j]%=MOD;
		}
	printf("%d",a[n][m]);
	printf("\n");
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d",&n);
	int i;
	for(i=0;i<n;i++)
		solution(i+1);
	return 0;
}
