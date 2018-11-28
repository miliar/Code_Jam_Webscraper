#include <vector>
#include <string>
#include <fstream>
#include <iostream>

using namespace std;

int Solve(vector<string> a)
{
	int ret = 0;
	for(int i = 0; i < a.size(); i++)
	{
		int pos = a[i].find_last_of('1');
		if(pos > i)
		{
			for(int j = i + 1; j < a.size(); j++)
			{
				int jpos = a[j].find_last_of('1');
				if(jpos <= i)
				{
					for(int k = j - 1; k >= i; k--)
					{
						ret++;
						swap(a[k], a[k + 1]);
					}
					break;
				}
			}
		}
	}
	return ret;
}

int main()
{
	ifstream in("in.txt");
	int tests, n;
	in >> tests;
	vector<string> toSolve;
	for(int t = 1; t <= tests; t++)
	{
		in >> n;
		toSolve.resize(n);
		for(int i = 0; i < n; i++)
			in >> toSolve[i];
		cout << "Case #" << t << ": " << Solve(toSolve) << endl;
	}
	return 0;
}