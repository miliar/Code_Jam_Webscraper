#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int potencia( int a, int b){
	int res = a;
	if (b == 0){
		return 1;
		}
	for(int i=2;i <= b; i++){
		res *= a;
		}
	return res;	
	}

int main(){
	ifstream entrada("A-large.in"); 
	ofstream salida("A-large.out"); 
	
	int T;
	entrada >> T;
	int caso = 1;
	
	while (T > 0) {
		int N;
		int k;
		int aux;
		entrada >> N;
		entrada >> k;
		salida << "Case #" << caso << ":" ;
		aux = potencia(2, N) ;

		//la prende aux
		if(k == (aux-1) || ((k+1)%aux == 0 )){
			salida << " ON" <<endl; 
			} else {
				salida << " OFF" <<endl;
			}
		caso++;
		T--;
	}
	return 0;
}
