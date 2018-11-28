#include <iostream>
#include <vector>
#include <fstream>
#include <stdlib.h>
#include <set>
#include <limits.h>
#include <iomanip>

using namespace std;

int ganados[100];
int jugados[100];
char resultados[100][100];
double owp[100];
double oowp[100];
int numberTeams;

double calculateOwp(int team1){
	double sumowp = 0;
	for (int j = 0; j < numberTeams; j++){
		if (resultados[team1][j] != '.'){//Es oponente
			sumowp += double((ganados[j] - (resultados[j][team1] - '0'))) / (double)((jugados[j] - 1));

		}
	}
	return (sumowp / jugados[team1]);
}

int main(int argc, char *argv[]){
	if (argc != 2){
		cerr << "Error: " << argv[0] << " file" << endl;
		exit(-1);
	}
	cout << setprecision(10);
	ifstream file(argv[1]);
	if (!file.is_open()){
		cerr << "Error: file " << argv[0] << " could not be opened" << endl;
	}
	int T;
	file >> T;
	for (int test = 0; test < T; test++){
		file >> numberTeams;
		for (int row = 0; row < numberTeams; row++){
			for (int column = 0; column < numberTeams; column++){
				file >> resultados[row][column];
			}
		}
		//Calculamos WP
		for (int i = 0; i < numberTeams; i++){
			jugados[i] = 0;
			ganados[i] = 0;
			for (int j = 0; j < numberTeams; j++){
				if (resultados[i][j] == '1'){
					jugados[i]++;
					ganados[i]++;
				} else if (resultados[i][j] == '0'){
					jugados[i]++;
				}
			}
		}
		//Calculamos owp 
		for (int i = 0; i < numberTeams; i++){
			owp[i] = calculateOwp(i);	
		}
		//Calculamos oowp
		for (int i = 0; i < numberTeams; i++){
			double oowpSum = 0;
			for (int j = 0; j < numberTeams; j++){
				if (resultados[i][j] != '.'){
					oowpSum += owp[j];
				}
			}
			oowp[i] = oowpSum / jugados[i];
		}
		cout << "Case #" << (test+1) << ": " << endl;
		for (int i = 0; i < numberTeams; i++){
			double rpi = 0.25 * (((double)ganados[i]) / jugados[i]) + 0.50 * owp[i] + 0.25 * oowp[i];
			cout << rpi << endl;
		}
	}
}
