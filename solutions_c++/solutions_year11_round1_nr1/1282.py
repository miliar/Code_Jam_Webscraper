#include <iostream>
using namespace std;

int main(void){
	int T,N, Pd, Pg;
	cin >> T;
	for(int i = 1; i <= T; ++i){
		cout << "Case #" << i << ": ";
		cin >> N >> Pd >> Pg;
		if(Pg == 0 and Pd != 0){
			 cout << "Broken" << endl;
			 continue;
		}
		if(Pg == 100 and Pd != 100){
			cout << "Broken" << endl;
			continue;
		}
		bool possible = false;
		for(int j = 1; j <= N; ++j){
			if((j * 100 * Pd)%10000 == 0){
				cout << "Possible" << endl;
				possible = true;
				break;
			}
		}
		if(!possible){
			cout << "Broken" << endl;
		}
	} 
}
