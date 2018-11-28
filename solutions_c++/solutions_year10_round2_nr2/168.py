#include <cmath>
using namespace std;
#include <iostream>
#include <string>
#include <cstdio>
#include <bitset>
#include <map>

//By chyx111
#define DBG(a) cerr << #a << ": " << (a) << endl
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)

const int MAXN = 64;
int v[MAXN], x[MAXN];
bitset<MAXN> ok;

int main() {
	int ca;cin>>ca;
	Rep(ica,ca){
		int N, K, B, T;
		cin>>N>>K>>B>>T;
		Rep(i,N)scanf("%d", x+i);
		Rep(i,N)scanf("%d", v+i);

		long long cnt = 0;
		int passed = 0;
		ok.reset();
		for(int i = N-1; i>=0; --i){
			if( v[i] * T >= B - x[i] ){
				ok[i] = true;
				passed++;
				if( passed <= K ){
					cnt += N-1-i+1 - passed;
				}
			}
		}

		printf("Case #%d: ", ica+1);
		if( passed >= K ){
			printf("%lld\n", cnt);
		}else{
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}

