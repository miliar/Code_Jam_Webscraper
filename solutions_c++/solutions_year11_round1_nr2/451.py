#include <iostream>
#include <vector>
#include <fstream>
#include <stdlib.h>
#include <set>
#include <limits.h>

using namespace std;


int getPoints(vector<string> dictionary, string &word, string &list){
	int points = 0;
	int acertados = 0;
	for (int i = 0; i < dictionary.size(); i++){
		if (dictionary[i].size() != word.size()){
			dictionary[i] = "";
		}
	}
	for (int i = 0; i < list.size(); i++){
		char letra = list[i];
		bool elige = false;
		for (int j = 0; j < dictionary.size(); j++){//Esta esa letra?
			for (int k = 0; k < dictionary[j].size(); k++){
				if (dictionary[j][k] == letra){
					elige = true;
					break;
				}
				if (elige){
					break;
				}
			}
		}
		if (elige){
			bool acerto = false;
			for (int j = 0; j < word.size(); j++){
				if (word[j] == letra){
					acerto = true;
					acertados++;
					//Eliminar
					for (int k = 0; k < dictionary.size(); k++){
						if ((dictionary[k].size() != 0) && (dictionary[k][j] != letra)){
							dictionary[k] = "";
						}
					}
				} else {
					//Eliminar
					for (int k = 0; k < dictionary.size(); k++){
						if ((dictionary[k].size() != 0) && (dictionary[k][j] == letra)){
							dictionary[k] = "";
						}
					}
				}
			}
			if (!acerto){
				points++;
			}
			if (acertados == word.size()){
				return points;
			}
		}
	}
	cerr << "Error interno" << endl;
}

int main(int argc, char *argv[]){
	if (argc != 2){
		cerr << "Error: " << argv[0] << " file" << endl;
		exit(-1);
	}
	ifstream file(argv[1]);
	if (!file.is_open()){
		cerr << "Error: file " << argv[0] << " could not be opened" << endl;
	}
	int T;
	file >> T;
	for (int i = 0; i < T; i++){
		int N, M;
		file >> N >> M;
		vector<string> dictionary;
		for (int j = 0; j < N; j++){
			string word;
			file >> word;
			dictionary.push_back(word);
		}
		vector<string> lists;
		for (int j = 0; j < M; j++){
			string list;
			file >> list;
			lists.push_back(list);
		}

		vector<int> solutionIndexes;
		for (int j = 0; j < lists.size(); j++){
			int bestPoints = -1;
			int bestIndex = -1;
			//cerr << "Lista: " << j << lists[j] << endl;
			for (int k = 0; k < dictionary.size(); k++){
				int puntos = getPoints(dictionary, dictionary[k], lists[j]);
				//cerr << "Palabra " << dictionary[k] << ": " << puntos << endl;
				if (puntos > bestPoints){
					bestPoints = puntos;
					bestIndex = k;
				}
			}
			solutionIndexes.push_back(bestIndex);
		}
		cout << "Case #" << (i+1) << ": ";
		for (int j = 0; j < solutionIndexes.size()-1; j++){
			cout << dictionary[solutionIndexes[j]] << " ";
		}
		cout << dictionary[solutionIndexes[solutionIndexes.size()-1]] << endl;
	}
}
