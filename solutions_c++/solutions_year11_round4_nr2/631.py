#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

const double zero=1e-6;

char ma[1010][1010];
double ma1[1010][1010],ma2[1010][1010],ma3[1010][1010];
int n,m,d;

bool ok( int l ){
	for ( int i=l; i<=n; ++i )
		for ( int j=l; j<=m; ++j ){
			double sumx=ma2[i][j]-ma2[i-l][j]-ma2[i][j-l]+ma2[i-l][j-l]-ma[i][j]*i-ma[i-l+1][j]*(i-l+1)-ma[i][j-l+1]*i-ma[i-l+1][j-l+1]*(i-l+1);
			double sumy=ma3[i][j]-ma3[i-l][j]-ma3[i][j-l]+ma3[i-l][j-l]-ma[i][j]*j-ma[i-l+1][j]*j-ma[i][j-l+1]*(j-l+1)-ma[i-l+1][j-l+1]*(j-l+1);
			double sumw=ma1[i][j]-ma1[i-l][j]-ma1[i][j-l]+ma1[i-l][j-l]-ma[i][j]-ma[i-l+1][j]-ma[i][j-l+1]-ma[i-l+1][j-l+1];
			/*if (l==5 && i==6 && j==6 )
				printf("%.4lf %.4lf %.4lf\n",sumx,sumy,sumw);*/
			if ( fabs(sumx*2-(i+i-l+1)*sumw)<zero && fabs(sumy*2-(j+j-l+1)*sumw)<zero ) return true;
		}
	return false;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int times=0;
	scanf("%d",&times);
	for (int z=1; z<=times; ++z )
	{
		printf("Case #%d: ",z);
		scanf("%d%d%d",&n,&m,&d);
		for (int i=1; i<=n; ++i )
		for ( int j=1; j<=m; ++j )
		{
			char x;
			scanf(" %c",&x);
			ma[i][j]=x-'0';
			ma1[i][j]=ma[i][j]+ma1[i-1][j]+ma1[i][j-1]-ma1[i-1][j-1];
			ma2[i][j]=ma[i][j]*i+ma2[i-1][j]+ma2[i][j-1]-ma2[i-1][j-1];
			ma3[i][j]=ma[i][j]*j+ma3[i-1][j]+ma3[i][j-1]-ma3[i-1][j-1];
		}
		int ans=0;
		for (int a=min(n,m);a>2;--a)
		if (ok(a))
		{
			ans=a;
			break;
		}
		if (ans) printf("%d\n", ans);else printf("IMPOSSIBLE\n");
	}
}
