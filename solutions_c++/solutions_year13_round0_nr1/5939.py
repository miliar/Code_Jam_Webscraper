// CodeJamQA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

FILE * input;
char board[4][4];
int hasempty;

void readboard()
{int r;
	for(int l=0; l< 4; l++)
		r= fscanf(input, "%4c ", board[l]);
	fscanf(input," ");
	
}

char chekline(int l)
{
	char last, cur;

	if((last = board[l][0]) == '.')
	{
		hasempty =1;
		return 0;
	}
	for(int  j=1; j<4; j++)
	{
		cur = board[l][j];
		if(cur == '.')
		{
			hasempty=1;
			return 0;
		}
		if (cur == 'T')
			continue;
		if (cur != last && last != 'T')
			return 0;
		last =cur;
	}
	return cur;
}

char chekseq( char *start, int inc)
{
	char last, cur;

	if((last = *start) == '.')
	{
		hasempty =1;
		return 0;
	}

	start+=inc;
	for(int  j=1; j<4; j++, start+=inc)
	{
		cur = *start;
		if(cur == '.')
		{
			hasempty=1;
			return 0;
		}
		if (cur == 'T')
			continue;
		if (cur != last && last != 'T')
			return 0;
		last =cur;
	}
	return last;
}


char * check()
{
	
	static char buffer[]= "W won";
	int x,o,t,e;
	char winner;

	hasempty=0;
	//scan line
	for(int l=0; l<4; l++)
	{
		if (( buffer[0] = chekseq(board[l], 1)) != 0)
		{
			return buffer;
		}
	}

	for(int l=0; l<4; l++)
		if (( buffer[0] = chekseq(&board[0][l], 4)) != 0)
			return buffer;

	if (( buffer[0] = chekseq(&board[0][0], 5)) != 0)
	return buffer;

	if (( buffer[0] = chekseq(&board[0][3], 3)) != 0)
	return buffer;

	if (! hasempty)
		return "Draw";
	return "Game has not completed";

}

int _tmain(int argc, _TCHAR* argv[])
{
	int cases;



	input = _wfopen (argv[1],L"r");

	fscanf(input, "%d ", &cases);

	for(int i=1; i<= cases; i++)
	{
		readboard();
		printf("Case #%d: %s\n", i,  check());
	}
	return 0;
}

