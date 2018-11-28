#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <map>
#include <set>
#include <sstream>
#include <strstream>
#include <queue>
#include <stack>
#include <set>
#include <cstring>
#include <string>

using namespace std;

ifstream in("large.in");
ofstream out("large.out");

int n,k,b,T;

int x[110],v[110];

vector <int> ans;

bool ka[110];

long long solve()
{
	int i;
	long long answer = 0;

	ans.clear();

	for (i = 0 ; i < n ; i++)
		ka[i] = false;

	for (i = n - 1; i >= 0 ; i--)
		if (b - x[i] <= T*v[i])
		{
			ans.push_back(i);
			ka[i] = true;
		}

	if (ans.size() < k)
		return -1;

	if (k == 0)
		return 0;

	int u = ans[k - 1];
	
	for (i = u + 1; i < n; i++)
		if (!ka[i])
		{
			answer += (i - u);
			u++;
		}
	return answer;

}

int main()
{
	int test,i;
	in >> test;
	long long answer = 0;
	for (int t = 1; t <= test; t++)
	{
		answer = 0;

		in >> n >> k >> b >> T;

		for (i = 0 ; i < n; i++)
			in >> x[i];
		for (i = 0 ; i < n; i++)
			in >> v[i];

		answer = solve();

		if (answer < 0)		
			out << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		else
			out << "Case #" << t << ": " << answer << endl;
	}
	return 0;
}