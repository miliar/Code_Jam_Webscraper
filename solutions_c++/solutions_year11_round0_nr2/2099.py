#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	for(int t=1; t<=T; t++)
	{
		int C;
		char comb[300][300];
		int D;
		bool op[300][300];
		int N;
		string A;
		char L[1000];
		int top = 0;
		for(int i=0; i<300; i++)
			for(int j=0; j<300; j++)
				comb[i][j] = '@';
		fin >> C;		
		for(int i=0; i<C; i++)
		{
			string s;
			fin >> s;
			comb[ s[0] ][ s[1] ] = s[2];
			comb[ s[1] ][ s[0] ] = s[2];
		}
		fin >> D;		
		for(int i=0; i<300; i++)
			for(int j=0; j<300; j++)
				op[i][j] = false;
		for(int i=0; i<D; i++)
		{
			string s;
			fin >> s;
			op[ s[0] ][ s[1] ] = true;
			op[ s[1] ][ s[0] ] = true;
		}
		fin >> N;
		fin >> A;
		for(int i=0; i<N; i++)
		{
			if(top>0)
			{
				if(comb[ A[i] ][ L[top-1] ] != '@')
				{
					L[top-1] = comb[ A[i] ][ L[top-1] ];
				}
				else
					{
						bool flag = false;
						for(int j=0; j<top; j++)
							if(op[ A[i] ][ L[j] ] == true)
							{
								flag = true;
								break;
							}
						if(flag == true)
							top = 0;
						else
						{
							L[top] = A[i];
							top++;
						}
					}
			}
			else
			{
				L[top] = A[i];
				top++;
			}
		}
		fout << "Case #" << t << ": [" ;
		for(int i = 0; i<top; i++)
		{
			fout << L[i];
			if(i!=top-1)
				fout<<", ";
		}
		fout << "]" << endl;
	}
	return 0;
}

