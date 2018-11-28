#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>

using namespace std;

int main(){
	int tcase;
	cin >> tcase;
	
	for(size_t casen = 0; casen < tcase; ++casen)
	{
		int N, E;
		cin >> N;
		vector < pair < int, int > > V(N);		
		for (int i = 0 ; i < N ; i++){
			cin >> V[i].first >> V[i].second;
		}
		cin >> E;
		
		sort(V.begin(), V.end());
		
		int d = V[0].first - 0;		
		int DP[V.size()];
		memset (DP, 0, sizeof(int) * V.size());
		DP[0] = d;
		for (int Ci = 0 ; Ci < V.size() ; Ci++){
			for(int i = V.size() - 1 ; i > Ci ; i--){
				if (V[Ci].first + DP[Ci] >= V[i].first){
					d = min(V[i].first - V[Ci].first, V[i].second);
					DP[i] = max(DP[i], d);
				}
			}
		}
		
		bool isPossible = false;
		
		for (int i = 0 ; i < V.size() ; i++){
			if (DP[i] + V[i].first >= E) isPossible = true;
		}

		
		cout << "Case #" << casen + 1 << ": ";
		if (isPossible) cout << "YES" << endl;
		else cout << "NO" << endl;
		
	}
	

	return 0;
}
