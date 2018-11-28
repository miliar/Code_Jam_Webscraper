#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int	q[2000];
char	v[2000];	
int	nse;
int	nq;

int calc()
{
	int	ans=0, i, j, ct=0;

	for (i=0;i<nse;i++)
		v[i] = 0;

	for (i=0;i<nq;i++)
	{
		if (ct == (nse - 1) && !v[q[i]])
		{
			ans++;
			ct = 1;
			for (j=0;j<nse;j++)
				v[j] = 0;
			v[q[i]] = 1;
		}
		else if (!v[q[i]])
		{
			ct++;
			v[q[i]] = 1;
		}
	}

	return ans;
}

int main()
{
	int	i, j, n;
	string	str;
	cin >> n;
	cin.ignore(256, '\n');

	for (i=0;i<n;i++)
	{
		cin >> nse;
		cin.ignore(256, '\n');
		vector<string>	v;
		for (j=0;j<nse;j++)
		{
			getline(cin, str);
			v.push_back(str);
		}
		cin >> nq;
		cin.ignore(256, '\n');
		for (j=0;j<nq;j++)
		{
			getline(cin, str);
			q[j] = find(v.begin(), v.end(), str) - v.begin();
		}
		cout << "Case #" << (i+1) << ": " << calc() << endl;
	}

	return 0;
}
