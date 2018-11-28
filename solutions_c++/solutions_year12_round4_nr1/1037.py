#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;
typedef long long i64;

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		cout << "Case #" << ts << ": ";
		int N;
		cin >> N;
		vector<i64> D(N+1);
		vector<i64> L(N+1);
		i64 TD;
		for(int i=0; i<N; i++) cin >> D[i] >> L[i];
		cin >> TD;
		D[N]=TD;
		L[N]=4000000000LL;
		vector<i64> bestd(N+1,4000000000LL);
		bestd[0]=0;
		for(int i=0; i<N+1; i++) {
			bestd[i] = max(bestd[i],D[i]-L[i]);
			i64 d1 = bestd[i];
			i64 d2 = bestd[i]+2*(D[i]-bestd[i]);
			//cout << i << " " << D[i] << " " << L[i] << " " << d1 << " " << d2 << endl;
			for(int j=i+1; j<N+1; j++) {
				if(D[j]>d2) break;
				bestd[j] = min(bestd[j], D[i]);
			}
		}
		cout << (bestd[N] < 4000000000LL ? "YES" : "NO") << endl;
	}
}
