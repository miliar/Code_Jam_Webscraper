// Task1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	char MyArray[4][4] /*= {'.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'}*/;
	ifstream file("A-large.in");
	ofstream offile("input.txt");

	int N = 0;

	file>>N;

	for(int iN=0; iN<N; iN++)
	{
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				file>>MyArray[i][j];

		int iX = 0, iO = 0, iT = 0;
		bool bX = false, bO = false;
		bool bNZ = false;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				if(MyArray[i][j]=='.')
					bNZ = true;

				if(MyArray[i][j] == 'X')
					iX++;
				if(MyArray[i][j] == 'O')
					iO++;
				if(MyArray[i][j] == 'T')
					iT++;
			}
			if(iX==4 || (iX==3 && iT==1))
				bX=true;
			if(iO==4 || (iO==3 && iT==1))
				bO=true;

			iX = iO = iT =0;
		}

		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				if(MyArray[j][i]=='.')
					bNZ = true;

				if(MyArray[j][i] == 'X')
					iX++;
				if(MyArray[j][i] == 'O')
					iO++;
				if(MyArray[j][i] == 'T')
					iT++;
			}
			if(iX==4 || (iX==3 && iT==1))
				bX=true;
			if(iO==4 || (iO==3 && iT==1))
				bO=true;

			iX = iO = iT =0;
		}

		// проверка по диагоналям
		for(int i=0; i<4; i++)
		{
			if(MyArray[i][i] == 'X')
				iX++;
			if(MyArray[i][i] == 'O')
				iO++;
			if(MyArray[i][i] == 'T')
				iT++;
		}
		if(iX==4 || (iX==3 && iT==1))
			bX=true;
		if(iO==4 || (iO==3 && iT==1))
			bO=true;
		iX = iO = iT =0;

		for(int i=0; i<4; i++)
		{
			if(MyArray[i][3-i] == 'X')
				iX++;
			if(MyArray[i][3-i] == 'O')
				iO++;
			if(MyArray[i][3-i] == 'T')
				iT++;
		}
		if(iX==4 || (iX==3 && iT==1))
			bX=true;
		if(iO==4 || (iO==3 && iT==1))
			bO=true;
		iX = iO = iT =0;

		// Игра не окончена
		if(!bX && !bO && bNZ)
			offile<<"Case #"<<iN+1<<": Game has not completed"<<endl;

		// ничья
		if((!bX && !bO && !bNZ) || (bX && bO))
			offile<<"Case #"<<iN+1<<": Draw"<<endl;

		// Выиграл X
		if(bX && !bO)
			offile<<"Case #"<<iN+1<<": X won"<<endl;

		// Выиграл О
		if(bO && !bX)
			offile<<"Case #"<<iN+1<<": O won"<<endl;


		cout<<endl;
	}
	offile.close();
	int n;
	cin>>n;


	return 0;
}

void Output(char OutArray[4][4])
{
	int n;
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
			cout<<OutArray[i][j];
		cout<<endl;
	}
	cin>>n;
}

void InputArray(char OutArray[4][4])
{
	cout<<"Vvedite dannye"<<endl;
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			cin>>OutArray[i][j];
}
