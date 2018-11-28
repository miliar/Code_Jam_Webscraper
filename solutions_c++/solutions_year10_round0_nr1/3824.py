#include <iostream>
#include <math.h>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		unsigned long int n, k;
		cin >> n;
		cin >> k;
		unsigned long int p = pow(2, n);
		if((k + 1) % p == 0)
			cout << "Case #" << i << ": " << "ON" << endl;
		else
			cout << "Case #" << i << ": " << "OFF" << endl;
	}
	return 0;
}
