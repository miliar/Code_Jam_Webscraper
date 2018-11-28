// codejam2009_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int _tmain(int argc, _TCHAR* argv[])
{
	int count = 0;
	ifstream inFile;
	ofstream outFile;

	inFile.open("A-large.in");
	if (!inFile) {
		cout << "Unable to open file";
		exit(1); 
	}

	outFile.open("out.txt");
	if (!outFile)
	{
		cout << "Unable to open file.";
		exit(1);
	}
	
	char str[2000];
	int lines = 0;
	int L,D,N;
	vector<string> v,test;
	while (!inFile.eof())
	{
		inFile.getline(str,2000);
		lines++;
		
		if (lines == 1)
		{
			string str2(str);

			size_t found = 0;
			size_t pos = 0;
			found = str2.find_first_of(' ');
			while (found != string::npos)
			{
				string tmp;
				tmp = str2.substr(pos,found);
				L = atoi(tmp.c_str());
				cout << L << endl;				
				
				pos = found;
				found = str2.find_first_of(' ',found+1);
				tmp = str2.substr(pos,found);
				D = atoi(tmp.c_str());
				cout << D << endl;

				pos = found;
				found = str2.find_first_of(' ',found+1);
				tmp = str2.substr(pos,found);
				N = atoi(tmp.c_str());
				cout << N << endl;
			}
		}
		else if (lines <= D+1)
		{
			v.push_back(str);
		}
		else
			test.push_back(str);
	}

	for (int i = 0; i < N; i++)
	{
		string str_t = test[i];
		int len = str_t.length();

		string str_c;
		str_c.resize(L);
		int index = 0;
		vector<string> words;
		string tmp;
		size_t found;
		int p = 0;
	
		for (int j = 0; j < len; j++)
		{
			switch (str_t[j])
			{
			case '(':
				found = str_t.find_first_of(')',j);
				tmp = str_t.substr(j+1,found-1-j);
				words.push_back(tmp);
				j = found;
				str_c[index++] = '$';							
				break;	
			case ')':
				break;
			default:
				str_c[index++] = str_t[j];
				break;
			}
		}

		for (int k = 0; k < D; k++)
		{
			int t;
			vector<string>::iterator it = words.begin();
			for (t = 0; t < L; t++)
			{				
				if (str_c[t] == '$')
				{
					string str_tmp = *it;
					if (str_tmp.find_first_of(v[k][t]) != string::npos)
					{
						it++;
						continue;
					}
					else
						break;
				}
				else
				{
					if (str_c[t] == v[k][t])
					{
						continue;
					}
					else
						break;
				}
			}

			if (t == L)
			{
				count++;
			}		
		}

		//cout << "count = " << count << endl;
		outFile << "Case #" << i+1 << ": " << count << endl;
		count = 0;
		str_c.clear();
		str_c.resize(L);
		words.clear();
		words.resize(0);	
	}

	inFile.close();
	outFile.close();

	return 0;
}

