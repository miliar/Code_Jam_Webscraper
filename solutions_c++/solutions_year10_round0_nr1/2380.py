#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int T,N,K,caso;
	cin >> T;
	caso = 0;
	int state[11];

	for (caso = 1; caso <= T; caso++){
		cin >> N >> K;

		memset(state,0,sizeof state);

		int llega = 0;
		while (K--){
			for (int i=0; i <= llega; i++){
				if (state[i]){
					state[i] = 0;
				} else {
					state[i] = 1;
				}
			}

			llega = N;
			for (int i=0;i<N;i++){
				if (state[i] == 0){
					llega = i;
					break;
				}
			}

			//cout << "Llega hasta el " << llega << endl;
		}

		if (llega == N){
			cout << "Case #" << caso << ": " << "ON" << endl;
		} else {
			cout << "Case #" << caso << ": " << "OFF"  << endl;
		}
	}
	
	return 0;
}