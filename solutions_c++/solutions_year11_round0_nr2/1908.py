
#include <iostream>
#include <set>

using namespace std;

int C, D;
char c[100][5];
char d[100][5];


char check_invocation(char c1, char c2)
{
	for (int i = 0; i < C; i++)
	{
		if ((c[i][0] == c1 && c[i][1] == c2) || (c[i][1] == c1 && c[i][0] == c2)) return c[i][2];
	}
	return 0;
}

bool check_clearance(char *str, int len)
{
	set<char> s;

	for (int i = 0; i < len; i++) s.insert(str[i]);

	for (int i = 0; i < D; i++)
	{
		if (s.find(d[i][0]) != s.end() && s.find(d[i][1]) != s.end()) return true;
	}
	return false;
}

int main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		int N, len;
		char n[1000], r[1000];

		cin >> C;
		for (int j = 0; j < C; j++) cin >> c[j];

		cin >> D;
		for (int j = 0; j < D; j++) cin >> d[j];

		cin >> N;
		cin >> n;

		len = 0;
		for (int j = 0; j < N; j++)
		{
			r[len] = n[j];
			len++;

			if (len >= 2)
			{
				char c = check_invocation(r[len-1], r[len-2]);
				if (c != 0)
				{
					len--;
					r[len-1] = c;
				}

				if (check_clearance(r, len))
				{
					len = 0;
				}
			}
		}

		cout << "Case #" << (i+1) << ": [";
		for (int j = 0; j < len; j++)
		{
			cout << r[j];
			if (j != len-1) cout << ", ";
		}
		cout << "]" << endl;
	}
}
