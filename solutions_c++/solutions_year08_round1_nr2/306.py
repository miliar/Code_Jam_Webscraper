#include<iostream>
#include<algorithm>	
#include<map>
#include<vector>
#include<cmath>
#include<queue>
#include<string>

#define INF ((1 << 30) - 1)

using namespace std;

int main() {
	int T, C, N, M, nbits, minNbits, minComb, combc, X, Y;
	long long sum;
	
	bool satisfied[2001][2001][2];
	bool hasSatisfied[2001];
	
	cin >> C;
	
	for(int ci = 0; ci < C; ci++) {
		cin >> N >> M;
		
		memset(satisfied, 0, sizeof(satisfied));
		
		for(int mi = 0; mi < M; mi++) {
			cin >> T;
			for(int ti = 0; ti < T; ti++) {
				cin >> X >> Y;
				satisfied[mi][X-1][Y] = true;
			}
		}
		
		minComb = -1;
		minNbits = 2001;
		
		for(int comb = 0; comb < (1 << N); comb++) {
			combc = comb;
			
			nbits = 0;
			
			while(combc) {
				combc &= (combc >> 1);
				nbits++;
			}
			
			bool satisfiesAll = true;
			
			memset(hasSatisfied, 0, sizeof(hasSatisfied));
			
			for(int i = 0; i < N; i++) {
				for(int mi = 0; mi < M; mi++) {
					hasSatisfied[mi] |= satisfied[mi][i][(comb >> i) & 1];
				}
			}
			
			for(int mi = 0; mi < M; mi++) {
				satisfiesAll &= hasSatisfied[mi];
			}
			
			if(satisfiesAll && minNbits > nbits) {
				minNbits = nbits;
				minComb = comb;
			}
		}
		
		if(minComb == -1) {
			cout << "Case #" << (ci+1) << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << (ci+1) << ":";
			
			for(int i = 0; i < N; i++) {
				cout << " " << ((minComb >> i) & 1);
			}
			
			cout << endl;
		}
	}
	
	return 0;
}
