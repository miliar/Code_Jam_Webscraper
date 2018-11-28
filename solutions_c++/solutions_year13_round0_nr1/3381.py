#include<iostream>
#include<fstream>
using namespace std;
string a[5];
ifstream in("1.in");
ofstream out("1large.out");
int Try[100][5][3];
int trySum = 0;

bool isO(int x, int y){
	if ((a[x][y-1] == 'O') || (a[x][y-1] == 'T')) return true;
	else return false;
}
bool isX(int x, int y){
	if ((a[x][y-1] == 'X') || (a[x][y-1] == 'T')) return true;
	else return false;
}

void makeTry(){

	for (int i = 1; i <= 4; i++){
		trySum++;
		for (int j = 1; j <= 4; j++){
			Try[trySum][j][1] = i;
			Try[trySum][j][2] = j;
		}
		trySum++;
		for (int j = 1; j <= 4; j++){
			Try[trySum][j][1] = j;
			Try[trySum][j][2] = i;
		}
	}
	trySum++;
	for (int j = 1; j <= 4; j++){
			Try[trySum][j][1] = j;
			Try[trySum][j][2] = j;
	}
	trySum++;
	for (int j = 1; j <= 4; j++){
			Try[trySum][j][1] = j;
			Try[trySum][j][2] = 5-j;
	}
}
bool decided(){
	for (int i = 1; i <= trySum; i++){
		bool isTrue = true;
		for (int j = 1; j <= 4; j++)
			if (!isX(Try[i][j][1],Try[i][j][2])) isTrue = false;
		if (isTrue){out << "X won"; return true;}
		isTrue = true;
		for (int j = 1; j <= 4; j++)
			if (!isO(Try[i][j][1],Try[i][j][2])) isTrue = false;
		if (isTrue){out << "O won"; return true;}
	}
	return false;
}
int main(){


	int n;
	in >> n;
	makeTry();
	for (int iTest = 1; iTest <= n; iTest++){
		out << "Case #" << iTest << ": ";
		for (int line = 0; line <= 4; line++)
			getline(in, a[line]);
		if (!decided()){
			bool isEnd = true;
			for (int i = 1; i <= 4; i++)
				for (int j = 0; j <= 3; j++)
					if (a[i][j] == '.') isEnd = false;
			if (isEnd) out << "Draw";
				else out << "Game has not completed";
		}
		out << endl;
	}
}
