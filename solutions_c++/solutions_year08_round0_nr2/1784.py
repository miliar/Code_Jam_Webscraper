
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <map>
#include <list>
#include <vector>

using namespace std;


int main(void) {
	ifstream arq("B-large.in");
	ofstream saida("outputBlarge.in");

	string linha;

	arq >> linha;
	int qtdCasos = atoi(linha.c_str());

	for(int caso=1; caso<=qtdCasos; caso++) {
		arq >> linha;
		int tempoVirada = atoi(linha.c_str());
		cout << "Tempo Virada:" << tempoVirada << endl;

		arq >> linha;
		int qtdTrem1 = atoi(linha.c_str());
		cout << "Qtd TremA: " << qtdTrem1 << endl;

		arq >> linha;
		int qtdTrem2 = atoi(linha.c_str());
		cout << "Qtd TremB: " << qtdTrem2 << endl;

		//Ler os tempos do trem A-B
		vector<int> saidaA;
		vector<int> chegadaA;
		for(int x=0; x<qtdTrem1; x++) {
			arq>>linha;
			int tempo = 0;
			string hora1(linha.substr(0,2));
			string minuto1(linha.substr(3,2));

			tempo = atoi(hora1.c_str()) * 60 + atoi(minuto1.c_str());

			saidaA.push_back(tempo);
			cout << tempo << endl;

			arq>>linha;
			string hora2(linha.substr(0,2));
			string minuto2(linha.substr(3,2));
			tempo = atoi(hora2.c_str()) * 60 + atoi(minuto2.c_str()) + tempoVirada;

			chegadaA.push_back(tempo);
			cout << tempo << endl;
		}
		sort(saidaA.begin(), saidaA.end());
		sort(chegadaA.begin(), chegadaA.end());

		//Ler os tempos do trem B-A
		vector<int> saidaB;
		vector<int> chegadaB;
		for(int x=0; x<qtdTrem2; x++) {
			arq>>linha;
			int tempo = 0;
			string hora1(linha.substr(0,2));
			string minuto1(linha.substr(3,2));

			tempo = atoi(hora1.c_str()) * 60 + atoi(minuto1.c_str());

			saidaB.push_back(tempo);
			cout << tempo << endl;

			arq>>linha;
			string hora2(linha.substr(0,2));
			string minuto2(linha.substr(3,2));
			tempo = atoi(hora2.c_str()) * 60 + atoi(minuto2.c_str()) + tempoVirada;

			chegadaB.push_back(tempo);
			cout << tempo << endl;
		}
		sort(saidaB.begin(), saidaB.end());
		sort(chegadaB.begin(), chegadaB.end());


		for(unsigned int x=0; x<chegadaA.size(); x++) {
			vector<int>::iterator it = saidaB.begin();
			for(; it<saidaB.end() && *it<chegadaA[x]; it++);
			if( it<saidaB.end() )
				saidaB.erase(it);
		}

		for(unsigned int x=0; x<chegadaB.size(); x++) {
			vector<int>::iterator it = saidaA.begin();
			for(; it<saidaA.end() && *it<chegadaB[x]; it++);
			if( it<saidaA.end() )
				saidaA.erase(it);
		}

		cout << "Case #" << caso << ": " << saidaA.size() << " " << saidaB.size() << endl;
		saida << "Case #" << caso << ": " << saidaA.size() << " " << saidaB.size() << endl;

	}
}

