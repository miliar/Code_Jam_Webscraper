#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <fstream>
using namespace std;

typedef map<char, set<string> > mymap;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int L, D, N;
	fin >> L >> D >> N;

	mymap tempM;
	vector<mymap > lookup(L);
	for (int i = 0; i < L; ++i)
		lookup[i] = tempM;
	
	for (int i = 0; i < D; ++i)
	{
		string line;
		fin >> line;

		int len = line.size();
		for (int j = 0; j < len; ++j)
		{
			mymap::iterator it = lookup[j].find(line[j]);
			if (it == lookup[j].end())
			{
				set<string> v;
				v.insert(line);
				lookup[j].insert(make_pair(line[j], v));
			}
			else
			{
				//it->second.push_back(line);
				it->second.insert(line);
			}
		}
	}

	for (int i = 1; i <= N; ++i)
	{
		//Loop over test cases
		string word;
		fin >> word;
		int wordLen = word.size();

		//TODO: Fix me
//		cout << word << endl;

		int index = 0;
		bool inParens = false;
		vector<vector<char> > forms(L);
		vector<char> v;
		for (int j = 0; j < L; ++j)
		{
			forms[j] = v;
		}
		for (int c = 0; c < wordLen; ++c)
		{
			if (word[c] == '(')
				inParens = true;
			else if (word[c] == ')')
			{
				inParens = false;
				++index;
			}
			else
			{
				forms[index].push_back(word[c]);
				if (!inParens)
					++index;
			}
		}

		set<string> allMatches;
		set<string> allMatches2;
		set<string> *ptrAllMatches = &allMatches;
		set<string> *ptrAllMatches2 = &allMatches2;
		set<string> * tmp;
		for (int j = 0; j < L; ++j)
		{
			//Loop over each index

			set<string> matches;

			int numChars = forms[j].size();
			for (int k = 0; k < numChars; ++k)
			{
				char c = forms[j][k];
				mymap::iterator it = lookup[j].find(c);
				if (it != lookup[j].end())
				{
					matches.insert(it->second.begin(), it->second.end());
					//for (set<string>::iterator it2 = it->second.begin(); it2 != it->second.end(); it2++)
					//	matches.insert(*it2);
				}
			}
			if (j == 0)
				*ptrAllMatches = matches;
			else
			{
				//allMatches = array_intersect(allMatches, matches);
				//set_intersection(ptrAllMatches->begin(), ptrAllMatches->end(), matches.begin(), matches.end(), ptrAllMatches2->end());
				ptrAllMatches2->clear();
				for (set<string>::iterator it = matches.begin(); it != matches.end(); it++)
				{
					set<string>::iterator it2 = ptrAllMatches->find(*it);
					if (it2 != ptrAllMatches->end())
						ptrAllMatches2->insert(*it);
				}

				//Swap ptrs
				tmp = ptrAllMatches;
				ptrAllMatches = ptrAllMatches2;
				ptrAllMatches2 = tmp;
			}
		}

		unsigned int num = ptrAllMatches->size();
//		cout << num << endl;
		cout << "Case #" << i << ": " << num << endl;
		fout << "Case #" << i << ": " << num << endl;

	}

}