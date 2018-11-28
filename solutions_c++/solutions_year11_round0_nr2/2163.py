#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

int T, C, D;
char combine[400][400];
bool opposed[400][400];

stack<char> st;

char pushed[500];

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		memset(combine, 0, sizeof(combine));
		memset(opposed, 0, sizeof(opposed));
		memset(pushed, 0, sizeof(pushed));

		cin >> C;
		for (int i = 0; i < C; ++i)
		{
			string str;
			cin >> str;

			combine[str[0]][str[1]] = combine[str[1]][str[0]] = str[2];
		}

		cin >> D;
		for (int i = 0; i < D; ++i)
		{
			string str;
			cin >> str;

			opposed[str[0]][str[1]] = opposed[str[1]][str[0]] = true;
		}

		string str;
		cin >> D >> str;
		
		for (int i = 0; i < str.size(); ++i)
		{
			char toPush = str[i];

			if (!st.empty())
			{
				char top = st.top();
				
				if (combine[top][str[i]] != 0)
				{
					st.pop();
					toPush = combine[top][str[i]];
					pushed[top]--;
				}

				bool cont = false;
				for (int j = 'A'; j <= 'Z'; ++j)
					if (pushed[j] > 0 && opposed[j][toPush])
					{
						while (!st.empty())
							st.pop();
						memset(pushed, 0, sizeof(pushed));
						cont = true;
						break;
					}

				if (cont)
					continue;
			}

			st.push(toPush);
			pushed[toPush]++;
		}

		string ans = "";
		while (!st.empty())
		{
			char top = st.top();
			st.pop();

			if (ans != "")
				ans = ", " + ans;
			ans = top + ans;
		}

		cout << "Case #" << t <<": [" << ans << "]\n";
	}

	return 0;
}