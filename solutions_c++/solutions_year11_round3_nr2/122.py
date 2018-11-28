#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)
#define FOR(i,a,b) for (int i=a,_n=b; i<=_n; i++)

int nTC,L,N,C,a[10000],D[1000010];
long long t;

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		printf("Case #%d: ",TC);
		scanf("%d %lld %d %d",&L,&t,&N,&C);
		REP(i,C) scanf("%d",&a[i]);
		
		for (int k=0; ; k++){
			REP(i,C){
				int j = k*C+i;
				if (j>N) goto finish;
				D[j] = a[i];
			}
		}
		finish:;

		int at = 0;
		long long ct = 0;
		while (at < N){
			if (ct <= t){
				long long wait = t - ct;
				long long need = D[at] * 2LL;
//				fprintf(stderr,"> at = %d, ct = %lld, need = %lld, wait = %lld, D = %d\n", at, ct, need, wait, D[at]);
				if (wait >= need){ // low speed
					at++;
					ct += need;
//					fprintf(stderr,"at = %d, ct = %lld, need = %lld\n", at, ct, need);
				} else {
					vector<int> Ds;
					Ds.push_back((need - wait)/2);
//					fprintf(stderr,"rem = %lld, \n",(need - wait)/2);
					ct += wait;
					for (at++; at<N; at++) Ds.push_back(D[at]);
					sort(Ds.rbegin(),Ds.rend());
					REP(i,Ds.size()){
						if (L > 0){
							ct += Ds[i];
							L--;
						} else {
							ct += Ds[i]*2LL;
						}
					}
					break;
				}
			} else {
				fprintf(stderr,"at = %d, %lld, %lld HERE\n",at,ct,t);
				break;
			}
		}
		printf("%lld\n",ct);
	}
}


