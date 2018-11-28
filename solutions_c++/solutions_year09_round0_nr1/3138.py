#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Words
{
	private:
	string word;
	bool isGood;

	public:
	Words(string);
	string getString(){ return word; }
	void setIsGood(bool);
	bool getIsGood(){ return isGood; }
	bool inString(string,int);
	bool inStringChar(char,int);
};

int numOfGood(int size, Words **words)
{
	int a = 0;
	for(int i = 0; i < size; i++)
	{
		if(words[i]->getIsGood() == true)
		{
			a++;
		}
	}
	return a;
}

int decode(int size,Words **words, string str, int wordSize)
{

	bool END = false;
	int bracketStart=0;
	int bracketStop=0;
	bool BRACKET = false;
	int j;

		for(int i = 0; i < size; i++)
		{
			words[i]->setIsGood(true);
		}


		for(int i = 0, j = 0; i < str.length(); i++)
		{
			if(str.at(i) == '(')
			{
				bracketStart = i;
				BRACKET = true;

			}
			else if(str.at(i) == ')')
			{
				bracketStop = i;
				BRACKET = false;
				string s = str.substr(bracketStart+1, bracketStop-1-bracketStart);

				for(int k = 0; k < size; k++)
				{
					if(!words[k]->inString(s,j))
					{
						words[k]->setIsGood(false);
					}
				}
				j++;
			}
			else if(!BRACKET)
			{
				for(int k = 0; k < size; k++)
				{
					if(!words[k]->inStringChar(str.at(i),j))
					{
						words[k]->setIsGood(false);
					}
				}
				j++;
			}

		}


	return numOfGood(size, words);


}



int main(void)
{
	int L, D, N;

	scanf("%d %d %d", &L, &D, &N);


	Words *words[D];
	string line[N];

	for(int i = 0; i < D; i++)
	{
		string str;
		cin >> str;
		words[i] = new Words( str );
	}

	for(int i = 0; i < N; i++)
	{
		cin >> line[i];
	}


	for(int i = 0; i < N; i++)
	{
		cout << "Case #" << i+1 << ": " << decode(D, words, line[i], L) << endl;
	}


return 0;

}

Words::Words(string str)
{
	word = str;
	isGood = true;
}
void Words::setIsGood(bool a)
{
	isGood = a;
}

bool Words::inString(string str, int pos)
{
	int k = 0;


	for(int i = 0; i < str.length(); i++)
	{
		if(word.at(pos) != str.at(i))
		k++;
	}

	if(k == str.length())
	{
		return 0;
	}
	else
	{
		return 1;
	}

}

bool Words::inStringChar(char c, int pos)
{
	if(word.at(pos) == c)
	return true;
	else
	return false;
}

