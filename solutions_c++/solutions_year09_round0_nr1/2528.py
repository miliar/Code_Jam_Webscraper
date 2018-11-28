/*
 * A.cpp
 *
 *  Created on: Sep 2, 2009
 *      Author: bernberg11
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main(int argc, char * argv[])
{
	int L, D, N;
	ifstream infile;
	vector<string> dictionary;
	string word;
	vector<string> candidates;
	char letter;
	vector<char> letters;
	infile.open(argv[1]);
	if (!infile)
	{
	   cout << "Invalid file name" << endl;
	   exit(1);
	}
	infile >> L >> D >> N;
	for (int i=0; i < D; i++)
	{
		infile >> word;
		dictionary.push_back(word);
	}

	for (int i=0; i < N; i++)
	{
		candidates = dictionary;
		for (int j=0; j < L; j++)
		{
			while (infile.get(letter) &&
					!(isalpha(letter) || letter == '(' || letter == ')'));
			if (letter != '(') letters.push_back(letter);
			else
			{
				while(infile.get(letter) && letter != ')')
				{
					letters.push_back(letter);
				}
			}

			for (vector<string>::iterator iter = candidates.begin(); iter != candidates.end(); )
			{

				if (find(letters.begin(),letters.end(),(*iter)[j]) == letters.end()) iter = candidates.erase(iter);
				else ++iter;
			}

			letters.clear();
		}

		cout << "Case #" << i+1 << ": " << candidates.size();
		cout << endl;
	}
	return 0;
}
