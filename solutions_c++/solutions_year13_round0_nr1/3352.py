#include<iostream>
#include<map>
#include<vector>
#include<string>
using namespace std;

map<char,int> charMap;

void solve(char** board, int t)
{
	bool isOver = true;
	int b[10] = {1,1,1,1,1,1,1,1,1,1};
	FILE *fpOut = fopen("/Users/adarshkumarsharma/cpp/Code/CodeJam/Tic-Tac-Toe/src/A-large.out","a+");

	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			b[i] *= charMap[board[i][j]];

	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			b[i+4] *= charMap[board[j][i]];

	for(int j=0;j<4;j++)
		b[8] *= charMap[board[j][j]];

	for(int j=0;j<4;j++)
		b[9] *= charMap[board[3-j][j]];


	char winner = 'N';
	for(int i=0;i<10;i++)
	{
		if(b[i]==0)
			isOver = false;
		else if(b[i]%2==0 && b[i]%3==0)
			continue;
		else if(b[i]%2==0)
		{
			winner = 'X';
			break;
		}
		else if (b[i]%3==0)
		{
			winner = 'O';
			break;
		}
	}

	fprintf(fpOut, "Case #%d: ",t);
	if(winner!='N')
		fprintf(fpOut,"%c won\n",winner);
	else if(isOver == true)
		fprintf(fpOut,"Draw\n");
	else
		fprintf(fpOut,"Game has not completed\n");

	fclose(fpOut);
}

int main()
{
	charMap['X'] = 2;
	charMap['O'] = 3;
	charMap['T'] = 1;
	charMap['.'] = 0;

	FILE * fp = fopen("/Users/adarshkumarsharma/cpp/Code/CodeJam/Tic-Tac-Toe/src/A-large.in","r");
	int T;
	fscanf(fp,"%d",&T);
	char** board = new char*[4];
	for(int i=0;i<4;i++)
		board[i] = new char[5];

	for(int t=0;t<T;t++)
	{
		char temp[10];
		for(int i=0;i<4;i++)
		{
			memset(board[i],0,5);
			fgets(temp,10,fp);
			fread(board[i],1,4,fp);
		}
		fgets(temp,10,fp);
		solve(board, t+1);
	}

	for(int i=0;i<4;i++)
		delete[] board[i];
	delete[] board;
	fclose(fp);

}





