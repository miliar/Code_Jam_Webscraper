/*
ID: ZSilber57
PROG: 
LANG: C++
*/

#include <iostream> 
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <bitset>

using namespace std;

char replace(char x)
{
	if (x == 'a')
		return 'y';
	if (x == 'b')
		return 'h';
	if (x == 'c')
		return 'e';
	if (x == 'd')
		return 's';
	if (x == 'e')
		return 'o';
	if (x == 'f')
		return 'c';
	if (x == 'g')
		return 'v';
	if (x == 'h')
		return 'x';
	if (x == 'i')
		return 'd';
	if (x == 'j')
		return 'u';
	if (x == 'k')
		return 'i';
	if (x == 'l')
		return 'g';
	if (x == 'm')
		return 'l';
	if (x == 'n')
		return 'b';
	if (x == 'o')
		return 'k';
	if (x == 'p')
		return 'r';
	if (x == 'q')
		return 'z';
	if (x == 'r')
		return 't';
	if (x == 's')
		return 'n';
	if (x == 't')
		return 'w';
	if (x == 'u')
		return 'j';
	if (x == 'v')
		return 'p';
	if (x == 'w')
		return 'f';
	if (x == 'x')
		return 'm';
	if (x == 'y')
		return 'a';
	if (x == 'z')
		return 'q';
	return ' ';
}

int main()
{
	ofstream cout ("Problem1.out");
	ifstream cin ("A-small-attempt1.in"); 

	int T;
	cin >> T;

	char inStr[300][1000];
	char trash[100];
	cin.getline(trash,100);
	for (int i = 0; i < T; i++)
	{
		cin.getline(inStr[i],1000);	
	}

	for (int i = 0; i < T; i++)
	{
		for (int j = 0; j < 100; j++)
		{
			if (inStr[i][j] != NULL)
				inStr[i][j] = replace(inStr[i][j]);
		}
	}

	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i+1 << ": ";
		for (int j = 0; j < 100; j++)
		{
			if (inStr[i][j] != NULL)
				cout << inStr[i][j];
		}
		cout << "" << endl;
	}
	     
	return 0;
}
