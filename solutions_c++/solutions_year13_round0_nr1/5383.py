#include<iostream>
#include<stdio.h>
#include<string>
#include<fstream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

char map[4][4];

void clearmap()
{
	for (int i=0; i<4; i++)
	{
		for (int j=0; j<4; j++)
		{
			map[i][j] = 'A';
		}
	}
}

char whowin()
{
	int xcnt = 0, ocnt = 0, tcnt = 0, emptycnt = 0;
	// check row
	
	for (int row=0; row<4; row++)
	{
		xcnt = 0; ocnt = 0; tcnt = 0; emptycnt = 0;
		for (int i=0; i<4; i++)
		{
			if (map[row][i] == 'X') xcnt++;
			if (map[row][i] == 'O') ocnt++;
			if (map[row][i] == 'T') tcnt++;
			if (map[row][i] == '.') emptycnt++;
		}
		if (xcnt == 4) {return 'X';}
		if (ocnt == 4) {return 'O';}
		if ((xcnt == 3) && (tcnt == 1)) {return 'X';}
		if ((ocnt == 3) && (tcnt == 1)) {return 'O';}

	}
	// check col
	for (int col = 0; col<4; col++)
	{
		xcnt = 0; ocnt = 0; tcnt = 0;
		for (int i=0; i<4; i++)
		{
			if (map[i][col] == 'X') xcnt++;
			if (map[i][col] == 'O') ocnt++;
			if (map[i][col] == 'T') tcnt++;
		}
		if (xcnt == 4) {return 'X';}
		if (ocnt == 4) {return 'O';}
		if ((xcnt == 3) && (tcnt == 1)) {return 'X';}
		if ((ocnt == 3) && (tcnt == 1)) {return 'O';}
	}
	// check dia
	xcnt = 0; ocnt = 0; tcnt = 0;
	for (int index = 0; index<4; index++)
	{
		if (map[index][index] == 'X') xcnt++;
		if (map[index][index] == 'O') ocnt++;
		if (map[index][index] == 'T') tcnt++;
	}
	if (xcnt == 4) {return 'X';}
	if (ocnt == 4) {return 'O';}
	if ((xcnt == 3) && (tcnt == 1)) {return 'X';}
	if ((ocnt == 3) && (tcnt == 1)) {return 'O';}

	xcnt = 0; ocnt = 0; tcnt = 0; 
	for (int index = 0; index<4; index++)
	{
		if (map[index][3-index] == 'X') xcnt++;
		if (map[index][3-index] == 'O') ocnt++;
		if (map[index][3-index] == 'T') tcnt++;
	}
	if (xcnt == 4) {return 'X';}
	if (ocnt == 4) {return 'O';}
	if ((xcnt == 3) && (tcnt == 1)) {return 'X';}
	if ((ocnt == 3) && (tcnt == 1)) {return 'O';}
	if (emptycnt > 0) {return 'N';}
	return 'D';
}

int main()
{
    ifstream infile;
    infile.open("A-small-attempt0.in", ifstream::in);
    ofstream outfile;
    outfile.open("A-small-attempt0.out", ofstream::out);


     int T;
     char result;
     char line[101];

      if (!infile.is_open())
    {
        cout<<"Failed open file"<<endl;
        return 0;
    } 

    clearmap();

    infile.getline(line,101);
    sscanf(line, "%d", &T);
    cout<<T<<endl;
	for (int l=0; l<T; l++)
    {
    	for (int row = 0; row<4; row++)
    	{
    		infile.getline(line,101);
    		for (int col = 0; col<4; col++)
    		{
    			map[row][col] = line[col];
				cout<<map[row][col];
    		}
			cout<<'\n';
    	}
		infile.getline(line,101);
    	result = whowin();
    	if (result == 'X')
    	{
    		outfile<<"Case #"<<l+1<<": "<<"X won\n";
    	}
    	if (result == 'O')
    	{
    		outfile<<"Case #"<<l+1<<": "<<"O won\n";
    	}
    	if (result == 'N')
    	{
    		outfile<<"Case #"<<l+1<<": "<<"Game has not completed\n";
    	}
    	if (result == 'D')
    	{
    		outfile<<"Case #"<<l+1<<": "<<"Draw\n";
    	}
    }


    infile.close();
    outfile.close();
    return 0;
}