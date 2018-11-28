/* Rob Keim
    Google Code Jam
	 Online Round 1 */

#include <algorithm>
#include <cassert>
#include <cmath>
#include <deque>
#include <fstream>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define FOR(i, a, b) for (int i = a; i < b; i++)
#define REP(i, n) FOR(i, 0, n)

	vector<int> v1;
	vector<int> v2;

bool prime(int x)
{
	if (x % 2 == 0)
	{
		return 0;
	}
	for (int i = 3; i * i <= x; i += 2)
	{
		if (x % i == 0)
		{
			return 0;
		}
	}
	return 1;
}

void factor(int num, int asdf)
{
	if (prime(num))
	{
		if (asdf == 1)
		{
			v1.push_back(num);
			return;
		}
		if (asdf == 2)
		{
			v2.push_back(num);
			return;
		}
	}
	if (num % 2 == 0)
	{
		if (asdf == 1)
		{
			v1.push_back(2);
			factor(num / 2, 1);
			return;
		}
		if (asdf == 2)
		{
			v2.push_back(2);
			factor(num / 2, 2);
			return;
		}
	}
	for (int i = 3; i * i <= num; i += 2)
	{
		if (num % i == 0)
		{
			if (prime(i))
			{
				if (asdf == 1)
				{
					v1.push_back(i);
					factor(num / i, 1);
					return;
				}
				if (asdf == 2)
				{
					v2.push_back(i);
					factor(num / i, 2);
					return;
				}
			}
			else
			{
				if (asdf == 1)
				{
					factor(i, 1);
					factor(num / i, 1);
					return;
				}
				if (asdf == 2)
				{
					factor(i, 2);
					factor(num / i, 2);
					return;
				}
			}
		}
	}
	return;
}

int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		cout << "\tUSAGE: Program In Out\n";
		exit(1);
	}
	ifstream fin (argv[1]);
	ofstream fout (argv[2]);
	assert(fin != NULL);

	int x;
	fin >> x;
	int setNum[1001];

	REP(zzz, x)
	{
		int A, B, P;
		fin >> A >> B >> P;
						int ctr = 1;
				for (int i = A; i <= B; i++)
				{
					setNum[i] = ctr;
					ctr++;
				}
		for (int j = A; j <= B; j++)
		{
			for (int k = A; k <= B; k++)
			{
				v1.clear();
				v2.clear();
				factor(j, 1);
				factor(k, 2);
				sort(v1.begin(), v1.end());
				sort(v2.begin(), v2.end());
				//cout << j << " = ";
				for (int i = 0; i < v1.size(); i++)
				{
					//cout << v1.at(i) << " ";
				}
				//cout << endl;
				//cout << k << " = ";
				for (int i = 0; i < v2.size(); i++)
				{
					//cout << v2.at(i) << " ";
				}
				//cout << endl;
				bool common = 0;
				for (int i = 0; i < v1.size(); i++)
				{
					if (common)
					{
						break;
					}
					for (int j = 0; j < v2.size(); j++)
					{
						if ((v1.at(i) == v2.at(j)) && (v1.at(i) >= P))
						{
							common = 1;
							break;
						}
					}
				}
				//cout << "Common: " << common << endl;
				if (common)
				{
					setNum[k] = setNum[j];
				}

			}
		}
		for (int i = A; i <= B; i++)
		{
			//cout << setNum[i] << " ";
		}
		bool ans[10000];
		for (int i = 0; i <= B; i++)
		{
			ans[i] = 0;
		}
		for (int i = A; i <= B; i++)
		{
			ans[setNum[i]] = 1;
		}
		int unique = 0;
		for (int i = 0; i <= B; i++)
		{
			if (ans[i])
			{
				unique++;
			}
		}
		//cout << endl;

		cout << "Case #" << (zzz + 1) << ": " << unique << endl;
		fout << "Case #" << (zzz + 1) << ": " << unique << endl;
	}

	return 0;
}
