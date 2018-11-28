#include <iostream>
using namespace std;



int main(){
	int caseNum;
	int R, k, N;
	cin >> caseNum;
	for(int i = 0; i < caseNum; i++){
		cin >> R;
		cin >> k;
		cin >> N;
		int *g = (int *)malloc(sizeof(int) * N);
		int start = 0;
		int total = 0;
		for(int i = 0; i < N; i++){
			cin >> g[i];
			total += g[i];
		}
		if(total < k){
			cout << "Case #" << i+1 << ": " << total * R << endl;
			continue;
		}
		
		total = 0;
		for(int i = 0; i < R; i++){
			int currentVolume = k;
			while(1){
				if(currentVolume - g[start] >= 0){
					total += g[start];
					currentVolume -= g[start];
					start = (start + 1) % N;
				}
				else
					break;
			}
		}
		cout << "Case #" << i+1 << ": " << total << endl;
	}
	return 0;
}

