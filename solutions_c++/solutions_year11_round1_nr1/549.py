#include <iostream>

using namespace std;

void main(){

	int t;
	cin >> t;

	for (int i = 0; i < t; i++){
		long long N;
		int pd, pg;

		cin >> N;
		cin >> pd;
		cin >> pg;

		if (pg == 100){
			if (pd == 100){
				cout << "Case #" << i+1 << ": Possible";
				if (i != t){
					cout << endl;
				}
			}
			else {
				cout << "Case #" << i+1 << ": Broken";
				if (i != t){
					cout << endl;
				}
			}
			continue;
		}
		
		if (pg == 0){
			if (pd == 0){
				cout << "Case #" << i+1 << ": Possible";
				if (i != t){
					cout << endl;
				}
			}
			else {
				cout << "Case #" << i+1 << ": Broken";
				if (i != t){
					cout << endl;
				}
			}
			continue;
		}
	
		for (int x = 1; x <= pd; x ++){
			if ( ((x*100) % pd)  == 0 ){
				long long n = (x*100) / pd;
				if (n <= N){
					cout << "Case #" << i+1 << ": Possible";
					if (i != t){
						cout << endl;
					}
				}
				else {
					cout << "Case #" << i+1 << ": Broken";
					if (i != t){
						cout << endl;
					}
				}
				break;
			}
		}
	}
}