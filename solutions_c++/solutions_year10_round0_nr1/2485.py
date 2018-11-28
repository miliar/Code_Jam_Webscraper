#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int i, j, cont, pot, n, k, t;
	cin >> t;
	for(j = 1; j<= t; j++){
		cin >> n >> k;
		pot = (int)pow(2.0, n);
		k = k%pot;
//		cout << k << endl;
		for(i = cont = 0; i < n; i++, k>>=1)
			if(k&1)
				cont++;
		if(cont == n)
			cout << "Case #"<< j<<": ON" << endl;
		else
			cout << "Case #"<< j<<": OFF" << endl;
	}
	return 0;
}
