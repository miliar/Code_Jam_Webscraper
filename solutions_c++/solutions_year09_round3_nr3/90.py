#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <functional>
#include <cmath>
using namespace std;

int a[200];
int d[200];
int F[200][200];
bool Fb[200][200];

int f(int l,int r)
{
	if(r-l<2)
		return 0;
	if(!Fb[l][r])
	{
		F[l][r]=INT_MAX;
		for(int i=l+1;i<r;i++)
			F[l][r]=min(F[l][r],f(l,i)+f(i,r)+a[r]-a[l]-2);
		Fb[l][r]=true;
	}
	return F[l][r];
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	//
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		memset(Fb,0,sizeof(Fb));
		int n,k;
		scanf("%d%d",&n,&k);
		a[0]=0;
		for(int i=1;i<=k;i++)
			scanf("%d",a+i);
		sort(a,a+k);
		a[k+1]=n+1;
		//
		printf("Case #%d: %d\n",t,f(0,k+1));
	}
	//
	return 0;
}