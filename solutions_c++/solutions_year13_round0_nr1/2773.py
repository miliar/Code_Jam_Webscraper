#include <cstdio>
#include <map>
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int t, c=1;
	scanf("%d", &t);
	ofstream myfile;
	myfile.open ("GCJA.out");
	while(t--)
	{
		char a[4][4];
		int flag = 0, win = -1;
		map<char,int> row, col, d1, d2;

		for(int i=0; i<4; i++)
				scanf("\n%c%c%c%c", &a[i][0], &a[i][1], &a[i][2], &a[i][3]);

		d1['T'] = d2['T'] = 0;
		d1['X'] = d2['X'] = 0;
		d1['O'] = d2['O'] = 0;
		d1['.'] = d2['.'] = 0;
		for(int i=0; i<4; i++)
		{
			row['T'] = col['T'] = 0;
			row['X'] = col['X'] = 0;
			row['O'] = col['O'] = 0;
			row['.'] = col['.'] = 0;
			for(int j=0; j<4; j++)
			{
				row[a[i][j]]++;
				col[a[j][i]]++;
				if(i == j)
				{
					d1[a[i][j]]++;
				}
				if(i+j == 3)
				{
					d2[a[i][j]]++;
				}
			}
			if(row['.'] > 0 || col['.'] > 0)
			{
				flag = 1;
			}
			if(((row['X'] == 3 && row['T'] == 1) || row['X'] == 4) || ((col['X'] == 3 && col['T'] == 1) || col['X'] == 4))
			{
				win = 0;
				break;
			}
			else if(((row['O'] == 3 && row['T'] == 1) || row['O'] == 4) || ((col['O'] == 3 && col['T'] == 1) || col['O'] == 4))
			{
				win = 1;
				break;
			}
		}

		if(win == -1)
		{
			if(((d1['X'] == 3 && d1['T'] == 1) || d1['X'] == 4) || ((d2['X'] == 3 && d2['T'] == 1) || d2['X'] == 4))
				win = 0;
			else if(((d1['O'] == 3 && d1['T'] == 1) || d1['O'] == 4) || ((d2['O'] == 3 && d2['T'] == 1) || d2['O'] == 4))
				win = 1;
		}

		if(win == 0)
			myfile << "Case #"<< c << ": X won\n";
		else if(win == 1)
			myfile << "Case #"<< c << ": O won\n";
		else if(flag)
			myfile << "Case #"<< c << ": Game has not completed\n";
		else
			myfile << "Case #"<< c << ": Draw\n";
		c++;
	}
}
