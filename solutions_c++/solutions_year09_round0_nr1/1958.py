#include <iostream>
#include <string>

using namespace std;

string word[6000];
string pattern;

bool match(string &w, string &p, int letter, int position)
{
	if (letter == w.length())
		return true;
	if (p[position] != '(')
	{
		if (w[letter] != p[position])
			return false;
		else
			return match(w, p, letter + 1, position + 1);
	} else
	{
		bool ok = false;
		while (p[position] != ')')
		{
			if (p[position] == w[letter])
				ok = true;
			position++;
		}
		if (!ok)
			return false;
		else
			return match(w, p, letter + 1, position + 1);
	}	
}

int main()
{
	int i, j, l, d, n, c;
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> l >> d >> n;
	for (i = 0; i < d; i++)
		cin >> word[i];
	for (i = 0; i < n; i++) 
	{
		cin >> pattern;
		c = 0;
		for (j = 0; j < d; j++)
			if (match(word[j], pattern, 0, 0))
				c++;
		cout << "Case #" << i + 1 << ": " << c << endl;
	}
	return 0;	
}
