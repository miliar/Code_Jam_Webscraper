#include <iostream>
#include <math.h>

using namespace std;

int main(){
	unsigned int t, n, k;
	cin >> t;
	for (unsigned int i=1; i<=t; i++){
		cin >> n >> k;
		unsigned int d = (1U << n ) - 1;

		cout << "Case #" << i << ": " <<
					(  (k & d) == d ? "ON" : "OFF" ) << endl;
	}
}
