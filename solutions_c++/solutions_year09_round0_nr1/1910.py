#include <iostream>
#include <string>
#include <vector>

using namespace std;
typedef long long int64;

bool match(vector<string> letters, string word);

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("outlarge.txt", "w", stdout);

	int64 l, d, n;
	vector<string> words;
	string pat;

	cin >> l >> d >> n;

	for (int i=0; i<d; i++) //woorden inlezen
	{
		string t;
		cin >> t;
		words.push_back(t);
	}
	
	for (int k=0; k<n; k++) //patterns overlopen
	{
		int64 count=0;
		cin >> pat;

		vector<string> letters;

		for (int i=0; i<pat.length(); i++) //pattern scheiden
		{
			string t="0";

			if (pat[i]!='(')
			{
				t[0]=pat[i];
				letters.push_back(t);
			}
			else
			{
				int end=pat.find(')', i+1);
				string subst=pat.substr(i,end-i+1);
				letters.push_back(subst);

				i=end;
			}
		}

		for (int j=0; j<d; j++) //woorden overlopen
		{
			if (letters.size()==words[j].size())
			{
				if (match(letters, words[j])==true)
					count++;
			}
		}

		cout << "Case #" << k+1 << ": " << count << endl;
	}

	return 0;
}

bool match(vector<string> letters, string word)
{
	int64 aantal=letters.size();

	for (int i=0; i<aantal; i++)
	{
		bool m=false;

		for (int j=0; j<letters[i].size(); j++)
		{
			if (letters[i][j] == word[i])
				m=true;
		}

		if (m==false)
			return false;
	}

	return true;
}