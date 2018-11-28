#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <climits>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define Long long long

int v[512];
bool seen[512];
int len;

bool good(int mask, int n)
{
	len = 0;
	fill(seen, seen+n+1, 0);	
	
	for (int i=0; i<n-2; i++)
		if ( ((mask>>i)&1) == 1 )
		{
			v[len++] = i+2;
			seen[i+2] = true;
		}
	v[len++] = n;
	seen[n] = true;
		
	bool flag = true;
	int c = 0;
	
	do
	{
		c = 0;
		for (int i=0; i<len; i++)
			if (v[i] <= n) c++;
			else break;
		
		if (c!=1 && !seen[c]) return false;
		n = c;
		
	}	while ( c != 1);
	
	return true;
}

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t, n = 1;
	cin >> t;
	int ans[] = {0, 0, 1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780, 20388, 38674, 73562, 40265, 68060, 13335, 84884};
	
	
	for (int x=1; x<=t ; x++)
	{
		cin >> n;
		
		/*		
		int stop = 1<<(n-2), c = 0;
		for (int i=0; i<stop; i++)
			if (good(i, n)) 
			{
				//cout << "good: " << i << endl;
				c = (c+1)%100003;
			}
		*/
		
		printf("Case #%d: %d\n", x, ans[n]);
	}
		
}