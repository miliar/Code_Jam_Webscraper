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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("answer.txt", "w", stdout);
	int tc;
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		int n;
		cin >> n;
		vector< vector<char> > s(n, vector<char> (n));
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < n; ++j)
				cin >> s[i][j];
		}
		vector<int> ans(n);
		//wp
		vector<double> wp(n);
		vector< vector<double> > wp1(n, vector<double>(n));
		for(int i = 0; i < n; ++i)
		{
			double w = 0, l = 0;
			for(int j = 0; j < n; ++j)
			{
				if(s[i][j] == '1')
					++w;
				else if(s[i][j] == '0')
					++l;
			}
			wp[i] = w / (w+l);

			for(int j = 0; j < n; ++j)
			{
				if(s[i][j] == '1')
					wp1[i][j] = (w-1) / (w+l-1);
				else if(s[i][j] == '0')
					wp1[i][j] = w / (w+l-1);
			}
		}

		//owp
		vector<double> owp(n);
		vector< vector<double> > owp1(n, vector<double>(n));
		for(int i = 0; i < n; ++i)
		{
			double w = 0, cnt = 0;
			for(int j = 0; j < n; ++j)
			{
				if(s[i][j] != '.')
				{
					w += wp1[j][i];
					++cnt;
				}
			}
			owp[i] = w / cnt;

			for(int j = 0; j < n; ++j)
			{
				if(s[i][j] != '.')
					owp1[i][j] = (w-wp1[j][i]) / (cnt-1);
			}
		}

		//oowp
		vector<double> oowp(n);
		for(int i = 0; i < n; ++i)
		{
			double w = 0, cnt = 0;
			for(int j = 0; j < n; ++j)
			{
				if(s[i][j] != '.')
				{
					w += owp[j];
					++cnt;
				}
			}
			oowp[i] = w / cnt;
		}

		cout << "Case #" << Case + 1 <<": " << endl;
		for(int i = 0; i < n; ++i)
		{
			cout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
		}
	}

	return 0;
}
