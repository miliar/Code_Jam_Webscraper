#include <iostream>
#include <vector>
#include <string>

using namespace std;

string resultado;

void introducir( char elemento, vector<string> &comb, vector<string> &opos){
	
	unsigned int i = 0;
	bool encontrado = false;
	while (i < comb.size() && !encontrado) {
		
		if ( (comb[i][0] == resultado[resultado.length()-1] && comb[i][1] == elemento) 
			|| (comb[i][1] == resultado[resultado.length()-1] && comb[i][0] == elemento)  ) {

			resultado.resize(resultado.length()-1);
			//cout << "combinacion " << comb[i][0] << "+" << comb[i][1] << "=" << comb[i][2]; 
			introducir(comb[i][2], comb, opos);
			encontrado = true;
		}
		i++;
	}
	if (!encontrado){
		unsigned int j = 0;
		while( j < resultado.length() && !encontrado) {
			i = 0;
			while (i < opos.size() && !encontrado) {
				
				if ( (opos[i].at(0) == resultado[j] && opos[i].at(1) == elemento) 
					|| (opos[i].at(1) == resultado[j] && opos[i].at(0) == elemento)  ) {
					
					resultado.resize(0);
					encontrado = true;
				}
				i++;
			}
			j++;
		}
		if (!encontrado) {
			resultado.push_back(elemento);
		}
			
	}

}
		 
int main(){
	int T;
	cin >> T;
	for (int j = 1; j<=T; j++) {
		
		int C, D, N;
		resultado.resize(0);
		
		cin >> C;
		
		vector<string> comb(C);
		for (int i = 0 ; i < C; i++) {
			char aux;
			
			for (int k =0; k<3; k++) {
				cin >> aux;
				comb[i] += aux;
			}
		}
		
		cin >> D;
		vector<string> opos(D);
		
		for (int i=0; i<D; i++) {
			char aux;
			
			for (int k =0; k<2; k++) {
				cin >> aux;
				opos[i] += aux;
			}
		}
		
		cin >> N;
		for (int i =0; i < N; i++) {
			char aux;
			cin >> aux;
			introducir(aux, comb, opos);
			
		}
		
		cout << "Case #" << j <<": [";
		if (resultado.length() > 0) {
			cout << resultado[0];
		}
		for (unsigned int i=1; i < resultado.length(); i++) {
			cout << ", " << resultado[i];
		}
		cout << "]" << endl;
		
	}
}
