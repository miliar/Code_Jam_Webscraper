#include <iostream>
#include <fstream>
#include <cmath>
#include <list>
#include <string>
#include <iomanip>

using namespace std;

void AlienLanguage();

void Watersheds();
int findSink(int i, int j, int numBasins, int W, int H);
int alts[100][100], basins[100][100];

void WelcomeToCodeJam();

int main()
{
//	AlienLanguage();
//	Watersheds();
	WelcomeToCodeJam();

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

void Watersheds()
{

	ifstream in("B-large.in");
	ofstream out("B-large.out");
	
	int T;
	in >> T;

	int H, W;

	for (int t = 1;t <= T;t++)
	{
		in >> H >> W;
		int numBasins = 0;
		//int basins[100][100], alts[100][100];
		for (int i = 0;i < H;i++)
		{
			for (int j = 0;j < W;j++)
			{
				in >> alts[i][j];
				basins[i][j] = -1;
			}
		}

		for (int i = 0;i < H;i++)
		{
			for (int j = 0;j < W;j++)
			{
				basins[i][j] = findSink(i,j,numBasins, W, H);
				if (basins[i][j] == numBasins) numBasins++;
			}
		}

		out << "Case #" << t << ":" << endl;
		for (int i = 0;i < H;i++)
		{
			for (int j = 0;j < W;j++)
			{
				out << (char)((int)'a'+basins[i][j]) << " ";
			}
			out << endl;
		}
	}
}

int findSink(int i, int j, int numBasins, int W, int H)
{
	if (basins[i][j] != -1) return basins[i][j];
	
	int minAlt = alts[i][j];
	int minDir = 0;
	//0 = this
	//1 = north
	//2 = west
	//3 = east
	//4 = south

	if (i != 0 && alts[i-1][j] < minAlt)//north is lowest
	{
		minAlt = alts[i-1][j];
		minDir = 1;
	}
	if (j != 0 && alts[i][j-1] < minAlt)//west is lowest
	{
		minAlt = alts[i][j-1];
		minDir = 2;
	}
	if (j != W-1 && alts[i][j+1] < minAlt)//east is lowest
	{
		minAlt = alts[i][j+1];
		minDir = 3;
	}
	if (i != H-1 && alts[i+1][j] < minAlt)//south is lowest
	{
		minAlt = alts[i+1][j];
		minDir = 4;
	}

	if (minDir == 0)
	{
		basins[i][j] = numBasins;
		return numBasins;
	}
	else if (minDir == 1)
	{
		return (basins[i][j] = findSink(i-1,j,numBasins, W, H));
	}
	else if (minDir == 2)
	{
		return (basins[i][j] = findSink(i,j-1,numBasins, W, H));
	}
	else if (minDir == 3)
	{
		return (basins[i][j] = findSink(i,j+1,numBasins, W, H));
	}
	else if (minDir == 4)
	{
		return (basins[i][j] = findSink(i+1,j,numBasins, W, H));
	}
	return -1;
}

void WelcomeToCodeJam()
{

	ifstream in("C-small-attempt0.in");
	ofstream out("C-small.out");

	int N;
	in >> N;

	char c = in.get();

	string phrase = "welcome to code jam";
	int phraseLen = 19;//number of chars in phrase

	char line[510], modLine[510];
	int len, ctr1;

	int numStrs[510][20];
	for (int i = 0;i < 510;i++)
		numStrs[i][19] = 1;

	for (int n = 1;n <= N;n++)
	{
		len = 0;
		while(true)
		{
			c = in.get();
			if ((c >= 'a' && c <= 'z') || c == ' ')
				line[len++] = c;
			else
				break;
		}
		line[len] = '\0';

		ctr1 = 0;
		for (int i = 0;i < len;i++)
		{
			if (ctr1 == 0 && line[i] != 'w')
			{
				continue;
			}
			else if (phrase.find(line[i],0) != string::npos)
			{
					modLine[ctr1++] = line[i];
			}
		}
		modLine[ctr1] = '\0';

		for (int i = 0;i < phraseLen;i++)
			numStrs[ctr1][i] = 0;

		cout << line << endl << " " << modLine << endl;
		for (int j = phraseLen-1;j >= 0;j--)
		{		
			for (int i = ctr1-1;i >= 0;i--)
			{
				if (phrase[j] == modLine[i])
				{
					numStrs[i][j] = (numStrs[i+1][j] + numStrs[i+1][j+1]) % 1000;
				}
				else
				{
					numStrs[i][j] = numStrs[i+1][j] % 1000;
				}
			}
		}
		cout << "Case #" << n << ": ";
		cout << setw(4) << setfill('0') << numStrs[0][0] << endl;

		out << "Case #" << n << ": ";
		out << setw(4) << setfill('0') << numStrs[0][0] << endl;
	}
}