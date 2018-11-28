#include <iostream>
#include <fstream>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>

double E=1e-9;
using namespace std;

long long mabs(long long x)
{
	if (x>0)
		return x;
	else return -x;
}


int main()
{
	freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int j=0;j<t;++j)
	{
		int res=0, n , s, p;
		
		cin >> n >> s >> p;
		vector <int> a(n);

		for(int i=0; i<n; ++i)
			cin>>a[i];

		sort(a.begin(), a.end());

		for (int i=n-1; i>=0; --i)
		{
			if (a[i] == 0)
			{	
				if(p==0) res++;
			} else if (p==0)
				res++;
			else if (3*p <= a[i])
				res++;
			else if (3*p <= a[i]+2)
				res++;
			else if (s >= 1 && 3*p <= a[i]+4)
			{
				res++; s--;
			}
		}

		printf("Case #%d: %d\n", j+1, res);
	}
    return 0;
}