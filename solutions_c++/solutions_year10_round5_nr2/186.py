#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

long long L;
long long d[100100];
int B[110];
bool ok;
int n;

int main(){
	//freopen("b.in","r",stdin);
	int test=0;
	scanf("%d", &test);
	for ( int T=1; T<=test; ++T ){
		ok=false;
		cin>>L>>n;
		int M=0;
		for ( int i=0; i<n; ++i ){
			scanf("%d", &B[i]);
			M=max(M,B[i]);
		}
		for ( int i=0; i<M; ++i )
			d[i]=-1;
		long long ans=L/M;
		d[0]=0;
		ok=false;
		while ( ! ok ){
			ok=true;
			for ( int i=0; i<M; ++i )
				if ( d[i]>=0 )
				for ( int j=0; j<n; ++j ){
					int t=i+B[j], tt=t%M;
					if ( t>=M ){
						if ( d[i]<d[tt] || d[tt]==-1 ){
							d[tt]=d[i]; ok=false;
						}
					} else
						if ( d[i]+1<d[tt] || d[tt]==-1){
							d[tt]=d[i]+1; ok=false;
						}
				}
		}
		printf("Case #%d: ", T);
		if ( d[L%M]==-1 )
			printf("IMPOSSIBLE\n");
		else
			printf("%lld\n", ans+d[L%M]);
	}
}
