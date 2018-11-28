#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(int argc, char* argv[]){
	
	unsigned long long n, k, t, power, i, res;

	cin >> t;
	
	for(i = 0; i < t; i++){
		cin >> n >> k;

		power = (unsigned long long)pow(2,n) - 1;
		res = k & power;

		if(res == power){
			cout << "Case #" << i+1 << ": ON"<< endl;
		} else {
			cout << "Case #" << i+1 << ": OFF"<< endl;		
		}

	}
	return 0;
}

