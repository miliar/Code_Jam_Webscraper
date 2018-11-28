#include<iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("A-small-attempt0.in", ios::in);
	ofstream fout("A_small.out", ios::out);

	int l;
	int d;
	int n;
	int j;
	int length;
	int row;
	int sum;
	char dic[5000][16];
	char now[256];
	bool set[15][26];
	bool flag;
	
	fin >> l >> d >> n;
	// input dic[]
	for (int i=0; i<d; i++)
		fin >> dic[i];

	for (i=0; i<n; i++)
	{
		sum = 0;

		fin >> now;
		// initialize set[][]
		length = strlen(now);
		row = 0;
		memset(set, 0, sizeof(set));
		j = 0;
		while (j<length)
		{
			if (now[j] == '(')
			{
				j++;
				while (now[j] != ')')
					set[row][now[j++] - 'a'] = true;
				row++;
				j++;
			}
			else
			{
				set[row][now[j] - 'a'] = true;
				row++;
				j++;
			}
		}
		// match
		for (j=0; j<d; j++)
		{
			flag = true;
			for (int k=0; k<l; k++)
				if (!set[k][dic[j][k] - 'a'])
				{
					flag = false;
					break;
				};
			if (flag)
				sum++;
		}
		fout << "Case #" << i+1 << ": " << sum <<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
