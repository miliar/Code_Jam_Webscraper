#include <iostream>

using namespace std;

int main(){
	int t,n;
	int sum,sumr;
	int min;
	
	int c;
	
	cin >> t;
	for(int i = 0; i < t; i++){
		cin >> n;
		
		sum = 0;
		sumr = 0;
		min = 10000000;
		for(int j = 0; j < n; j++){
			cin >> c;
			sum ^= c;
			sumr += c;
			if(min > c) min = c;
		}
		
		if(sum != 0) cout << "Case #" << (i+1) << ": NO" << endl;
		else cout << "Case #" << (i+1) << ": " << (sumr-min) << endl;
	}
	
	return 0;
}