#include <iostream>
#include <set>

using namespace std;

int main(int argc, char *argv[])
{
	int L, D, N;
	cin >> L >> D >> N;
	
	string words[5000];
	int scores[5000];
	
	for (int i = 0; i < D; i++)
	{
		cin >> words[i];
	}
	
	for (int i = 0; i < N; i++)
	{
		for (int n = 0; n < 5000; n++)
		{
			scores[n] = 0;
		}
		
		string w;
		cin >> w;
		
		for (int k = 0, idx = 0; k < L; k++, idx++)
		{
			set<char> letters;
			if (w[idx] != '(')
			{
				letters.insert(w[idx]);
			}
			else
			{
				idx++;
				while (w[idx] != ')')
				{
					letters.insert(w[idx]);
					idx++;
				}
			}
			for (int j = 0; j < D; j++)
			{
				if (letters.count(words[j][k]) > 0)
				{
					scores[j]++;
				}
			}
		}
		
		int matches = 0;
		for (int j = 0; j < D; j++)
		{
			if (scores[j] == L)
				matches++;
		}
		
		cout << "Case #" << i+1 << ": " << matches << endl;
	}
	
	return 0;
}
