#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

int main()
{
 	ifstream fi;
	ofstream fo;
	
 	fi.open("A-small.in", ios::in);
 	fo.open("A-small.out", ios::out);
	
	long long n, P, K, L;
	fi >> n;

	for (int z = 1; z <=n; z ++)
	{
	fi >> P >> K >> L;

	vector <long long> a(L);

	for (int i = 0; i < L; i ++)
	{
		fi >> a[i];
	}
	sort(a.rbegin(), a.rend());
	
	unsigned long long rs = 0;

	for (long long count, i = 1; i <= P; i ++)
	{
		for (long long j = 0; j < K; j ++)
		{
			if (a.size() > 0)
			{
				rs += a[0] * i;
				a.erase(a.begin());
			}
			else
			{
				break;
			}
		}
		if (a.size() == 0)
		{
			break;
		}
	}
	fo << "Case #" << z << ": " << rs << endl;
	}
	fi.close();
	fo.close();
	return 0;
}
