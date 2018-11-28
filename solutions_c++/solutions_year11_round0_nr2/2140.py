#include <iostream>
#include <vector>
#include <deque>
#include <cstring>

using namespace std;

char comb[50][2];
char prod[50];
int dest[50][26];

int freq[26];
int c, d;

void do_reactions(deque<char> &invoke)
{
	bool changes;
	do {
		if (invoke.size() < 2)
			break;
	
		char a = invoke[invoke.size()-2], b = invoke[invoke.size()-1];
		
		changes = false;
		for (int i = 0; i < c; i++)
		{
			if ((comb[i][0] == a && comb[i][1] == b)||(comb[i][1] == a && comb[i][0] == b))
			{
				freq[a-'A']--; freq[b-'A']--;
				invoke.pop_back();
				freq[prod[i]-'A']++;
				invoke[invoke.size()-1] = prod[i];
				changes = true;
				break;
			}
		}
	} while (changes);
	
	if (invoke.size() > 1)
	{
		for (int i = 0; i < d; i++)
		{
			bool clean = true;
			for (int j = 0; j < 26; j++)
				if (dest[i][j] && freq[j] == 0)
				{
					clean = false;
					break;
				}
				
			if (clean)
			{
				memset(freq, 0, sizeof freq);
				invoke.clear();
				break;
			}
		}
	}
}

int main()
{
	int T, n;
	cin >> T;
	
	for (int t = 1; t <= T; t++)
	{
		memset(dest, 0, sizeof dest);
		cin >> c;
		
		for (int i = 0; i < c; i++)
		{
			char e, f, g;
			cin >> e >> f >> g;
			comb[i][0] = e;
			comb[i][1] = f;
			prod[i] = g;
		}
		
		cin >> d;
		for (int i = 0; i < d; i++)
		{
			char e, f;
			cin >> e >> f;
			dest[i][e - 'A']++;
			dest[i][f - 'A']++;
		}

		cin >> n;
		deque<char> invoke;
		memset(freq, 0, sizeof freq);
		for (int i = 0; i < n; i++)
		{
			char el; 
			cin >> el;
			freq[int(el - 'A')]++;
			invoke.push_back(el);
			do_reactions(invoke);

		}
		
		cout << "Case #" << t << ": [";
		if (invoke.size())
		{
			cout << invoke[0];
			for (int i = 1; i < invoke.size(); i++)
				cout << ", " << invoke[i];
		}
		cout << "]" << endl;
	}
}
