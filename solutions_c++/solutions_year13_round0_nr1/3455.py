# include <iostream>
# include <string>
# include <fstream>


using namespace std;


ifstream fin ("A-large.in");
ofstream fout ("A-large.out");

string map [4];
bool empty = false;

void read_map(){
	empty = false;
	for (int i=0;i<4;i++){
		fin >> map[i];
		for (int j=0;j<4;j++)
			if (map[i][j] == '.')
				empty = true;
	}
}

bool Won (char c){

	if ( c == 'X' )
		c = 'O';
	else 
		c = 'X';


	//rows
	for (int i=0;i<4;i++){
		int cnt = 0;
		for (int j=0;j<4;j++){
			if (map[i][j] == c)
				break;
			else if (map[i][j] != '.')
				cnt ++;
		}
		if (cnt == 4)
			return true;
	}
	
	//col
	for (int i=0;i<4;i++){
		int cnt = 0;
		for (int j=0;j<4;j++){
			if (map[j][i] == c)
				break;
			else if (map[j][i] != '.')
				cnt ++;
		}
		if (cnt == 4)
			return true;
	}

	//diag
	string diag1=""; 
	diag1 += map[0][0];
	diag1 += map[1][1];
	diag1 += map[2][2];
	diag1 += map[3][3];

	string diag2="";
	diag2 += map[0][3];
	diag2 += map[1][2];
	diag2 += map[2][1];
	diag2 += map[3][0];

	int cnt1 = 0,cnt2 = 0;

	for (int i=0;i<4;i++){
		if (diag1[i] == c)
			break;
		else if (diag1[i]!='.')
			cnt1++;
	}

	if (cnt1 == 4)
		return true;

	for (int i=0;i<4;i++){
		if (diag2[i] == c)
			break;
		else if (diag2[i]!='.')
			cnt2++;
	}

	if (cnt2 == 4)
		return true;

	return false;
}

int main (){
	int T;

	fin >> T;

	for (int i=0;i<T;i++){
		read_map();

		if (Won('X'))
			fout << "Case #" << i+1 << ": X won\n";
		else if (Won('O'))
			fout << "Case #" << i+1 << ": O won\n";
		else if (empty)
			fout << "Case #" << i+1 << ": Game has not completed\n";
		else
			fout << "Case #" << i+1 << ": Draw\n";
	}
	return 0;
}