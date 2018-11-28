#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;


bool FindWord(string strWord, vector <string> pattern)
{
	for (int i = 0; i < strWord.length(); i ++)
	{
		if (pattern[i].find(strWord[i]) == string::npos)
			return false;
	}
	return true;
}

vector <string> Decrypt(string s)
{
	vector <string> maxpattern;
	string Temp;
	for (int i = 0; i < s.length(); i++)
	{
		Temp = "";
		if (s[i] == '(')
		{
			i++;
			while (s[i] != ')')
			{
				Temp = Temp + s[i];
				i++;
			}
			maxpattern.push_back(Temp);
		
		}
		else
        {
            maxpattern.push_back(s.substr(i,1));
        }
	}
	return maxpattern;
}



int main()
{
	
    
    int L, D, N;

    vector <string> dictonary;
	vector <vector<string> > pattern;
	
	ifstream fin ("A-large.in");
	ofstream fout ("A-large.out");
    
    fin >> L >> D >> N;
	
	string Temp;
	
    for (int i = 0; i < D; i++)
	{
		fin >> Temp;
		dictonary.push_back(Temp);
	}

	for (int i = 0; i < N; i ++)
	{
		fin >> Temp;
		pattern.push_back(Decrypt(Temp));
	}

	for (int tcase = 0; tcase < N; tcase++)
	{
		int count = 0;
		for (int j = 0; j < D; j++)
		{
			if(FindWord(dictonary[j], pattern[tcase]))
				count++;
		}

		fout << "Case #" << tcase + 1 << ": " << count << endl;
	}
	return 0;
}
