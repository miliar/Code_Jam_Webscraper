#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
using namespace std;

int main()
{
	int L, D, N, i;
	vector <string> words;
	string s;

	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> L >> D >> N;

	words.resize(D);

	for (i=0; i<D; i++)
		cin >> words[i];
	
	bool pattern[17][27];
	for (i=0; i<N; i++)
	{
		bool nawias = false;
		int pos = 0, res=0;

		cin >> s;
		memset(pattern, 0, sizeof(pattern));

		for (string::size_type j=0; j<s.size(); j++)
		{
			if (s[j] == '(')
				nawias = true;
			else if (s[j] == ')') {
				nawias = false;
				pos++;
			} else {
				pattern[pos][s[j]-'a'] = true;
				if (!nawias)
					pos++;
			}
		}

		for (int j=0; j<D; j++)
		{
			bool ok = true;

			for (int k=0; k<L; k++)
				if (!pattern[k][words[j][k]-'a']) {
					ok = false;
					break;
				}

			if (ok)
				res++;
		}

		cout << "Case #" << i+1 << ": " << res << "\n";
	}
}
