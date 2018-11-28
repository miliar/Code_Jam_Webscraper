#include<iostream>
#include<fstream>
using namespace std;

int result(char a[4][4])
{
	int i,j;
	for(i = 0; i < 4; i++)
	{
		for(j = 0; j < 4 && (a[i][j] == 'X' || a[i][j] == 'T'); j++);
		if(j == 4)
			return 2;
		for(j = 0; j < 4 && (a[i][j] == 'O' || a[i][j] == 'T'); j++);
		if(j == 4)
			return 1;
		for(j = 0; j < 4 && (a[j][i] == 'X' || a[j][i] == 'T'); j++);
		if(j == 4)
			return 2;
		for(j = 0; j < 4 && (a[j][i] == 'O' || a[j][i] == 'T'); j++);
		if(j == 4)
			return 1;
	}
	if((a[0][0] == 'X' || a[0][0] == 'T') && (a[1][1] == 'X' || a[1][1] == 'T') && (a[2][2] == 'X' || a[2][2] == 'T') && (a[3][3] == 'X' || a[3][3] == 'T'))
		return 2;
	if((a[0][0] == 'O' || a[0][0] == 'T') && (a[1][1] == 'O' || a[1][1] == 'T') && (a[2][2] == 'O' || a[2][2] == 'T') && (a[3][3] == 'O' || a[3][3] == 'T'))
		return 1;
	if((a[3][0] == 'X' || a[3][0] == 'T') && (a[2][1] == 'X' || a[2][1] == 'T') && (a[1][2] == 'X' || a[1][2] == 'T') && (a[0][3] == 'X' || a[0][3] == 'T'))
		return 2;
	if((a[3][0] == 'O' || a[3][0] == 'T') && (a[2][1] == 'O' || a[2][1] == 'T') && (a[1][2] == 'O' || a[1][2] == 'T') && (a[0][3] == 'O' || a[0][3] == 'T'))
		return 1;
	for(i = 0; i < 4; i++)
		for(j = 0; j < 4; j++)
			if(a[i][j] == '.')
				return 4;
	return 3;
}


int main()
{
	ifstream infile("D:\\input.txt");
	ofstream outfile("D:\\output.txt");
	if(!infile){
		cout << "Can't open input.txt" << endl;
	}
	if(!outfile){
		cout << "Can't open output.txt" << endl;
	}
	int T;
	infile >> T;
	char a[4][4];
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			a[i][j] = '0';
	for(int i = 0; i < T; i++)
	{
		for(int j = 0; j < 4; j++)
			for(int k = 0; k < 4; k++)
			infile >> a[j][k];
		if(result(a) == 1)
			outfile << "Case #" << i+1 << ": " << "O won" << endl;
		else if(result(a) == 2)
			outfile << "Case #" << i+1 << ": " << "X won" << endl;
		else if(result(a) == 3)
			outfile << "Case #" << i+1 << ": " << "Draw" << endl;
		else
			outfile << "Case #" << i+1 << ": " << "Game has not completed" << endl;
	}
	return 0;
}