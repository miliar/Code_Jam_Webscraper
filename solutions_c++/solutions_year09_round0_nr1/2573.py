#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <cctype>

using namespace std;

int main()
{
  //Read in the file
  ifstream inTest;
  inTest.open("A-small3.txt");//"InputFile.txt");
  string line;

	int wordLength, numWords, numTests;

	inTest >> wordLength;
	inTest >> numWords;
	inTest >> numTests;

  //Open file for output
  ofstream outTest;
  outTest.open("result3.txt");

	vector<string> words;
	for(int i=0; i<numWords; i++)
	{
		inTest >> line;
		words.push_back(line);
	}

  for(int currTest=1; currTest <= numTests; currTest++) //Each test
  {
		vector<string> possWords = words;

		for(int spot=0; spot<wordLength; spot++) //Each letter(s) in test
		{
			bool parens = false;

			
		string nextLetters = "";

			while(1) //Get possible letters
			{			
				char temp = inTest.get();
				if(isalpha(temp))
				{
					nextLetters += temp;

					if(!parens)
						break;
				}
				else if(temp == '(')
					parens = true;
				else if(temp == ')')
					break;
			}

			for(int i=0; i<possWords.size(); i++)
				{
					if(nextLetters.find(possWords[i][spot]) == string::npos)
					{
						possWords.erase(possWords.begin() + i);
						i--;
					}
				}
		}

		outTest << "Case #" << currTest << ": " << possWords.size() << endl;
  }
  return 1;
}





/*    int numSwitches = 0;

    //Get number of search engines
    getline(inTest, line);
    cout << "-------Test " << currTest << "-------" << endl;
    cout << "Number of search engines: " << line << endl;
    int numEngines = atoi(line.c_str());

    //Capture all search engines
    vector<pair<string, bool> > engines;
    for(int currEngine=1; currEngine <= numEngines; currEngine++)
    {
      getline(inTest, line);
      engines.push_back(pair<string, bool> (line, false));
    }
    
    //Read in queries
    getline(inTest, line);
    int numQueries = atoi(line.c_str());
    for(int currQuery = 1; currQuery <= numQueries; currQuery++)
    {
      getline(inTest, line);

      //Check if all are true
      bool allTrue = true;
      for(int i=0; i < engines.size(); i++)
      {
				if(engines[i].first == line)
				{
					engines[i].second = true;
				}
				if(engines[i].second == false)
				{
					allTrue = false;
				}
      }
      if(allTrue)
      {
				for(int i=0; i< engines.size(); i++)
				{
					engines[i].second = false;
				}
				numSwitches++;
      }
    }

    outTest << "Case #" << currTest << ": " << numSwitches << endl;
		*/