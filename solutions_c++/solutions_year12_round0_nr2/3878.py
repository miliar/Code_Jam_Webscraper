#include <iostream>
#include <string>

using namespace std;

int main(){
	int ncases,ngog,nsp,nth,temp;
	int output = 0;
	cin >> ncases;
	for(int k = 0; k < ncases; k++){
		cin >> ngog >> nsp >> nth;
		for(int j = 0; j < ngog; j++){
			cin >> temp;
			if(temp > 3*(nth-1)) output++;
			else if(((temp == 3*(nth-1) && nth > 1)|| temp == 3*(nth-1) - 1) && nsp > 0) {nsp--;output++;}
		}
		cout << "Case #" << k+1 << ": " << output << endl; 
		output = 0;
	}
	return 0;
}		
	 
