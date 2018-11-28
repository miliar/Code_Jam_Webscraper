#include <fstream>
#include <string>
using namespace std;

const int MOD = 10000;

long long counter[1000];
long long extra[1000];
bool score[1000];
string fraze = "welcome to code jam";

string Format(long long num)
{
	num %= MOD;
	string res(4, '0');
	int start = 1000;
	for (int i = 0; i < 4; i++)
	{
		res[i] = (char)(num / start + '0');
		num %= start;
		start /= 10;
	}
	return res;
}

int main()
{
	ifstream fin("data.txt");
	ofstream fout("result.txt");
	int N = 0;
	fin >> N;
	fin.ignore();
	string word;
	int count = 0;
	for (int i = 0; i < N; i++)
	{
		memset(&counter, 0, sizeof(counter));
		getline(fin, word);
		count = 0;
		for (int j = 0; j < (int)word.size(); j++)
		{
			if (word[j] == fraze[0])
				count++;
			counter[j] = count;
		}
		for (int j = 1; j < (int)fraze.size(); j++)
		{
			memset(&extra, 0, sizeof(extra));
			for (int k = 1; k < (int)word.size(); k++)
			{
				if (word[k] == fraze[j] && counter[k] > 0)
				{
					extra[k] = counter[k] + extra[k - 1];
				}
				else
				{
					extra[k] = extra[k - 1];
				}
				extra[k] %= MOD;
				
			}

			if (j != (int)fraze.size() - 1)
			{
				for (int s = 0; s < 1000; s++)
				{
					counter[s] = extra[s];
				}
			}

			for (int k = 0; k < 1000; k++)
			{
				if (k > 0 && counter[k] == 0 && counter[k - 1] != 0)
				{
					counter[k] = counter[k - 1];
				}
			}
		}
		long long sum = 0;

		fout << "Case #" << i + 1 << ": " << Format(extra[word.size() - 1]) << endl;
	}
	fout.close();
	return 0;
}