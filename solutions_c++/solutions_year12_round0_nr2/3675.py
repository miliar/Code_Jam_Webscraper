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

int main()
{
	ofstream cout ("Problem2.out");
	ifstream cin ("B-large.in"); 

	int T;
	cin >> T;

	int N[100],S[100],p[100],t[100][100];
	for (int i = 0; i < T; i++)
	{
		cin >> N[i];
		cin >> S[i];
		cin >> p[i];
		for (int j = 0; j < N[i]; j++)
		{
			cin >> t[i][j];
		}

		int valid = 0;
		for (int j = 0; j < N[i]; j++)
		{
			if (t[i][j] >= (p[i]*3)-2)
				valid++;
		}
		for (int j = 0; j < N[i]; j++)
		{
			if (t[i][j] < (p[i]*3)-2 && t[i][j] >= (p[i]*3)-4 && S[i] > 0)
			{
				if (t[i][j] != 0 || p == 0)
				{
					S[i]--;
					valid++;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << valid << endl;
	}
	     
	return 0;
}
