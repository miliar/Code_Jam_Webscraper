#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream infile("A-large.in");//Sample.in
	ofstream outfile("A-large.out");//Sample.out
	
	int L, D, N;
	infile >> L >> D >> N;
	
	char let[D][L];
	
	for (int i = 0; i < D; i++)
	{
		for (int j = 0; j < L; j++)
		{
			do {
				infile >> let[i][j];
			}while(let[i][j] < 'a' && let[i][j] > 'z');
		}	
	}
	
	bool la[L][26];
	char ch; 
	
	for (int i = 0; i < N; i++)
	{
		for (int m = 0; m < L; m++)
		{
			for (int n = 0; n < 26; n++)
			{
				la[m][n] = false;
			}	
		}
		
		int j = 0, k = 0;
		while(j < L)
		{
			do {
				infile >> ch;
			}while(ch == '\n');
			
			if (ch == '(')
			{
				infile >> ch;
				
				while (ch != ')')
				{
					la[j][ch - 'a'] = true;
					infile >> ch;
				}				
			}else
			{
				la[j][ch - 'a'] = true;	
			}
			j++;
		}
		
		int p = 0, q = 0, num = 0;
		for (p = 0; p < D; p++)
		{
			for (q = 0; q < L; q++)
			{
				if (!la[q][let[p][q] - 'a'])
				{
					break;	
				}
			}
			
			if (q == L)
			{
				num++;
			}
		}
		outfile << "Case #" << i + 1 << ": " << num << endl;
	}
	
	infile.close();
    outfile.close();
	return 0;	
}
