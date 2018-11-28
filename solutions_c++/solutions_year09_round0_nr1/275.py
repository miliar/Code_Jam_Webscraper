#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string words[5010];
int pattern[100];

bool isGoodWord(const string & word, int ti)
{
	if (word.length() != ti) {
		return false;
	}
	int i = 0;
	for (; i < word.length(); ++ i)
	{
		if ((pattern[i] & (1 << (word[i] - 'a'))) == 0) {
			return false;
		}
	}
	return true;
}

int calc(const string & line, int wordCount)
{
	memset(pattern, 0, sizeof(pattern));
	int ti = 0;
	for (int i = 0; i < line.length(); ++ i)
	{
		if (line[i] == '(') {
			while(line[++i] != ')') 
			{
				pattern[ti] |= (1 << (line[i] - 'a'));
			}
		} else {
			pattern[ti] |= (1 << (line[i] - 'a'));
		}
		++ ti;
	}

	int ret = 0;
	for (int i = 0; i < wordCount; ++ i)
	{
		if (isGoodWord(words[i], ti)) {
			++ ret;
		}
	}
	return ret;

}

int main()
{
	int l, d, n;
	fstream file("A-small1.in");
	fstream output("A-small.out", ios_base::out);
	file >> l >> d >> n;
	for (int i = 0; i < d; ++ i)
	{
		file >> words[i];
	}
	file.get();
	int caseIndex = 0;
	string line;
	while (++caseIndex <= n)
	{
		getline(file, line);
		output << "Case #" << caseIndex << ": " << calc(line, d) << endl;
	}

	file.close();
	output.close();
	return 0;
}