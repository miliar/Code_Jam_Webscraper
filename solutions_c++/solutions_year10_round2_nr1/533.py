#include <iostream>
#include <string>
#include <vector>

using namespace std;

int t;
int n, m;
int result;
vector<string> existed, must_exist;
int current;

int DoIt(string must, string is)
{
	int res = 0;
	bool is_good = true;

	for (int i = 0; i < (int)min(must.length(), is.length()); i++)
	{
		if (must[i] != is[i])
		{
			is_good = false;
			res--;
			break;
		}

		if (must[i] == '/')
			res++;

	}

	if (is_good)
	{
		if (is.length() > must.length())
		{
			if (is[must.length()] != '/')
				res--;
		}
		else if (is.length() < must.length())
		{
			if (must[is.length()] != '/')
				res--;
		}
	}

	return max(res, 0);
}

int All(string value)
{
	int res = 0;
	
	for (int i = 0; i < (int)value.length(); i++)
		if (value[i] == '/')
			res++;

	return res;
}

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cin >> n >> m;

		result = 0;

		existed.clear();
		must_exist.clear();

		existed.resize(n);
		must_exist.resize(m);

		for (int j = 0; j < n; j++)
			cin >> existed[j];

		for (int j = 0; j < m; j++)
			cin >> must_exist[j];

		for (int j = 0; j < m; j++)
		{
			current = 0;

			for (int u = 0; u < (int)existed.size(); u++)
			{
				current = max(current, DoIt(must_exist[j], existed[u]));
			}

			result += All(must_exist[j]) - current;
			existed.push_back(must_exist[j]);
		}



		cout << "Case #" << i + 1 << ": " << result << endl;
	}

	return 0;
}