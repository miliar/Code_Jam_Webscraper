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
		bool ans = true;
		long long n, pd, pg;
		cin >> n >> pd >> pg;
		if(pd != 100 && pg == 100)
			ans = false;
		else if(pg == 0 && pd != 0)
			ans = false;
		else
		{
			int d = 100;
			if(pd % 2 == 0)
			{
				pd /= 2;
				d /= 2;
			}
			if(pd % 2 == 0)
			{
				pd /= 2;
				d /= 2;
			}
			if(pd % 5 == 0)
			{
				pd /= 5;
				d /= 5;
			}
			if(pd % 5 == 0)
			{
				pd /= 5;
				d /= 5;
			}
			if(d > n)
				ans = false;
		}

		string res = ans ? "Possible" : "Broken";
		cout << "Case #" << Case + 1 <<": " << res << endl;
	}

	return 0;
}
