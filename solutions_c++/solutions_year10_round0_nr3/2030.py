#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	ifstream entrada("C-large.in"); 
	ofstream salida("C-large.out"); 
	
	int T;
	entrada >> T;
	int caso = 1;
	
	while (T > 0) {
		salida << "Case #" << caso << ":" ;

		unsigned long long int R;
		entrada >> R;
		
		unsigned long long int K;
		unsigned long long int N;
		entrada >> K;
		
		entrada >> N;
		
		vector <unsigned long long int> grupos;
		unsigned long long int auxN = N;
		
		while (auxN > 0) {
			unsigned long long int grupoAux;
			entrada >> grupoAux;
			
			grupos.push_back(grupoAux);
			auxN--;
		}
		
		
		unsigned long long int suma = 0ULL;
		
		unsigned long long int auxPrimPosicion = 0;
		
		int cantIter;
		
		unsigned long long int auxSuma;
		
		unsigned long long int auxArraySuma[N];
		unsigned long long int auxArrayPosicion[N];
		for(auxN = 0; auxN < N ; auxN++){
				cantIter = 1;
				auxPrimPosicion = auxN;
				auxSuma = grupos[auxPrimPosicion];
				auxPrimPosicion ++;
				if(auxPrimPosicion == N){
					auxPrimPosicion = 0;
					}
				while(auxSuma+grupos[auxPrimPosicion] <= K && cantIter < N){
						auxSuma = auxSuma+grupos[auxPrimPosicion];
						auxPrimPosicion++;
						if(auxPrimPosicion == N){
							auxPrimPosicion = 0;
							}
						cantIter++;
					}
				auxArraySuma[auxN] = auxSuma;
				auxArrayPosicion[auxN] = auxPrimPosicion;
				
				
						
				}
				/*for(int i=0;i<N;i++){
					cout << auxArraySuma[i] << endl;
					}
				for(int i=0;i<N;i++){
					cout << auxArrayPosicion[i] << endl;
					}*/
		unsigned long long int actual =	0;
		while(R > 0){
			
			suma += auxArraySuma[actual];
			actual = auxArrayPosicion[actual];
			/*cout << endl;
			cout << suma << endl;*/
			R--;
		}
		salida << " "<< suma <<endl;
		caso++;
		T--;
	}
	return 0;
}
