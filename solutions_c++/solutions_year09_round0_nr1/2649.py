#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int L, D, N;
	fin >> L >> D >> N;
	char** dic = new char*[D];
	for (int i=0; i<D; i++)
	{
		dic[i] = new char[L];
		for (int j=0; j<L; j++)
		{
			fin>>dic[i][j];
		}
	}
	
	for (int i=0; i<N; i++)
	{
		int count = 0;
		string word;
		fin >> word;
		//slice the word
		char** wordslice = new char*[L];
		for (int j=0; j<L; j ++)
		{
			wordslice[j] = new char[256];
		}
		int s_length = 0;
		int l_count = 0;
		for (int j=0; j<word.length();)
		{
			if(word[j]=='(')
			{
				j++;
				while(word[j]!=')')
				{
					wordslice[s_length][l_count] = word[j];
					l_count++;
					j++;
				}
				j++;
				s_length++;
				l_count = 0;
			}
			else
			{
				wordslice[s_length][l_count] = word[j];
				s_length++;
				j++;
			}
		}

		/*for (int j=0; j<L; j++)
		{
			for (int k=0; k<strlen(wordslice[j]); k++)
			fout << wordslice[j][k];
			fout << "\n";
		}
		fout << "\n";*/
		
		
		//find dictionarys in words
		for (int j=0; j<D; j++)
		{
			bool exist = true;
			for (int k=0; k<L; k++)
			{
				char * pch2 = strchr(wordslice[k], dic[j][k]);
				if(pch2 == NULL)					
				{
					exist = false;
					break;
				}
			}
			if (exist == true) count++;
		}

		fout << "Case #" << i+1 << ": " << count << "\n";
	}

	return 0;
}
