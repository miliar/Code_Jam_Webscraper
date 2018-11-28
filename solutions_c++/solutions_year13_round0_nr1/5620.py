// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

void rotate_matrix(int a[][4]){
	int b[4][4];
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++){
			b[i][j] = a[j][3-i];
		}
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++){
			a[i][j] = b[i][j];
		}
}

void print_matrix(int a[][4]){
	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++)
			cout<<a[i][j];
		cout<<endl;
	}
}

int decision(int a[][4]){
	//"X won" -> 1
	//"O won" -> 2
	//"Game has not completed" -> 3
	//"Draw" -> 4
	int countX, countO, countT, countD;
	for (int i = 0; i < 4; i++){
		countX = 0;
		countO = 0;
		countT = 0;
		countD = 0;
		for (int j = 0; j < 4; j++){
			if (a[i][j] == 1)
				countX++;
			if (a[i][j] == 2)
				countO++;
			if (a[i][j] == 3)
				countT++;
			if (a[i][j] == 4)
				countD++;
		}
		if (countX == 4 || (countX == 3 && countT == 1)) return 1;
		if (countO == 4 || (countO == 3 && countT == 1)) return 2;
	}
	
	countX = 0;
	countO = 0;
	countT = 0;
	for (int i = 0; i < 4; i++){
		if (a[i][i] == 1)
			countX++;
		if (a[i][i] == 2)
			countO++;
		if (a[i][i] == 3)
			countT++;
	}
	if (countX == 4 || (countX == 3 && countT == 1)) return 1;
	if (countO == 4 || (countO == 3 && countT == 1)) return 2;
	
	if (countD > 1) return 3;
	else return 4;
}

int main () {
  string line, message;
  ifstream myfile ("A-small-attempt2.in");
  ofstream myresult ("result.txt");
  int game[4][4];
  int iter, a, b, result;
  int count = -1;
  if (myfile.is_open()){
    while (myfile.good()){
		getline (myfile,line);
		if (count == -1){
			stringstream ss(line);
			ss >> iter;
			count++;
		}
		else{
			if (line.empty() == 0){
				for (int i = 0; i < 4; i++){
					if (line[i] == 'X')
						game[count % 4][i] = 1;
					if (line[i] == 'O')
						game[count % 4][i] = 2;
					if (line[i] == 'T')
						game[count % 4][i] = 3;
					if (line[i] == '.')
						game[count % 4][i] = 4;	
				}
				if ((count % 4) == 3){
					a = decision(game);
					rotate_matrix(game);
					b = decision(game);
					if (min(a,b) == 1) result = 1;
					else{
						if (min(a,b) == 2) result = 2;
						else result = b;
					}
					switch(result){
						case 1:	message = "X won";
						break;
						case 2:	message = "O won";
						break;
						case 3:	message = "Game has not completed";
						break;
						case 4:	message = "Draw";
						break;
					}
					myresult<<"Case #"<<(count+1)/4<<": "<<message<<endl;
				}
				count++;
			}	
		}
    }
    myfile.close();
	myresult.close();
  }
  
  return 0;
}