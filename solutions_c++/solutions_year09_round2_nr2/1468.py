#include<iostream>
#include<string>
#include<vector>
#include <algorithm>
using namespace std;

int main(){
	int size, numero, actual, nuevoNumero, multiplicador, numeroOriginal;
	int count = 0;
	vector<int> conjunto, cjto;
	char tmp[1000];
	gets(tmp); size=atoi(tmp);
	cerr << size << endl;
	while(size--){
		gets(tmp);
		numero = atoi(tmp);
		numeroOriginal = numero;
		conjunto.clear();
		cjto.clear();
		while(numero>9){
			actual = numero % 10;
			conjunto.push_back(actual);
			numero = numero / 10;
		}
		if (numero>0)
			conjunto.push_back(numero);
		for (int h=conjunto.size()-1;h>=0;h--)
			cjto.push_back(conjunto[h]);
		
		next_permutation( cjto.begin(), cjto.end() );
		while (cjto[0]==0)
			next_permutation( cjto.begin(), cjto.end() );
		nuevoNumero = 0;
		multiplicador = 1;
		for (int h=cjto.size()-1;h>=0;h--){
			nuevoNumero += cjto[h]*multiplicador;
			multiplicador *= 10;
		}
		//cerr << "comparo "<< nuevoNumero << " " << numero << endl;
		if (nuevoNumero<=numeroOriginal){
			conjunto.clear();
			conjunto.push_back(cjto[0]);
			conjunto.push_back(0);
			for (int h=1;h<cjto.size();h++)
				conjunto.push_back(cjto[h]);
		
			nuevoNumero = 0;
			multiplicador = 1;
			for (int h=conjunto.size()-1;h>=0;h--){
				nuevoNumero += conjunto[h]*multiplicador;
				multiplicador *= 10;
			}
			//for (int h=0;h<conjunto.size();h++)
			//	cerr << conjunto[h] << " + ";
			
		}
		printf("Case #%d: %d\n",++count, nuevoNumero);
	}

  return 0;
}
