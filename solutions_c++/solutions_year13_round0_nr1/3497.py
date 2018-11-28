//============================================================================
// Name        : compete.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	char table[4][4];
	int num;
	int flag;
	int countrow[3];
	int countcol[3];
	int countdia[3];

	cin >> num;
	for(int tablenum=1;tablenum<=num;++tablenum){
		//initial
		flag = 0;
		for(int i=0;i<3;++i){
			countdia[i] = 0;
		}

		for(int j=0;j<4;++j)
			for(int k=0;k<4;++k)
				cin >> table[j][k];

		for(int j=0;j<4;++j){
			if(table[j][j]=='X'){
				countdia[0] += 1;
			}
			else if(table[j][j] == 'O'){
				countdia[1] += 1;
			}
			else if(table[j][j] == 'T'){
				countdia[2] += 1;
			}
		}

		if(countdia[0] == 4 || (countdia[0] == 3 && countdia[2] == 1)){
				cout << "Case #" << tablenum << ": X won" << endl;
				continue;
		}
		else if(countdia[1] == 4 || (countdia[1] == 3 && countdia[2] == 1)){
				cout << "Case #"<< tablenum << ": O won" << endl;
				continue;
		}

		for(int i=0;i<3;++i){
			countdia[i] = 0;
		}

		for(int j=0;j<4;++j){
				if(table[j][3-j]=='X'){
					countdia[0] += 1;
				}
				else if(table[j][3-j] == 'O'){
					countdia[1] += 1;
				}
				else if(table[j][3-j] == 'T'){
					countdia[2] += 1;
				}
		}

		if(countdia[0] == 4 || (countdia[0] == 3 && countdia[2] == 1)){
					cout << "Case #" << tablenum << ": X won" << endl;
					continue;
		}
		else if(countdia[1] == 4 || (countdia[1] == 3 && countdia[2] == 1)){
				cout << "Case #"<< tablenum << ": O won" << endl;
				continue;
		}


		for(int j=0;j<4;++j){
				for(int i=0;i<3;++i){
						countrow[i] = 0;
						countcol[i] = 0;
					}

				for(int k=0;k<4;++k){
					if(table[j][k]=='X'){
						countrow[0] += 1;
					}
					else if(table[j][k] == 'O'){
						countrow[1] += 1;
					}
					else if(table[j][k] == 'T'){
						countrow[2] += 1;
					}
					else{
						flag = 1;
					}

					if(table[k][j]=='X'){
							countcol[0] += 1;
					}
					else if(table[k][j] == 'O'){
							countcol[1] += 1;
					}
					else if(table[k][j] == 'T'){
							countcol[2] += 1;
					}
					else{
							flag = 1;
					}
				}
			if(countrow[0] == 4 || (countrow[0] == 3 && countrow[2] == 1)){
					cout << "Case #"<< tablenum << ": X won" << endl;
					flag = 2;
					break;
			}
			else if(countrow[1] == 4 || (countrow[1] == 3 && countrow[2] == 1)){
					cout << "Case #"<< tablenum << ": O won" << endl;
					flag = 2;
					break;
			}

			if(countcol[0] == 4 || (countcol[0] == 3 && countcol[2] == 1)){
					cout << "Case #"<< tablenum << ": X won" << endl;
					flag = 2;
					break;
			}
			else if(countcol[1] == 4 || (countcol[1] == 3 && countcol[2] == 1)){
					cout << "Case #"<< tablenum << ": O won" << endl;
					flag = 2;
					break;
			}
		}
		if(flag == 1){
			cout << "Case #"<< tablenum << ": Game has not completed" << endl;
		}
		else if(flag == 0){
			cout << "Case #"<< tablenum << ": Draw" << endl;
		}
	}
	return 0;
}
