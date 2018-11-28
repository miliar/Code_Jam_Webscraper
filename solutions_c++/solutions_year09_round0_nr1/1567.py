#include <iostream>
#include <fstream>
#include <cmath>
#include <list>

using namespace std;

void AlienLanguage();
void Watersheds();
void WelcomeToCodeJam();

int main()
{
	AlienLanguage();
//	Watersheds();
//	WelcomeToCodeJam();

	return 0;
}

void AlienLanguage()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");

	int L, D, N;
	
	in >> L >> D >> N;

	list<char*> lang;
	lang.push_back(" ");//buffer to allow us to erase without skipping the next word

	for (int i = 0;i < D;i++)
	{
		char * langWord = (char*)malloc(15*sizeof(char));
		in >> langWord;
		lang.push_back(langWord);

	}

//----------------------------------------//
		for (list<char*>::iterator it = lang.begin();it != lang.end();it++)
			cout << *it << " ";
		cout << endl;
//----------------------------------------//

	char word[15*30];//holds up to 15 tokens of length > (26+2)

	list<char*> matches;
	char tokens[15][26];
	for (int i = 1;i <= N;i++)
	{
		matches = lang;
		in >> word;
		int ctr1 = 0;
		for (int j = 0;j < strlen(word);j++, ctr1++)
		{
			if (word[j] != '(') 
			{
				tokens[ctr1][0] = word[j];
				tokens[ctr1][1] = ')';
				continue;
			}
			int ctr2 = 0;
			while(word[++j] != ')')
				tokens[ctr1][ctr2++] = word[j];
			tokens[ctr1][ctr2] = ')';
		}

		for (int j = 0;j < L;j++)
		{
			for (list<char*>::iterator it = ++matches.begin();it != matches.end();it++)
			{
				//cout << i << " ";
				int match = false;
				int ctr = 0;
				while (tokens[j][ctr] != ')')
				{
					//cout << tokens[i][ctr] << " " << (*it)[i] << " " << ctr << endl;
					if ((*it)[j] == tokens[j][ctr])
					{					
						match = true;
						break;
					}			
					ctr++;
				}
				if (match == false)
				{
					//cout << " " << *it << " ";
					it = matches.erase(it);
					//cout << "size: " << matches.size() << endl;
					if (matches.size() != 0) it--;
				}
			}
		}
		cout << matches.size()-1 << endl;//-1 to account for the buffer
		out << "Case #" << i << ": " << matches.size()-1 << endl;
	}	
}