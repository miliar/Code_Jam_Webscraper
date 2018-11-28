#include<iostream>
#include<fstream>
#include <string.h>

using namespace std;

const int SIZE = 26;
const int N  = 101;

ifstream fin("mag_large.in");
ofstream fout("mag_large.out");

int cas, index = 1;

int c, d, n;

int str[101];
int length;
int combine[SIZE][SIZE];
int oppose[SIZE][SIZE];

void cmbop()
{
	int a, b;
	if (length>1)
	{
		a =str[length-2];
		b = str[length-1];
		if (combine[a][b] != 0)
		{
			str[length-2] = combine[a][b];
			length --;
			return;
		}//end if
	}

	a = str[length-1];
	for (int i=0; i <= length-2; i ++)
	{
		b = str[i];

		if (oppose[a][b] == -1)
		{
			length = 0;
			break;
		}
	}
}


void read()
{
	memset(combine, 0, sizeof(int) * SIZE * SIZE);
	memset(oppose, 0, sizeof(int) * SIZE * SIZE);
	fin >> c;

	char c1, c2, c3;
	for (int i=0; i < c; i ++)
	{
		fin >> c1 >> c2 >> c3;

		combine[c1 - 'A'][c2- 'A'] = c3 - 'A';
		combine[c2-'A'][c1-'A'] = c3-'A';
	}

	fin >> d;
	int i;
	for (i=0; i < d; i ++)
	{
		fin >> c1 >> c2;
		oppose[c1-'A'][c2-'A'] =  -1;
		oppose[c2-'A'][c1-'A'] = -1;
	}
	
	length = 0;
	fin >> n;
	char cha;
	for (i=0; i< n; i ++)
	{
		fin >> cha;
		str[length] = cha - 'A';
		length ++;
		cmbop();
	}
}

void print()
{
	fout<< "Case #" << index <<": [";

	if (length>0)
	{
		char c = 'A' + str[0];
		fout << c;
	}

	for (int i=1; i < length; i ++)
	{
		char c = 'A' + str[i];
		fout << ", " << c;
	}

	fout << "]" << endl;
}


int main()
{
	fin >> cas;

	while (index <= cas)
	{
		read();
		print();
		index ++;
	}

	return 0;
}