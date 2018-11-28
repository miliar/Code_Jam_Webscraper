#include <iostream>
#include <string>
using namespace std;

const int MAXD = 5001;
const int MAXL = 16;

int L, D, N;
string word[MAXD];
bool used[MAXL][26];

int main()
{
	freopen("lol.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> L >> D >> N;
	for (int x=0; x<D; x++)
		cin >> word[x];

	for (int x=0; x<N; x++)
	{
		string s; cin >> s;
		memset(used, false, sizeof used);

		//parse
		int pos = 0;
		bool inbrackets = false;
		for (int a=0; a<s.size(); a++)
		{
			if (s[a] == '(')
			{
				inbrackets = true;
				continue;
			}

			if (s[a] == ')')
			{
				inbrackets = false;
				pos++;
				continue;
			}

			used[pos][s[a]-'a'] = true;

			if (!inbrackets)
				pos++;
		}

		//get ans
		int ans = 0;
		for (int a=0; a<D; a++)
		{
			bool works = true;
			for (int b=0; b<L; b++)
				if (!used[b][word[a][b]-'a'])
				{
					works = false;
					break;
				}

			if (works)
				ans++;
		}

		printf("Case #%d: %d\n", x+1, ans);
	}
}
