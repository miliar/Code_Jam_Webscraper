#include <iostream>
#include <string>

using namespace std;

int wordLength = 0;

bool Match(string quest, string word)
{
	int questOrder = 0;
	bool char_match = false;

	for(int i = 0; i < wordLength; i++)
	{
		if(quest[questOrder] == '(')
		{
			questOrder++;
			while(quest[questOrder] != ')')
			{
				if(quest[questOrder] == word[i])
				{
					char_match = true;
				}
				questOrder++;							
			}
			questOrder++;
		}
		else if(quest[questOrder] == word[i])
		{
			questOrder++;
			char_match = true;
		}
	
		if(char_match)
		{
			char_match = false;
		}
		else
		{
			return false;	
		}
	}
	return true;
}

int main()
{
	int wordCount = 0;
	int questCount = 0;

	cin>>wordLength>>wordCount>>questCount;

	string *word = new string[wordCount];
	string *quest = new string[questCount];

	for(int i = 0; i < wordCount; i++)
	{
		cin>>(word[i]);
	}

	for(int i = 0; i < questCount; i++)
	{
		cin>>quest[i];
	}

	int matchCount = 0;
	for(int i = 0; i < questCount; i++)
	{
		for(int j = 0; j < wordCount; j++)
		{
			if(Match(quest[i], word[j]))
			matchCount++;
		}
		cout<<"Case #"<<i+1<<": "<<matchCount<<endl;
		matchCount = 0;
	}

	delete[] word;
	delete[] quest;

	return 0;
}

