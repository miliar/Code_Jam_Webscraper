#include <iostream>
#include <vector>
#include <string>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

void solve_combine(const vector<string> &combine, string &result)
{
	if (result.length() <= 1) return;

	char a = result[result.length() - 2];
	char b = result[result.length() - 1];

	for (vector<string>::const_iterator i = combine.begin(); i != combine.end(); i++)
	{
		const string &com = *i;
		if ((a == com[0] && b == com[1]) ||
			(a == com[1] && b == com[0]))
		{
			// combine
			result.erase(result.length() - 1, 1);
			result[result.length() - 1] = com[2];
		}
	}
}

void solve_oppose(const vector<string> &oppose, string &result)
{
	if (result.length() <= 1) return;
	char a = result[result.length() - 1];
	for (vector<string>::const_iterator i = oppose.begin(); i != oppose.end(); i++)
	{
		const string &opp = *i;
		if (a == opp[0])
		{
			for (int j = 0; j < result.length(); j++)
			{
				if (result[j] == opp[1])
				{
					result.clear();
					return;
				}
			}
		}
		else if(a == opp[1])
		{
			for (int j = 0; j < result.length(); j++)
			{
				if (result[j] == opp[0])
				{
					result.clear();
					return;
				}
			}
		}
	}
}

void solve(const vector<string> &combine, const vector<string> &oppose, const string &invoke)
{
	string result;

	for (int i = 0; i < invoke.length(); i++)
	{
		result.append(invoke, i, 1);
		solve_combine(combine, result);
		solve_oppose(oppose, result);
	}
	cout << "[";
	for (int i = 0; i < result.length(); i++)
	{
		if (i < result.length() - 1)
		{
			cout << result[i] << ", ";
		}
		else
		{
			cout << result[i];
		}
	}
	cout << "]" << endl;
}

int main()
{
	uint64_t t;
	cin >> t;
	if (!cin) return -1;
	
	for (uint64_t i = 0; i < t; i++)
	{
		int n_combine, n_oppose, n_invoke;		

		cin >> n_combine;
		if (!cin) return -1;
		vector<string> combine(n_combine);
		for (int j = 0; j < n_combine; j++)
		{
			cin >> combine[j];
			if (!cin) return -1;
			if (combine[j].length() != 3) return -1;
		}

		cin >> n_oppose;
		if (!cin) return -1;
		vector<string> oppose(n_oppose);
		for (int j = 0; j < n_oppose; j++)
		{
			cin >> oppose[j];
			if (!cin) return -1;
			if (oppose[j].length() != 2) return -1;
		}

		cin >> n_invoke;
		if (!cin) return -1;
		string invoke;
		cin >> invoke;
		if (!cin) return -1;
		if (invoke.length() != n_invoke) return -1;

		cout << "Case #" << (i + 1) << ": ";
		solve(combine, oppose, invoke);
	}
	
}

