#include <fstream>
#include <iostream>
#include <stdio.h>
using namespace std;


char matrix[9][9];
char matrix2[9][9];

int char_index(char x)
{
	switch(x)
	{
		case 'q':
		case'Q':
		return 0;

		case 'w':
		case'W':
		return 1;

		case 'e':
		case'E':
		return 2;

		case 'r':
		case'R':
		return 3;

		case 'a':
		case'A':
		return 4;

		case 's':
		case'S':
		return 5;

		case 'd':
		case'D':
		return 6;

		case 'f':
		case'F':
		return 7;

		default:
		cout<<"Error!!!!!!!!!!!!!!!";
		cout<<" The offending character is "<<x<<"."<<endl;
		return 8;
	}
}




class Combo
{
	public:
	char array[100];
	int posn;

	public:
	Combo()
	{
		posn = 0;
	}
	void push(char c)
	{
		char result;

		if (posn == 0)
		{
			array[0] = c;
			posn++;
			return;
		}

		result = matrix[char_index(array[posn-1])][char_index(c)];
		if ( result != '\0' )
		{
			posn--;
			push(result);
			return;
		}
		else
		{
			array[posn] = c;
			posn++;
		}
		for (int i = 0; i < posn - 1; i++)
		{
			if ( matrix2[char_index(array[i])][char_index(c)] == '#')
			{
				posn = 0;
				return;
			}
		}
		
	}
};
int main()
{
	ifstream inp("B-large.in", ifstream::in);
	ofstream outp("outputlarge.txt", ofstream::out);

	/**** Declare variables ***/

	int T;
	int C, D, N;
	char c3[3], c2[2], c;

	/******* Start looping ******/
	inp>>T;
	cout<<"Reading T="<<T<<endl;
	for (int i = 1; i <= T; i++)
	{
		cout<<"Case "<<i<<endl;
		for (int j = 0; j < 9; j++)
			for (int k = 0; k < 9; k++)
				matrix[j][k] = 0;

		for (int j = 0; j < 9; j++)
			for (int k = 0; k < 9; k++)
				matrix2[j][k] = 0;


		inp>>C;
		cout<<"Reading C="<<C<<":";

		for (int j = 0; j < C; j++)
		{
			inp>>c3[0]>>c3[1]>>c3[2];
			cout<<c3[0]<<c3[1]<<c3[2]<<endl;
			matrix[char_index(c3[0])][char_index(c3[1])] = c3[2];
			matrix[char_index(c3[1])][char_index(c3[0])] = c3[2];
		}

		inp>>D;
		cout<<"Reading D="<<D<<":";

		for (int j = 0; j < D; j++)
		{
			inp>>c3[0]>>c3[1];
			cout<<c3[0]<<c3[1]<<endl;
			matrix2[char_index(c3[0])][char_index(c3[1])] = '#';
			matrix2[char_index(c3[1])][char_index(c3[0])] = '#';
		}

		inp>>N;
		cout<<"Reading N="<<N<<endl;
		Combo obj;
		for (int j = 0; j < N; j++)
		{
			inp>>c;
			obj.push(c);
		}

		/********* Display solution ***********/
		outp<<"Case #"<<i<<": [";
		if (obj.posn == 0)
		{
			outp<<"]"<<endl;
			continue;
		}
		for(int j = 0; j < obj.posn - 1; j++)
		{
			outp<<obj.array[j]<<", ";
		}
		
		outp<<obj.array[obj.posn - 1]<<"]"<<endl;
	}

	/****** End ********/
	return 0;
}
