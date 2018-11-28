#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <list>
#include <stack>
#include <algorithm>
#include <queue>
#include <map>
#include <cstdlib>
#include <set>
#include <string>
#include <cstring>
#include <memory>
using namespace std;

//ofstream fout("C:\\Users\\Administrator\\Desktop\\A.out");
#define fout cout

class A
{
public:
	void Run();

private:
	void Input();
	void Do();
	void Output();

private:
	int caseNum, caseIndex;
	char board[4][10];
	int result;
};

void A::Run()
{
	scanf("%d", &caseNum);
	for(caseIndex = 1; caseIndex <= caseNum; ++caseIndex)
	{
		Input();
		Do();
		Output();
	}
}

void A::Input()
{
	for(int i = 0; i < 4; ++i)
		scanf("%s", board[i]);
}

void A::Do()
{
	result = 3;
	int xCount, oCount, tCount;
	for(int i = 0; i < 4; ++i)
	{
		xCount = oCount = tCount = 0;
		for(int j = 0; j < 4; ++j)
		{
			if(board[i][j] == 'X')
				++xCount;
			else if(board[i][j] == 'O')
				++oCount;
			else if(board[i][j] == 'T')
				++tCount;
		}
		if(xCount + tCount == 4) result = 0;
		else if(oCount + tCount == 4) result = 1;
	}
	
	if(result != 3) return;
	for(int i = 0; i < 4; ++i)
	{
		xCount = oCount = tCount = 0;
		for(int j = 0; j < 4; ++j)
		{
			if(board[j][i] == 'X')
				++xCount;
			else if(board[j][i] == 'O')
				++oCount;
			else if(board[j][i] == 'T')
				++tCount;
		}
		if(xCount + tCount == 4) result = 0;
		else if(oCount + tCount == 4) result = 1;
	}

	if(result != 3) return;
	xCount = oCount = tCount = 0;
	for(int i = 0; i < 4; ++i)
	{
		if(board[i][i] == 'X')
			++xCount;
		else if(board[i][i] == 'O')
			++oCount;
		else if(board[i][i] == 'T')
			++tCount;
	}
	if(xCount + tCount == 4) result = 0;
	else if(oCount + tCount == 4) result = 1;

	if(result != 3) return;
	xCount = oCount = tCount = 0;
	for(int i = 0; i < 4; ++i)
	{
		if(board[i][ 3 - i] == 'X')
			++xCount;
		else if(board[i][ 3 - i] == 'O')
			++oCount;
		else if(board[i][ 3 - i] == 'T')
			++tCount;
	}
	if(xCount + tCount == 4) result = 0;
	else if(oCount + tCount == 4) result = 1;

	if(result != 3) return;
	for(int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
		{
			if(board[i][j] == '.')
			{
				return;
			}
		}
	}
	result = 2;
}

void A::Output()
{
	fout << "Case #" << caseIndex << ": ";
	if(result == 0) fout << "X won";
	else if(result == 1) fout << "O won";
	else if(result == 2) fout << "Draw";
	else fout << "Game has not completed";

	fout << endl;
	//printf("Case #%d: %s\n", caseIndex, result ? "YES" : "NO");
}

A instance;
int main()
{
	instance.Run();
	return 0;
}
