#include <cstdlib>
#include <cctype>
#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <assert.h>

using namespace std;

bool isDone(string s)
{
	for(int c=0;c<s.size();c++)
	{
		if(s[c]=='_')
		{
			return false;
		}
	}
	return true;
}

bool match(string test, string guess)
{
	if(test.size()!=guess.size())
	{
		return false;
	}
	for(int c=0;c<test.size();c++)
	{
		if(guess[c]=='_')
		{
			continue;
		}
		if(test[c]!=guess[c])
		{
			return false;
		}
	}
	return true;
}

int main()
{
	ifstream cin("C:\\Users\\Bryan\\Desktop\\TestFile.in");
	ofstream cout("C:\\Users\\Bryan\\Desktop\\Output.txt");

	int T;
	cin >> T;

	for(int counter=1;counter<=T;counter++)
	{
		cout << "Case #" << counter << ":";

		int N,M;
		cin >> N >> M;
		vector<string> word;
		for(int c=0;c<N;c++)
		{
			string i;
			cin >> i;
			word.push_back(i);
		}
		vector<string> letter;
		for(int c=0;c<M;c++)
		{
			string i;
			cin >> i;
			letter.push_back(i);
		}

		for(int c=0;c<letter.size();c++)
		{
			vector<int> numG;
			for(int n=0;n<word.size();n++)
			{
				string guess="";
				for(int x=0;x<word[n].size();x++)
				{
					guess+="_";
				}

				int current=0;
				int guesses=0;
				while(!isDone(guess))
				{
					vector<string> possible;
					for(int x=0;x<word.size();x++)
					{
						if(match(word[x],guess))
						{
							bool invalid=false;
							for(int i=0;i<word[x].size();i++)
							{
								for(int j=0;j<current;j++)
								{
									if(word[x][i]==letter[c][j] && guess[i]!=letter[c][j])
									{
										invalid=true;
										break;
									}
								}
								if(invalid)
								{
									break;
								}
							}
							if(!invalid)
							{
								possible.push_back(word[x]);
							}
						}
					}

					bool willTry=false;
					for(int x=0;x<possible.size();x++)
					{
						for(int i=0;i<possible[x].size();i++)
						{
							if(possible[x][i]==letter[c][current])
							{
								willTry=true;
								break;
							}
						}
						if(willTry)
						{
							break;
						}
					}

					if(willTry)
					{
						bool inWord=false;
						for(int x=0;x<word[n].size();x++)
						{
							if(word[n][x]==letter[c][current])
							{
								guess[x]=word[n][x];
								inWord=true;
							}
						}

						if(!inWord)
						{
							guesses++;
						}
					}
					current++;
				}
				numG.push_back(guesses);
			}

			int ans=0;
			for(int c=0;c<numG.size();c++)
			{
				if(numG[c]>numG[ans])
				{
					ans=c;
				}
			}

			cout << ' ' << word[ans];
		}

		cout << '\n';		
	}

	return 0;
}