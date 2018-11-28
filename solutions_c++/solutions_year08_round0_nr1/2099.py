#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	int N, S, Q;
	int table[1001][101];
	int solution;
	char name[101][100];
	char input[1001][100];

	ifstream fin("A-large.in");
	//ifstream fin("input.txt");
	ofstream fout("output.txt");

	fin >> N;
	for(int k=1; k<=N; k++)
	{
		fin >> S;
		for(int i=0; i<=S; i++)
		{
			fin.getline(name[i], 100, '\n');
			table[0][i] = 0;
		}
		fin >> Q;
		for(int i=0; i<=Q; i++)
			fin.getline(input[i], 100, '\n');

		for(int i=1; i<=Q; i++)
		{
			for(int j=1; j<=S; j++)
			{
				if(strcmp(input[i],name[j]) != 0)
					table[i][j] = table[i-1][j];
				else
				{
					table[i][j] = 10000;
					for(int l=1; l<=S; l++)
						table[i][j] = (table[i][j] > table[i-1][l] + 1 && j != l)? table[i-1][l]+1 : table[i][j];	
				}
			}
		}

		solution = 10000;
		for(int i=1; i<=S; i++)
		{
			solution = (table[Q][i] < solution)? table[Q][i] : solution;
		}
		fout << "Case #" << k << ": " << solution << endl;
	}

	fin.close();
	fout.close();

	return 0;
}