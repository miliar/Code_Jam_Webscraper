#include <iostream>
#include <vector>

using namespace std;

char combine[26][26];
bool oppose[26][26];

void init()
{
	for (int i = 0; i < 26; ++i)
		for (int j = 0; j < 26; ++j)
		{
			combine[i][j] = '\0';
			oppose[i][j] = false;
		}
}

void show(const vector<char> &ans)
{
	cout << '[';
	bool first = true;
	for (int i = 0; i < static_cast<int>(ans.size()); ++i)
	{
		if (first)
			first = false;
		else
			cout << ", ";
		cout << ans[i];
	}
	cout << ']' << endl;
}

void solve()
{
	int c;
	cin >> c;
	for (int i = 0; i < c; ++i)
	{
		string s;
		cin >> s;
		combine[s[0] - 'A'][s[1] - 'A'] = s[2];
		combine[s[1] - 'A'][s[0] - 'A'] = s[2];
	}

	int d;
	cin >> d;
	for (int i = 0; i < d; ++i)
	{
		string s;
		cin >> s;
		oppose[s[0] - 'A'][s[1] - 'A'] = true;
		oppose[s[1] - 'A'][s[0] - 'A'] = true;
	}

	int n;
	string s;
	cin >> n >> s;
	vector<char> ans;
	for (int i = 0; i < n; ++i)
	{
		const char c = s[i];
		if (ans.empty())
		{
			ans.push_back(c);
			continue;
		}
		if (combine[c - 'A'][ans.back() - 'A'] != '\0')
		{
			ans[ans.size() - 1] = combine[c - 'A'][ans.back() - 'A'];
			continue;
		}
		bool clear = false;
		for (int j = 0; j < static_cast<int>(ans.size()); ++j)
			if (oppose[ans[j] - 'A'][c - 'A'])
			{
				ans.clear();
				clear = true;
				break;
			}
		if (!clear)	ans.push_back(c);
	}
	show(ans);
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		init();
		solve();
	}
	return 0;
}
