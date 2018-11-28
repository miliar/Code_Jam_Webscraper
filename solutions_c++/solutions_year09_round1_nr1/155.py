#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

vector<int> bases;
int baset[9][2048];

int test(int v, int b);

int test0(int v, int b)
{
	int s = 0;
	int p = v;
	while (p > 0)
	{
		s += (p % b) * (p % b);
		p /= b;
	}
	if (v == s) return s;
	return test(s, b);
}

int test(int v, int b)
{
	if (v < 2048)
	{
		if (baset[b-2][v] >= 0) return baset[b-2][v];
		baset[b-2][v] = 0;
		return baset[b-2][v] = test0(v, b);
	}
	return test0(v, b);
}

int main()
{
	memset(baset, -1, sizeof(baset));
	string line;
	int T;
	cin >> T;
	getline(cin, line);
	for (int n = 1; n <= T; n++)
	{
		getline(cin, line);
		istringstream iss(line);
		bases.clear();
		int b;
		while (iss >> b)
		{
			bases.push_back(b);
		}
		for (int i = 2; i < 0x7fffffff; i++)
		{
			for (int j = 0; j < bases.size(); j++)
			{
				b = bases[j];
				if (test(i, b) != 1)
				{
					goto nexti;
				}
			}
			printf("Case #%d: %d\n", n, i);
			break;
nexti:
			;
		}
	}
	return 0;
}