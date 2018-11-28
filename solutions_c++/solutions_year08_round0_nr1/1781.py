#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
	int ncases,cont = 0;
	cin >> ncases;
	while (ncases != 0){
		cont++;
		int s;
		cin >> s;
		string qualquer;
		getline(cin,qualquer);
		vector<string> engines;
		vector<string> queries;
		engines.clear();
		queries.clear();		
		for (int i = 0 ; i < s ; i++){
			string nome;
			getline(cin,nome);
			//cout << nome << endl;
			engines.push_back(nome);			
		}
		int nqueries;
		cin >> nqueries;
		getline(cin,qualquer);
		for (int i = 0 ; i < nqueries; i++){
			string querie;
			getline(cin, querie);
			//cout << querie << endl;
			queries.push_back(querie);
		}		
		
		/*
		cout << "*****************Engines - " << s << endl;
		for (int i = 0 ; i < engines.size(); i++)
			cout << engines[i] << endl;
		cout << "*****************Queries - " << nqueries << endl;
		for (int i = 0 ; i < queries.size(); i++)
			cout << queries[i] << endl;
		*/
		vector<int> oc(engines.size());
		for (int i = 0; i < queries.size(); i++){
			for(int k = 0 ; k < engines.size(); k++){
				if (queries[i] == engines[k]){
					oc[k]++;
				}
			}
		}
		int solucao = -1;
		for (int i = 0 ; i < oc.size(); i++)
			if (oc[i] == 0){
				solucao = 0;
				break;
			}
		if (solucao != 0){		
			vector< vector<int> > positions;
			positions.clear();
			positions.resize(engines.size());
			for (int i = 0 ; i < positions.size(); i++){
				positions[i].clear();
			}
			
			// armazena as posições
			for (int i = 0; i < queries.size(); i++){
				for(int k = 0 ; k < engines.size(); k++){
					if (queries[i] == engines[k]){
						positions[k].push_back(i);
					}
				}
			}
		
			// acha o maior
			int maior = -1;
			int posmaior = -1;
			for (int i = 0; i < positions.size(); i++){
				if (positions[i][0] > maior){
					maior = positions[i][0];
					posmaior = i;
				}					
			}
			for (int i = 0; i < positions.size(); i++){
				int j = 0;
				while (positions[i].size() > 0){					
					if (positions[i][j] < maior)
						positions[i].erase(positions[i].begin()+j);
					else break;
				}
			}
			
			if (posmaior == -1)
				cout << "ERRO!" << endl;
			else {
				solucao = 0;
				bool terminou = false;
				while (!terminou){
					solucao++;
					/*					
					cout << "maior = " << maior  << endl;
					for (int i = 0; i < positions.size(); i++){
						cout << i << " > ";
						for (int k = 0; k < positions[i].size(); k++){
							cout << positions[i][k] << " ";
						}
						cout << endl;
					}
					*/
					// acha novo maior
					for (int i = 0; i < positions.size(); i++){
						if (positions[i].size() == 0){
							terminou = true;
							break;
						}							
						if (positions[i][0] > maior){
							maior = positions[i][0];
							posmaior = i;
						}					
					}
					// apaga os menores
					for (int i = 0; i < positions.size(); i++){
						int j = 0;
						while (positions[i].size() > 0){					
							if (positions[i][j] < maior)
								positions[i].erase(positions[i].begin()+j);
							else break;
						}
					}
				}
			}
		}			
		cout << "Case #" << cont << ": " << solucao << endl;
		ncases--;
	}
}
