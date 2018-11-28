#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;

#define REP(i,a) for(int i=0; i<(int)(a); ++i)

int main() {
	int caseN, T, N[2], h1, m1, h2, m2;

	cin >> caseN;
	REP(n, caseN) {
		cin >> T >> N[0] >> N[1];	
		priority_queue<int> out[2], in[2];
		
		REP(i, 2) while (N[i]--) {
			scanf("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
			out[i].push(-60*h1-m1);
			in[1-i].push(-60*h2-m2-T);
		}	
		
		int cnt[2] = {0, 0};
		REP(i, 2) {
			for (cnt[i] = 0; !out[i].empty(); out[i].pop()) 
				if (in[i].empty() || in[i].top() < out[i].top())
					++cnt[i]; else in[i].pop();
		}	
					
		cout << "Case #" << n+1 << ": " << cnt[0] << " " << cnt[1] << endl;
	}
}
