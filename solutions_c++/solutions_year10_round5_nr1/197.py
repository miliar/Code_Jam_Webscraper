#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int D, n;
int a[1000];
int maxx, lim;
bool isss[1100000];
int ss[1100000], tot;
int ans;

void prepare(){
	for ( int i=2; i<=1000000; ++i )
		if ( ! isss[i] ){
			ss[tot++]=i;
			for ( int j=i; j<=1000000/i; ++j )
				isss[i*j]=true;
		}
}

int solve( int x ){
	int ret=-1;
	if ( n<2 ) return -1;
	for ( int i=0; i<x; ++i ){
		int b=((a[1]-a[0]*i)%x+x)%x;
		bool ok=true;
		for ( int j=0; j<n-1; ++j )
			if ((a[j]*i+b)%x!=a[j+1]){
				ok=false; break;
			}
		if ( ok ){
			int t=(a[n-1]*i+b)%x;
			if ( ret==-1 )
				ret=(a[n-1]*i+b)%x;
			else
				if ( ret!=t )
					return -1;
		}
	}
	return ret;	
}

int main(){
//	freopen("a.in","r",stdin);
	prepare();
	int test=0;
	scanf("%d", &test);
	for ( int T=1; T<=test; ++T ){
		scanf("%d %d", &D, &n);
		lim=1;
		for ( int i=0; i<D; ++i )
			lim*=10;
		maxx=0;
		for ( int i=0; i<n; ++i ){
			scanf("%d", a+i);
			maxx=max(maxx,a[i]);
		}
		ans=-1;
		for ( int i=0; i<tot; ++i ){
			if ( ss[i]>lim ) break;			
			if ( ss[i]>maxx ){
				int t=solve(ss[i]);
				if ( t==-1 ) continue;
				if ( ans==-1 )
					ans=t;
				else 
					if ( ans!=t ){
						ans=-1; break;
					}
			}
		}
		printf("Case #%d: ", T);
		if ( ans==-1 )
			printf("I don't know.\n");
		else
			printf("%d\n", ans);
	}
}
