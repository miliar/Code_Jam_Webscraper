#include <iostream>
#include <vector>
using namespace std;

int main(){
	int T,N,K,i,j;
	cin >> T;
	vector<bool> power_s, state_s;
	for(i=1;i<=T;i++){
		cin >> N >> K;
		power_s = vector<bool>(N,false);
		state_s = vector<bool>(N,false);
		power_s.at(0) = true; state_s.at(0) = false;
		while(K--){
			for(j=0;j<N;j++){
			/*	if(power_s[j-1]==true && state_s[j-1]==true) {
					//if(state_s[j])  { state_s[j] = false; }
					//else { state_s[j] = true; }
					state_s[j] = !state_s[j];
					power_s[j] = true;
				}
				else {
					power_s[j] = false;
				}
			*/
				//state_s[j+1] = state_s[j] ^ power_s[j];

 state_s[j] = state_s[j] ^ power_s[j]; 	
			}

				for(j=0;j<N-1;j++)			power_s[j+1] = state_s[j] & power_s[j];
			//state_s[0] = !state_s[0];
		}
		cout << "Case #" << i << ": ";
		if(power_s[N-1] && state_s[N-1]) cout << "ON"; else cout << "OFF";
		cout << endl; 
	}

	return 0;
}
