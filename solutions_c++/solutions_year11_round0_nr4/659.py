#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <cstring>
#include <set>
#include <stack>


using namespace std;

ifstream in("large.in");
ofstream out("large.out");

int a[1100];

int n;

vector < vector <int> > v;
vector <int> vt;

int solve()
{
	int answer = 0,i,j,k;

	v.clear();

	for (i = 1; i <= n; ++i)
		if (a[i] != -1)
		{
			vt.clear();
			vt.push_back(a[i]);			
			k = a[i];		
			a[i] = -1;
			while (k != i)
			{
				int kt = k;
				k = a[k];
				a[kt] = -1;
				vt.push_back(k);				
			}
			v.push_back(vt);
		}

	/*for (i = 0 ; i < v.size(); ++i)
	{
		for (j = 0 ; j < v[i].size(); ++j)
			cout << v[i][j] << " ";
		cout << endl;
	}*/

	for (i = 0 ; i < v.size(); ++i)
	{
		if (v[i].size() > 1)
			answer += v[i].size();
	}

	return answer;
}

int main()
{
	int test, t, i;

	in >> test;

	for (t = 1; t <= test; ++t)
	{
		in >> n;
		for (i = 1 ; i <= n; ++i)
			in >> a[i];
		out << "Case #" << t << ": " << solve() << ".000000" << endl;
	}
	return 0;
}