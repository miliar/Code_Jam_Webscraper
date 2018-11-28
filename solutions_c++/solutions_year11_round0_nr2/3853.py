#include<iostream>
#include<string>
#include<string.h>
#include<list>
#include<algorithm>
#include<iterator>

using namespace std;

int main()
{
	const int nLetters = 'Z' - 'A' + 1;

	int t, c, d, n;
	char combo[nLetters][nLetters];
	char opp[nLetters];
	int  ocur[nLetters];
	string s;
	list<char> r;

	cin >> t;
	for(int i=1; i<=t; i++)
	{
		r.clear();
		memset(combo, 0xFF, sizeof(combo));
		memset(opp, 0xFF, sizeof(opp));
		memset(ocur, 0, sizeof(ocur));

		cin >> c;
		for(int j=0; j<c; j++)
		{
			cin >> s;
			combo[s[0]-'A'][s[1]-'A'] = s[2];
			combo[s[1]-'A'][s[0]-'A'] = s[2];
		}

		cin >> d;
		for(int j=0; j<d; j++)
		{
			cin >> s;
			opp[s[0] - 'A'] = s[1] - 'A';
			opp[s[1] - 'A'] = s[0] - 'A';
		}

		cin >> n >> s;
		r.push_back(s[0]);
		ocur[s[0] - 'A'] = 1;

		for(int j=1; j<n; j++)
		{
			if(combo[r.back() - 'A'][s[j] - 'A'] ^ (char)0xFF)
			{
				ocur[r.back() - 'A']--;
				r.back() = combo[r.back() - 'A'][s[j] - 'A'];
				ocur[r.back() - 'A']++;
			}
			else if(opp[s[j]-'A'] ^ (char)0xFF && ocur[opp[s[j]-'A']] > 0)
			{
				r.clear();
				memset(ocur, 0, sizeof(ocur));
				
				if(j + 1 < n)
				{
					j++;
					r.push_back(s[j]);
					ocur[s[j] - 'A'] = 1;
				}
			}
			else
			{
				ocur[s[j] - 'A']++;
				r.push_back(s[j]);
			}
		}
		cout << "Case #" << i << ": [";
		copy(r.begin(), --r.end(), ostream_iterator<char>(cout, ", "));
		if(!r.empty()) cout << r.back();
		cout << "]" << endl;	
	}
}
