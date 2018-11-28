#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <vector>
#include <stdlib.h>
#include <cmath>

using namespace std;
 
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)

int main(){
	//get inputs

	int ncase = 0;
	cin >> ncase;


	for(int icase = 0; icase<ncase; icase++){
		int n;
		cin >> n;
		unsigned long can[n];

		for(int i = 0; i< n; i++){
			cin >> can[i];
		}

		unsigned long xorsum = 0;
		unsigned long sum = 0;
		unsigned long min = can[0];
		for(int i = 0; i<n; i++){
			xorsum = xorsum ^ can[i];
			sum += can[i];
			if(can[i] < min)
				min = can[i];
		}



		cout << "Case #" << icase+1 << ": "; 
		if(xorsum == 0){
			cout << sum - min;
		}
		else{
			cout << "NO";
		}		
		cout << endl;
	}


	return 0;
}
