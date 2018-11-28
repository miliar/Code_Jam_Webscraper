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

int T;
int n;
long long a[800];
long long b[800];

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");

	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		fin >> n;
		for (int i = 0; i < n; i++)
		{
			fin >> a[i];
		}
		sort(a, a+n);
		for (int i = 0; i < n; i++)
		{
			fin >> b[i];
		}
		sort(b, b+n);
		long long res = 0;
		for (int i = 0; i < n; i++)
		{
			res += a[i] * b[n-1-i];
		}
		fout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
