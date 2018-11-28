#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <deque>
#include <map>
#include <cmath>
#include <set>
#include <stack>
#include <sstream>

using namespace std;

string toString(int val)
{
    ostringstream oss;
    oss << val;
    return oss.str();
}

int fromString(const std::string& s) 
{
  istringstream iss(s);
  int res;
  iss >> res;
  return res;
}

long long int gcd(long long int a, long long int b)
{
	if (b == 0)
		return a;
	else
		return gcd (b, a % b);
}

int main() 
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		cout << "Case #" << t + 1 << ": ";
		int n;
		long long int l, h;
		cin >> n >> l >> h;
		vector <long long int> orc(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> orc[i];
		}
		sort(orc.begin(), orc.end());
		vector <long long int> gcds(n);
		gcds[n - 1] = orc[n - 1];
		for (int i = n - 2; i >= 0; --i)
		{
			gcds[i] = gcd(orc[i], gcds[i + 1]);
		}
		vector <long long int> lcms(n);
		lcms[0] = orc[0];
		for (int i = 1; i < n; ++i)
		{
			if (lcms[i - 1] == -1)
			{
				lcms[i] = -1;
			}
			else
			{
				long long int a1 = lcms[i - 1] / gcd(lcms[i - 1], orc[i]);
				if (a1 > h / orc[i] + 1)
				{
					lcms[i] = -1;
				}
				else
				{
					lcms[i] = a1 * orc[i];
					if (lcms[i] > h)
					{
						lcms[i] = -1;
					}
				}
			}
		}
		bool solved = false;
		for (int i = 0; (i < n) && (!solved); ++i)
		{
			long long int nod = gcds[i], nok;
			if (i == 0)
			{
				nok = 1;
			}
			else
			{
				nok = lcms[i - 1];
			}
			if ((nok != -1) && (nod % nok == 0))
			{
				long long int l1 = l / nok;
				if (l1 * nok < l)
				{
					++l1;
				}
				long long int h1 = h / nok;
				long long int nd = nod / nok;
				int beg;
				for (long long int j = 1; (j * j <= nd) && (!solved); ++j)
				{
					beg = j;
					if ((nd % j == 0) && (l1 <= j) && (j <= h1) && (!solved))
					{
						cout << j * nok << endl;
						solved = true;
					}
				}
				for (int j = beg; j >= 1; --j)
				{
					if ((nd % j == 0) && (l1 <= nd / j) && (nd / j <= h1) && (!solved))
					{
						cout << (nd / j) * nok << endl;
						solved = true;
					}
				}
			}
		}
		if (!solved)
		{
			long long int nok = lcms[n - 1];
			long long int left = l / nok;
			if (left * nok < l)
			{
				++left;
			}
			if ((left * nok > h) || (nok == -1))
			{
				cout << "NO" << endl;
			}
			else
			{
				cout << left * nok << endl;
			}
		}
	}

	
	
	return 0;
}







