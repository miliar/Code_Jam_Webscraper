#include<iostream>
#include<stdio.h>

using namespace std;

void copy(char A[4][5], char B[4][5], char c)
{
	for(int i = 0; i < 4; i++)
	for(int j = 0; j < 4; j++)
	if(A[i][j] == 'T')
	B[i][j] = c;
	else B[i][j] = A[i][j];
}

bool check(char board[4][5], char c)
{
	char temp[4][5];
	copy(board, temp, c);
	int col[4] = {0, 0, 0, 0};
	int row[4] = {0, 0, 0, 0};
	int diag1 = 0, diag2 = 0;
	for(int i = 0; i < 4; i++)
	for(int j = 0; j < 4; j++)
	{
		if(temp[i][j] == c)
		{
			if(i == j)
			diag1++;
			if(i == 3-j)
			diag2++;
			col[j]++;
			row[i]++;
		}
	}
	if(col[0] == 4 || col[1] == 4 || col[2] == 4 || col[3] == 4)
	return true;
	if(row[0] == 4 || row[1] == 4 || row[2] == 4 || row[3] == 4)
	return true;
	if(diag1 == 4 || diag2 == 4)
	return true;
	return false;
}

int count(char A[4][5])
{
	int n = 0;
	for(int i = 0; i < 4; i++)
	for(int j = 0; j < 4; j++)
	if(A[i][j] != '.')
	n++;
	return n;
}

int main(void)
{
	freopen("C:/Downloads/GCJ-QR-A-Large-In.in", "r", stdin);
	freopen("C:/Downloads/GCJ-QR-A-Large-Out.txt", "w+", stdout);
	int T;
	cin>>T;
	int n = 1;
	char board[4][5];
	char temp;
	while(n <= T)
	{
		for(int i = 0; i < 4; i++)
		cin>>board[i];
		
		cout<<"Case #"<<n++<<": ";
		
		if(check(board, 'X'))
			cout<<"X won"<<endl;
		else if(check(board, 'O'))
			cout<<"O won"<<endl;
		else if(count(board) == 16)
			cout<<"Draw"<<endl;
		else 
			cout<<"Game has not completed"<<endl;
	}
}
