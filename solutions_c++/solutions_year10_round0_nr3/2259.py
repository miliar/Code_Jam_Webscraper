#include <iostream>
using namespace std;
#define For_ij(mi, mj) for(int i = 0, j = 0; i < (mi); i+=(j=(j+1)%(mj))==0)
#define For_i(m) for(int i = 0; i < (m); ++i)

int main(){
	unsigned T;
	cin >> T;
	for( unsigned t = 1; t <= T; ++t ){
		unsigned R, k, N;
		cin >> R >> k >> N;
		unsigned q[N];
		For_i(N) cin >> q[i];
		
		unsigned long long euros = 0;
		
		unsigned b = 0, e = 0;
		while (R--){
			unsigned ride = q[b];
			++b %= N;
			if (ride > k) break;
			
			while( b != e && ride + q[b] <= k ) ride += q[b], ++b %= N;
			e = b;
			euros += ride;
		}
		cout << "Case #" << t << ": " << euros << endl;
	}
}
