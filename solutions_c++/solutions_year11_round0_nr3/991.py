#include<iostream>

using namespace std;

int main(){
	int test, n, soma, xbits, menor, aux;
	
	cin >> test;
	for(int t=1;t<=test;t++){
		xbits = 0;
		soma = 0;
		menor = 9999999;
		
		cin >> n;
		for(int i=0;i<n;i++){
			cin >> aux;
			xbits = xbits ^ aux;
			soma+=aux;
			
			if(menor > aux) menor = aux;
		}
		
		cout << "Case #" << t << ": ";
		
		if(xbits != 0) cout << "NO\n";
		else{
			cout << (soma-menor) << "\n";
		}
	}
	return 0;
}
