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

int n,p;
int f[20][2000][20];
int a[2000];

int main(){
	//freopen("b1.in","r",stdin);
	int test=0;
	scanf("%d", &test);
	for ( int T=1; T<=test; ++T ){
		scanf("%d", &p); n=p;
		p=(1<<p);
		for ( int i=0; i<p; ++i )
			scanf("%d", &a[i]);
		memset(f,-1,sizeof(f));
		for ( int j=0; j<p/2; ++j ){
			int x;
			scanf("%d", &x);
			int t=min(a[j*2],a[j*2+1]);
			f[0][j][t]=x;
			for ( int k=0; k<t; ++k ) f[0][j][k]=0;
		}
		p=p/2;
		for ( int i=1; i<n; ++i ){
			for ( int j=0; j<p/2; ++j ){
				int x;
				scanf("%d", &x);
				for ( int k=0; k<n; ++k ){
					int t1=f[i-1][j*2][k];
					int t2=f[i-1][j*2+1][k];
					int t3=f[i-1][j*2][k+1];
					int t4=f[i-1][j*2+1][k+1];
					int m1=-1;
					int m2=-1;
					if ( t1!=-1 && t2!=-1 ) m1=t1+t2+x;
					if ( t3!=-1 && t4!=-1 ) m2=t3+t4;
					if ( m1!=-1 && m2!=-1 )
						f[i][j][k]=min(m1,m2);
					else
						if ( m1!=-1 )
							f[i][j][k]=m1;
						else
							if ( m2!=-1 )
								f[i][j][k]=m2;
				}
			}
			p=p/2;
		}
		int ans=1000000000;
		for ( int i=0; i<n; ++i )
			if ( f[n-1][0][i]!=-1 )
				ans=min(ans,f[n-1][0][i]);
		printf("Case #%d: %d\n", T, ans);
	}
}
