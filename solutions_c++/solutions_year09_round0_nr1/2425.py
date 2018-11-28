#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <cstdlib>
using namespace std;

int main()
{
	const string FILENAME = "C:\\CodeJam\\Aliens\\A-large.in";
	//const string FILENAME = "C:\\CodeJam\\Aliens\\test-in.txt";
	ifstream inFile(FILENAME.c_str());
	ofstream outFile((FILENAME + ".out.txt").c_str());

	unsigned int l, d, n;
	inFile >> l >> d >> n;
	inFile.ignore();

	vector<string> words;
	for (unsigned int i = 0; i < d; i++)
	{
		string word;
		getline(inFile, word);
		words.push_back(word);
	}

	for (unsigned int caseId = 1; caseId <= n; caseId++)
	{
		int matches = 0;
		string testCase;
		getline(inFile, testCase);

		for (unsigned int wordIndex = 0; wordIndex < words.size(); wordIndex++)
		{
			string& word = words[wordIndex];

			unsigned int tI = 0, wI = 0;
			bool inBlock = false, charFoundInBlock = false;

			while (tI < testCase.size() && wI < words.size())
			{
				char& tc = testCase[tI];
				char& wc = word[wI];

				if (tc == wc)
				{
					if (inBlock)
					{
						charFoundInBlock = true;
						while (testCase[++tI] != ')');
						inBlock = false;
					}
					wI++;
				}
				else if (tc == '(')
				{
					inBlock = true;
					charFoundInBlock = false;
				}
				else if (tc == ')')
				{
					if (!charFoundInBlock)
					{
						break;
					}
					inBlock = false;
					wI++;
				}
				else if (!inBlock)
				{
					break;
				}
				tI++;
			}

			if (wI == word.size())
			{
				matches++;
			}
		}
	
		outFile << "Case #" << caseId << ": " << matches << std::endl;
	}
	return 0;
}