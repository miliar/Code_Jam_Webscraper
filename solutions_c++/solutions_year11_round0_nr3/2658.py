#include <iostream>

using namespace std;

int main(){
	int c;
	cin >> c;
	
	
	for(int T=1;T<=c;T++){
		int n;
		cin >> n;
		if(n>1){
			int xsum=0;
			int sum=0;
			int input;
			int small=1000001;
			for(int i=0;i<n;i++){
				cin >> input;
				xsum = xsum ^ input;
				sum = sum + input;
				if(input < small){
					small = input;
				}
			}
			if(xsum == 0){
				cout << "Case #" << T << ": " << (sum-small) << endl;
			}
			else{
				cout << "Case #" << T << ": NO" << endl;
			}
		}
	}
}

// 
// Input 
//  	
// Output 
//  
// 2
// 5
// 1 2 3 4 5
// 3
// 3 5 6
// Case #1: NO
// Case #2: 11
