#include<iostream>
#include<fstream>
#include<string>

using namespace std;
string s[4];

int f()
{
	int i, j;

	for (i=0; i<4; i++) {
		if ((s[i][0]=='O' || s[i][0]=='T')&&(s[i][1]=='O' || s[i][1]=='T')&&(s[i][2]=='O' || s[i][2]=='T')&&(s[i][3]=='O' || s[i][3]=='T')) return 1;
		if ((s[0][i]=='O' || s[0][i]=='T')&&(s[1][i]=='O' || s[1][i]=='T')&&(s[2][i]=='O' || s[2][i]=='T')&&(s[3][i]=='O' || s[3][i]=='T')) return 1;
		if ((s[i][0]=='X' || s[i][0]=='T')&&(s[i][1]=='X' || s[i][1]=='T')&&(s[i][2]=='X' || s[i][2]=='T')&&(s[i][3]=='X' || s[i][3]=='T')) return 2;
		if ((s[0][i]=='X' || s[0][i]=='T')&&(s[1][i]=='X' || s[1][i]=='T')&&(s[2][i]=='X' || s[2][i]=='T')&&(s[3][i]=='X' || s[3][i]=='T')) return 2;
	}
	if ((s[0][0]=='O' || s[0][0]=='T')&&(s[1][1]=='O' || s[1][1]=='T')&&(s[2][2]=='O' || s[2][2]=='T')&&(s[3][3]=='O' || s[3][3]=='T')) return 1;
	if ((s[0][0]=='X' || s[0][0]=='T')&&(s[1][1]=='X' || s[1][1]=='T')&&(s[2][2]=='X' || s[2][2]=='T')&&(s[3][3]=='X' || s[3][3]=='T')) return 2;
	if ((s[0][3]=='O' || s[0][3]=='T')&&(s[1][2]=='O' || s[1][2]=='T')&&(s[2][1]=='O' || s[2][1]=='T')&&(s[3][0]=='O' || s[3][0]=='T')) return 1;
	if ((s[0][3]=='X' || s[0][3]=='T')&&(s[1][2]=='X' || s[1][2]=='T')&&(s[2][1]=='X' || s[2][1]=='T')&&(s[3][0]=='X' || s[3][0]=='T')) return 2;

	for (i=0; i<3; i++)
		for (j=0; j<3; j++) if (s[i][j]=='.') return 0;
	return 3;
}

int main(){
	int i, j, k, m, n, a, b, c, t, tt, res;

	ifstream fin("A-small-attempt0.in");
	ofstream fout("out.txt");
	fin >> tt;
	for (t=1; t<=tt; t++){
		res =0;
		fin >> s[0] >> s[1] >> s[2] >> s[3];
		res = f();
		fout << "Case #" << t << ": ";
		if (res == 0 ) fout << "Game has not completed";
		if (res == 1) fout << "O won";
		if (res == 2 ) fout << "X won";
		if (res == 3) fout << "Draw";
		fout << endl;
	}
}