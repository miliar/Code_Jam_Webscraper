
#include <cstdio>
#include <iostream>
#include <fstream>

#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <set>
#include <list>
#include <queue>
#include <string>

using namespace std;

ifstream file_in("input.txt");
ofstream file_out("output.txt");

void TestCase();

int main()
{
	int n;
	file_in >> n;

	for (int i = 1; i <= n; i++)
	{
		file_out << "Case #" << i << ": ";
		TestCase();
		file_out << endl;
	}
}

void DoWork(vector<vector<int>> &table, int p, int i, int n0, int n1, int n2)
{
	int max_n = max(n0, max(n1, n2));
	int min_n = min(n0, min(n1, n2));
	
	if (min_n < 0 || max_n > 30)
	{
		return;
	}

	bool surprising = (max_n - min_n) == 2;
	int a = max_n >= p ? 1 : 0;

	int s = table[0].size() - 1;
	
	int k = surprising ? 1 : 0;
	for (; k <= s; k++)
	{
		if (surprising)
		{
			table[i][k] = max(table[i][k], table[i - 1][k - 1] + a);
		}
		else
		{
			table[i][k] = max(table[i][k], table[i - 1][k] + a);
		}
	}
}

void TestCase()
{
	int n, s, p;
	file_in >> n >> s >> p;

	vector<int> score(n + 1);
	
	for (int i = 1; i <= n; i++)
	{
		file_in >> score[i];
	}
	
	vector<vector<int>> table(n + 1, vector<int>(s + 1, 0));

	for (int i = 1; i <= n; i++)
	{
		int remainder = score[i] % 3;
		int b = score[i] / 3;

		switch(remainder)
		{
		case 0:
			DoWork(table, p, i, b, b, b);
			DoWork(table, p, i, b - 1, b, b + 1);
			break;
		case 1:
			DoWork(table, p, i, b, b, b + 1);
			DoWork(table, p, i, b - 1, b - 1, b + 1);
			break;
		case 2:
			DoWork(table, p, i, b, b + 1, b + 1);
			DoWork(table, p, i, b, b, b + 2);
			break;
		}
	}

	file_out << table[n][s];
}
