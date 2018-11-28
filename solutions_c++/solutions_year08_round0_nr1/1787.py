
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <map>
#include <list>

using namespace std;


int main(void) {
	ifstream arq("A-small-attempt2.in");
	ofstream saida("outputSmall2.in");

	const int LINE_LENGTH = 200;
	char linha[LINE_LENGTH];

	arq.getline(linha,LINE_LENGTH);
	int qtdCasos = atoi(linha);


	//std::cout << qtdCasos << std::endl;


	for(int caso=1; caso<=qtdCasos; caso++) {
		//Ler os engines
		arq.getline(linha,LINE_LENGTH);
		int qtdEng = atoi(linha);

		list<string> engines;
		for(int x=0; x<qtdEng; x++) {
			arq.getline(linha,LINE_LENGTH);
			string nome(linha);
			engines.push_back(nome);
		}

		int qtdSwitch = 0;

		//Ler as palavras
		arq.getline(linha,LINE_LENGTH);
		int qtdPalavras = atoi(linha);
		list<string> enginesT(engines);
		for(int x=0; x<qtdPalavras; x++) {
			arq.getline(linha,LINE_LENGTH);
			string nome(linha);

			enginesT.remove(linha);
			if( qtdSwitch == -1 && enginesT.size() == 1 ) {
				enginesT = engines;
				enginesT.remove(linha);
				qtdSwitch++;
			} else
			if( enginesT.size() == 0 ) {
				qtdSwitch++;
				enginesT = engines;
				enginesT.remove(linha);
			}
		}

		if( qtdSwitch == -1 )
			qtdSwitch = 0;

		cout << "Case #" << caso << ": " << qtdSwitch << endl;
		saida << "Case #" << caso << ": " << qtdSwitch << endl;

	}
}
