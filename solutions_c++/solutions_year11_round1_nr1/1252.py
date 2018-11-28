#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>


using namespace std;

int N, PD, PG;

int main()
{
	int Ncase;
	freopen("a_small.in", "r", stdin);
	freopen("a_small.out", "w", stdout);
	cin >> Ncase;
	for (int run = 0; run < Ncase; ++run)
	{
		cin >> N >> PD >> PG;
		if (PG == 0 && PD > 0 || PG == 100 && PD < 100)
		{
			cout << "Case #" << run+1 << ": " << "Broken" << endl;
			continue;
		}
		int tmp = 100;
		while (true)
		{
			if (PD % 2 == 0 && tmp % 2 == 0)
			{
				PD = PD / 2;
				tmp = tmp / 2;
			}
			else break;
		}
		while (true)
		{
			if (PD % 5 == 0 && tmp % 5 == 0)
			{
				PD = PD / 5;
				tmp = tmp / 5;
			}
			else break;
		}
		if (tmp <= N)
			cout << "Case #" << run+1 << ": " << "Possible" << endl;
		else
			cout << "Case #" << run+1 << ": " << "Broken" << endl;
	}
}
