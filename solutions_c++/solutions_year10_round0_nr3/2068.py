#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
#define cl(a,co) memset(a,co,sizeof a)
#define un(a) sort(ALL(a)),a.erase( unique(ALL(a)), a.end() )
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow;

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		
		int R, k, N;
		int t[2000];
		int next[2000];
		ll sum[3000];
		memset(sum,0,sizeof sum);

		scanf("%d%d%d",&R,&k,&N);

		fu(a,N){
			scanf("%d",&t[a]);
			sum[a] = t[a];
			if( a > 0 ) sum[a] += sum[a-1];
		}

		fu(a,2*N){
			sum[N+a] = sum[N+a-1] + t[a%N];
		}

		fu(a,N){
			int sum2=0;
			next[a]=-1;

			for(int b=0; sum2+t[(a+b)%N]<=k && b<N; b++, next[a]=(a+b)%N) sum2 += t[ (a+b)%N ];
		}

/*
		cerr << endl;
		cerr << "NEXT" << endl;
		fu(a,N) cerr << next[a] << " "; cerr << endl;
		cerr << "SUM" << endl;
		fu(a,3*N) cerr << sum[a] << " "; cerr << endl;
*/
		vector<ll> steps;
		//steps.pb(0);

		bool v[2000];
		memset(v,0,sizeof v);

		int gdzie = 0;
		ll suma=0;

		int last[1000];
		memset(last,0,sizeof last);
		int counter = 0;

		while( v[gdzie] == 0 ){
			if( next[gdzie]-1 >= gdzie ){
				suma += sum[ next[gdzie] + N - 1 ] - sum[gdzie + N] + t[gdzie];	
			} else {
				suma += sum[ next[gdzie] + 2*N - 1 ] - sum[gdzie + N] + t[gdzie];
			}
	//		cerr << "next[gdzie]: " << next[gdzie] << " gdzie: " << gdzie << " SUMA: " << suma << endl;
			steps.pb( suma );
			
			if( v[gdzie] == 1 ) break;	
			
			last[gdzie] = counter++;	
			v[gdzie] = 1;
			
			if( gdzie == -1 ){
				break;
			}
			gdzie = next[gdzie];
		}
/*
cerr << gdzie << " steps.sz: " << steps.sz << endl;
cerr << "STEPS" << endl;
fu(a,steps.sz) cerr << steps[a] << " "; cerr << endl;
*/
		if( gdzie == -1 ){
			if( R-1 < steps.sz ){
				printf("%lld\n", steps[ R-1 ]);
			} else {
				printf("%lld\n", steps[ steps.sz-1 ]);
			}
		} else {
			//R--;

//cerr << "R: " << R << " gdzie: " << gdzie << " last[gdzie]: " << last[gdzie] << endl;

			ll res = 0;
			if( R >= last[gdzie] ){
				R -= last[gdzie];

				if( last[gdzie] > 0 ){
					res += steps[ last[gdzie]-1 ];
					suma -= steps[ last[gdzie]-1 ];
				}
				
				int mod = steps.sz - last[gdzie];

				int next = R % mod + last[gdzie];

				res += R / mod * suma;

				if( R%mod > 0 ){
					R--;
					if( last[gdzie] > 0 ){
						res += steps[ last[gdzie] + R % mod ] - steps[ last[gdzie] - 1 ] ;
					} else {
						res += steps[ R % mod + last[gdzie] ];
					}

				}

//cerr << "res: " << res << " mod: " << mod << " | " << R << " " << suma<< endl;	
				
				printf("%lld\n", res);
			}  else {
				printf("%lld\n", steps[ R ]);
					
			}

		}

	}

	return 0;
}
