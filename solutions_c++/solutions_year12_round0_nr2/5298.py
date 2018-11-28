#include <iostream>

using namespace std;

int main(){
	int T;
	cin >> T;
	
	for (int iT = 0; iT < T; iT++){
	
		int N, S, P;
		
		cin >> N >> S >> P;
		int mp = 0;
		int s = 0;
		for (int iN = 0; iN < N; iN++){
			int t;
			cin >> t;
			
			if (t >= 3 * P - 2){
				mp++;
				continue;
			}
			if (t >= 3 * P - 4 && s < S && P > 1){
				mp++;
				s++;
				continue;
			}
			
		}
		cout << "Case #" << iT + 1<<": " << mp << endl;
	
	
	
	}
	return 0;
	
}

