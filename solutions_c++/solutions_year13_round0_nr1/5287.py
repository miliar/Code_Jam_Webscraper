#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;

typedef struct position
{
	int x; //column
	int y; //row
}position;

bool isWinner(position* pos, int num)
{
	if(num<4)
		return false;
	int row[4],column[4],diagA=0,diagB=0;
	for(int i=0;i<4;i++)
		row[i]=column[i]=0;
	for(int i=0;i<num;i++)
	{
		row[pos[i].y]++;
		column[pos[i].x]++;
		if(pos[i].x==pos[i].y)
			diagA++;
		if(pos[i].x+pos[i].y==3)
			diagB++;
	}
	for(int i=0;i<4;i++)
	{
		if(row[i]==4||column[i]==4||diagA==4||diagB==4)
			return true;
	}
	return false;
}

int main(void)
{
	ifstream ifs;
	ifs.open("A-large.in",ios_base::in);
	ofstream ofs;
	ofs.open("A-large.out",ios_base::trunc);
	int T;
	ifs>>T;
	char board[4][4];

	for(int caseNo=1;caseNo<=T;caseNo++)
	{
		position X[16],Y[16],empty[16];
		bool Xwin=false,Ywin=false;
		int numX=0,numY=0,numEmpty=0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				ifs>>board[i][j];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				if(board[i][j]=='X'||board[i][j]=='T')
				{
					X[numX].x=j;
					X[numX].y=i;
					numX++;
				}
				if(board[i][j]=='O'||board[i][j]=='T')
				{
					Y[numY].x=j;
					Y[numY].y=i;
					numY++;
				}
				if(board[i][j]=='.')
				{
					empty[numEmpty].x=j;
					empty[numEmpty].y=i;
					numEmpty++;
				}
			}
		Xwin=isWinner(X,numX);
		if(Xwin)
		{
			ofs<<"Case #"<<caseNo<<": X won"<<endl;
			ifs.get();
			continue;
		}
		Ywin=isWinner(Y,numY);
		if(Ywin)
		{
			ofs<<"Case #"<<caseNo<<": O won"<<endl;
			ifs.get();
			continue;
		}
		if(numEmpty)
			ofs<<"Case #"<<caseNo<<": Game has not completed"<<endl;
		else
			ofs<<"Case #"<<caseNo<<": Draw"<<endl;
		ifs.get();
	}
}