#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <map>
#include <queue>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

int f[200][300];
int h,t,q[300];
bool use[300];
int D,I,M,n;
int a[200];

int main(){
//	freopen("b.in","r",stdin);
	int test=0;
	scanf("%d", &test);
	for ( int T=1; T<=test; ++T ){
		scanf("%d %d %d %d", &D,&I,&M,&n);
		int MM=0;
		for ( int i=0; i<n; ++i ){
			scanf("%d", a+i); MM=max(MM,a[i]);
		}
		int tt=0;
		memset(f,0,sizeof(f));
		for ( int i=1; i<=n; ++i )
			for ( int j=0; j<=MM; ++j ) f[i][j]=1000000;
		for ( int i=0; i<n; ++i ){
			for ( int j=0; j<=MM; ++j ){
				for ( int k=max(0,j-M); k<=min(j+M,MM); ++k )
					f[i+1][k]=min(f[i+1][k],f[i][j]+abs(a[i]-k));
				f[i+1][j]=min(f[i+1][j],f[i][j]+D);
			}
			h=t=0;
			for ( int j=0; j<=MM; ++j ){
				++t; q[t]=j; use[j]=true;
			}
			while ( h!=t ){
				++h; if ( h==300 ) h=1;
				for ( int j=max(0,q[h]-M); j<=min(q[h]+M,MM); ++j )
					if ( f[i+1][q[h]]+I<f[i+1][j] ){
						f[i+1][j]=f[i+1][q[h]]+I;
						if ( ! use[j] ){
							use[j]=true; ++t; if ( t==300 ) t=1; q[t]=j;
						}
					}
				use[q[h]]=false;
			}
		}
		int ans=1000000;
		for ( int i=0; i<=MM; ++i ) ans=min(ans,f[n][i]);
		printf("Case #%d: %d\n", T,ans);
	}
}
