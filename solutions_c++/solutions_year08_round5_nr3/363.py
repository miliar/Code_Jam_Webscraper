#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	
	int Ntc;
	cin >> Ntc;
	
	for(int Ntci = 1; Ntci <= Ntc; ++Ntci) {
		cout << "Case #" << Ntci << ": ";

		int M, N;
		cin >> M >> N;
		vector<int> dp(1024, 0);
		for(int r = 0; r != M; ++r) {
			string seats;
			cin >> seats;
			vector<int> dp2(1024, 0);
			for(int i = 0; i != (1 << N); ++i) {
				dp2[i] = 0;
				int best = 0;
				for(int j = 0; j+1 < N; ++j)
					if((i & (1 << j)) && (i & (2 << j)))
						goto noway;
				for(int j = 0; j != N; ++j)
					if((i & (1 << j)) && seats[j] == 'x')
						goto noway;
				if(r > 0) {
					for(int k = 0; k != (1 << N); ++k) {
						if(N == 1) {
							best = max(best, dp[k]);
							goto noway2;
						}
						if((i & 1) && (k & 2))
							goto noway2;
						if((i & (1 << (N - 1))) && (k & (1 << (N - 2))))
							goto noway2;
						for(int j = 1; j+1 < N; ++j) {
							if((i & (1 << j)) && (k & (2 << j)))
								goto noway2;
							if((i & (1 << j)) && (k & (1 << (j - 1))))
								goto noway2;
						}
						best = max(best, dp[k]);
						noway2:;
					}
				}
				dp2[i] = best;
				for(int j = 0; j != N; ++j)
					if(i & (1 << j)) ++dp2[i];
				noway:;
			}
			
			dp.swap(dp2);
		}
		
		int best = 0;
		for(int i = 0; i != (1 << N); ++i) {
			best = max(best, dp[i]);
		}
		
		cout << best << endl;
	}
}
