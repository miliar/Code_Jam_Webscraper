#include <iostream>
using namespace std;

int main (){
	int T, cont, k, a;
	
	cin >> T;
	
	for (int i=1; i<=T; i++){
		cont=0;
		cin >> a;
		for (int j=1; j<=a; j++){
			cin >> k;
			if (k!=j) cont++;
		}
		cout << "Case #" << i << ": " << cont << ".000000\n";
	}
	
	return 0;
}
