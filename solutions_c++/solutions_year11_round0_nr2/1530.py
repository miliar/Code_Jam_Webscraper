#include <fstream>
#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

ifstream fin("bs.in");
ofstream fout("bs.out");

int LtoN[26] = {4, 0, 0, 6, 2, 7, 0, 0, 0, 0, 
		0, 0, 0, 0, 0, 0, 0, 3, 5, 0, 
		0, 0, 1, 0, 0, 0 };

char combtab[26][26];

char comb[4] = {0,0,0,0}, op[3] = {0,0,0};

int optab[26][26];

char iarray[101], oarray[101];

int main()
{
	int T, C, D, N, i, j, k, h;
	char ch1, ch2, ch3;
	fin >> T;
	
	for(i = 1; i <= T; i ++)
	{
		memset(combtab, 0, sizeof(char) * 26 * 26);
		memset(optab, 0, sizeof(int) * 26 * 26);
		
		fin >> C;
		for(j = 0; j < C; j ++)
		{
			fin.read(comb, 1);
			fin.read(comb, 3);
			cout << comb << " ";
			combtab[comb[0] - 'A'][comb[1] - 'A'] = comb[2];
			combtab[comb[1] - 'A'][comb[0] - 'A'] = comb[2];
		}
		cout << endl;

		fin >> D;
		for(j = 0; j < D; j ++)
		{
			fin.read(op, 1);
			fin.read(op, 2);
			cout << op << " ";
			
			optab[op[0]-'A'][op[1] - 'A'] = 1;
			optab[op[1]-'A'][op[0] - 'A'] = 1;
		}
		cout << endl;
		
		fin >> N;
		k = -1;
		fin.read(&ch1, 1);
		
		if(i == 78)
		{
			i = 78;
		}
		for(j = 0; j < N; j ++)
		{
			fin.read(&ch1, 1);
			cout << ch1 << " ";
			
			if(k >= 0)
			{
				if(combtab[ch1-'A'][iarray[k]-'A'])
				{
					iarray[k] = combtab[ch1-'A'][iarray[k]-'A'];
				}	
				else
				{
					iarray[++ k] = ch1;
				}

				for(h = 0; h < k; h ++)
				{
					if(optab[iarray[h]-'A'][iarray[k]-'A'])
					{
						k = -1;
					}
				}
			}
			else
			{
				iarray[++ k] = ch1;
			}		
		}
		cout << endl;

		fout << "Case #" << i << ": [";

		for(j = 0; j < k ; j ++)
		{
			fout << iarray[j] << ", ";
		}
		if(k >= 0)
		{
			fout << iarray[k];
		}
		fout << "]" << endl;
	}
}
