// includes + defines {{{
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>
#define REP(i, n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define FORD(i, a, b) for(int i = (int)(a); i >= (int)(b); --i)
#define FORE(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define SIZE(x) ((int)((x).size()))
#define DEBUG(x) { cout << #x << ": " << (x) << endl; }
#define SQR(x) ((x) * (x))
#define INF 1023456789
using namespace std;
// }}}

typedef long long LL;

int main(){
	int T;
	cin >> T;
	FOR(q, 1, T){
		int R, K, N;
		cin >> R >> K >> N;
		vector<int> G(N);
		REP(i, N)
			cin >> G[i];

		vector<int> E(N, 0), P(N, 0); // posun, ak zacneme i-tou skupinou
		REP(i, N){
			if(i > 0){
				E[i] = E[i - 1] - G[i - 1];
				P[i] = P[i - 1] - 1;
			}

			while(P[i] < N && E[i] + G[(i + P[i]) % N] <= K){
				E[i] += G[(i + P[i]) % N];
				++P[i];
			}
		}

		vector<int> C(N, -1);
		int w = 0, i = 0;
		LL res = 0;
		while(R > 0 && C[w] == -1){ // hladanie cyklu
			--R;
			res += E[w];
			C[w] = i++;
			w = (w + P[w]) % N;
		}

		if(R > 0){
			LL sum = 0;
			int nw = w;
			do{
				sum += E[nw];
				nw = (nw + P[nw]) % N;
			}while(nw != w);

			res += sum * (R / (i - C[w]));
			R %= i - C[w];
		}

		while(R--){ // nedokonceny cyklus
			res += E[w];
			w = (w + P[w]) % N;
		}

		cout << "Case #" << q << ": " << res << endl;
	}
}
