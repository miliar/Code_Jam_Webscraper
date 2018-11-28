#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

int main(){
	int T;
	cin >> T;
	for(int caseNum = 1; caseNum <= T; ++caseNum){
		int N, L, H;
		cin >> N >> L >> H;
		vector<ll> freqs(N);
		ll maxFreq = 0;
		for(int i = 0; i < N; ++i){ cin >> freqs[i]; }
		int answer = -1;
		for(int i = L; i <= H; ++i){
			bool possible = true;
			for(int j = 0; j < N; ++j){
				if(i % freqs[j] != 0 && freqs[j] % i != 0){
					possible = false;
					break;
				}
			}
			if(possible){
				answer = i;
				break;
			}
		}
		if(answer < 0){
			cout << "Case #" << caseNum << ": NO" << endl;
		}else{
			cout << "Case #" << caseNum << ": " << answer << endl;
		}
	}
	return 0;
}
