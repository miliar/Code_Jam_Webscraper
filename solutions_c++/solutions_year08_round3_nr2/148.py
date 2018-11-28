#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <numeric>

using namespace std;

long long ans;

void evaluate(vector <char> & last, string & num, int ind)
{
	if (ind == num.size() - 1)
	{
		last.push_back(num[ind]);

		long long n = 0, res = 0, sign = 1;
		int i;

		for(i = 1; i < last.size(); i += 2)
		{
			if (last[i - 1] == ' ') n = n * 10 + (last[i] - '0');												
			else if (last[i - 1] == '+')
			{
				res += sign * n;
				n = last[i] - '0';
				sign = 1;
			}
			else if (last[i - 1] == '-')
			{
				res += sign * n;
				n = last[i] - '0';
				sign = -1;
			}
		}

		res += sign * n;

		if (res % 2 == 0 || res % 3 == 0 || res % 5 == 0 || res % 7 == 0) ++ans;
		last.pop_back();
		return;
	}

	last.push_back(num[ind]);
	
	last.push_back(' ');
	evaluate(last, num, ind + 1);
	last.pop_back();
	
	last.push_back('+');
	evaluate(last, num, ind + 1);
	last.pop_back();
	
	last.push_back('-');
	evaluate(last, num, ind + 1);
	last.pop_back();

	last.pop_back();
}

int main()
{
	ifstream fin("b.in");
	ofstream fout("b.out");

	int T, N;

	fin >> N;

	for(T = 1; T <= N; ++T)
	{
		string num;
		vector <char> last(1, ' ');

		fout << "Case #" << T << ": ";
		fin >> num;
		ans = 0;
		evaluate(last, num, 0);
		fout << ans << endl;
	}
	return 0;
}