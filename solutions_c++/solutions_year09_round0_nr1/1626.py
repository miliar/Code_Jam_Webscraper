#include <iostream>
#include <string>
#include <fstream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("out.txt");
	int L, D, N;
bool search(char str[], char dict[5050][30])
{
	for (int zz = 0; zz < 30; zz++)
	{
		for (int pp = 0; pp < D; pp++)
		{
			for (int qq = 0; qq < 30; qq++)
			{
				if (str[zz] != dict[pp][qq])
				{
					break;
				}
				else if (dict[pp][qq] == '\0')
				{
					return true;
					break;
				}
			}
		}
	}
	return false;
}


int main()
{

	fin >> L >> D >> N;

	char dict[5050][30] = {'\0'};
	for (int i = 0; i < D; i++)
	{
		fin >> dict[i];
	}

	char letters[30][30];
	string group;
	int cnt = 0;
	for (int i = 0; i < N; i++)
	{
		fin >> group;
		bool inParent = false;
		int k = 0;
		int m = 0;
		for (int yy =0; yy < 30; yy++)
		{
			for (int zz=0;zz<30;zz++)
				letters[yy][zz] = '\0';
		}
		for (int j = 0; j < group.length(); j++)
		{
			if (group[j] == '(')
			{
				inParent = true;
				continue;
			}
			else if (group[j] == ')')
			{
				inParent = false;
				k++;
				m = 0;
				continue;
			}

			if (inParent)
			{
				letters[k][m] = group[j];
				m++;
			}
			else
			{
				letters[k][m] = group[j];
				k++;
				m = 0;
			}
		}

		//cout << endl;
		/*for (int pp = 0; pp < L; pp++)
		{
			cout << letters[pp] << endl;
		}*/
		//cout << endl;

		cnt = 0;
		for (int xx = 0; xx < D; xx++)
		{
			bool foundWord = false;
			for (int yy = 0; yy < L; yy++)
			{
				bool foundLetter = false;
				for (int zz = 0; zz < 30; zz++)
				{
					if (dict[xx][yy] == letters[yy][zz])
					{
						foundLetter = true;
						if (yy == L-1)
						{
							//cout << dict[xx] << endl;
							foundWord = true;
						}
						break;
					}
				}
				if (!foundLetter)
					break;
				if (foundWord)
				{
					cnt++;
					break;
				}
			}


		}
		//cout << endl;
		fout << "Case #" << i+1 << ": " << cnt << endl;
	}

}