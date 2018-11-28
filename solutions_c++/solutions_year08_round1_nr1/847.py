
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <map>
#include <list>

using namespace std;


int main(void) {
	ifstream arq("A-small-attempt0.in");
	ofstream saida("outputSmallA0.in");

	const int LINE_LENGTH = 200;
	char linha[LINE_LENGTH];

	// Primeira linha => Qtd de casos
	arq >> linha;
	int qtdCasos = atoi(linha);


	for(int caso=1; caso<=qtdCasos; caso++) {
		//Ler a qtd de Numeros
		arq >> linha;
		int qtdNum = atoi(linha);

		list<int> v1;
		for(int x=0; x<qtdNum; x++) {
			string numero;
			arq >> numero;
			int i = atoi(numero.c_str());

			v1.push_back(i);
		}

		list<int> v2;
		for(int x=0; x<qtdNum; x++) {
			string numero;
			arq >> numero;
			int i = atoi(numero.c_str());

			v2.push_back(i);
		}

		v1.sort();
		v2.sort();
		v2.reverse();

		int soma = 0;
		for(int x=0; x<qtdNum; x++) {
			int i1 = v1.front();
			int i2 = v2.front();

			soma += i1 * i2;

			v1.pop_front();
			v2.pop_front();
		}


		cout << "Case #" << caso << ": " << soma << endl;
		saida << "Case #" << caso << ": " << soma << endl;

	}
}
