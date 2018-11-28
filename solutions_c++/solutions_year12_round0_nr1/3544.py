#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

class Translator
{
private:
	char letterMap[26];
	int bitmap[26];
public :
	Translator(vector<string> original, vector<string> googlerese)
	{
		memset(letterMap, 0, sizeof(letterMap));
		for (int i = 0; i < original.size(); i++)
		{
			for (int j = 0; j < original[i].size(); j++)
			{
				if (original[i][j] != ' ')
				{
					if (letterMap[googlerese[i][j] - 'a'] != 0 && letterMap[googlerese[i][j] - 'a'] != original[i][j])
					{
						throw "Error";
					}

					letterMap[googlerese[i][j] - 'a'] = original[i][j];
				}
				else if (googlerese[i][j] != ' ')
				{
					throw "Error";
				}
			}
		}

		memset(bitmap, 0, sizeof(bitmap));
		for (int i = 0; i < 26; i++)
		{
			bitmap[letterMap[i] - 'a'] = 1;
		}

		char c = '\0';
		for (int i = 0; i < 26; i++)
		{
			if (bitmap[i] == 0 && c == '\0')
			{
				c = i + 'a';
			}
			else if (bitmap[i] == 0 && c != '\0')
			{
				throw "not enough data.";
			}
		}

		for (int i = 0; i < 26; i++)
		{
			if (letterMap[i] == 0 && c != '\0')
			{
				letterMap[i] = c;
				c = '\0';
			}
			else if (letterMap[i] == 0 && c == '\0')
			{
				throw "Not enough data.";
			}
		}
	}

	string translate(string googlerese)
	{
		string output = googlerese;

		for (int i = 0; i < googlerese.size(); i++)
		{
			if (googlerese[i] != ' ')
			{
				if (letterMap[googlerese[i] - 'a'] == 0)
				{
					throw "Error";
				}

				output[i] = letterMap[googlerese[i] - 'a'];
			}
		}

		return output;
	}
};

int main()
{
	string googlerese[] = {"yeq", "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string original[] = {"aoz", "our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
	Translator translator = Translator(vector<string>(original, original + 4), vector<string>(googlerese, googlerese + 4));
	int T;
	cin >> T;
	string line;

	getline(cin, line);
	for (int i = 0; i < T; i++)
	{
		getline(cin, line);
		printf("Case #%d: %s\n", i + 1, translator.translate(line).c_str());
	}
}