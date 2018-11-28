#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <utility>

typedef long double LD;
typedef long long LL;
using namespace std;


int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tst;
	cin >> tst;

	for (int t = 1; t <= tst; ++t)
	{
		bool a[8][8];
		memset(a, 0, sizeof(a));
		cerr << "Test " << t << '\n';
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n - 1; ++i)
			a[i][i + 1] = a[i + 1][i] = true;
		a[0][n - 1] = a[n - 1][0] = true;

		int us[8], vs[8];

		for (int i = 0; i < m; ++i)
			cin >> us[i];
		for (int i = 0; i < m; ++i)
			cin >> vs[i];

		for (int i = 0; i < m; ++i)
			a[us[i] - 1][vs[i] - 1] = a[vs[i] - 1][us[i] - 1] = true;

		int p[256][9];
		int q[256];
		int w = 0;

		for (int m = 0; m < (1 << n); ++m)
		{
			int tp[9];
			int tq = 0;

			for (int j = 0; j < n; ++j) if (m & (1 << j))
			{
				tp[tq] = j;
				tq++;
			}
			if (tq < 3) continue;
			tp[tq] = tp[0];

			bool corr = true;
			for (int i = 0; i < tq; ++i)
				if (!a[ tp[i] ][ tp[i + 1] ]) corr = false;
			if (!corr) continue;
			
			for (int i = 0; i < tq; ++i)
				for (int j = i + 2; j < tq; ++j)
				{
					if (a[ tp[i] ][ tp[j] ] && !(i == 0 && j == tq - 1)) corr = false;
				}
			if (!corr) continue;
			
			for (int i = 0; i < tq; ++i)
				p[w][i] = tp[i];
			q[w] = tq;
			++w;
		}

		cerr << w << " masks" << '\n';
		
		if (w == 1)
		{
			cout << "Case #" << t << ": " << n << '\n';
			for (int i = 0; i < n - 1; ++i) cout << i + 1 << ' ';
			cout << n << '\n';
			continue;
		}

		for (int c = n - 1; c >= 1; --c)
		{
			int b[9];
			memset(b, 0, sizeof(b));
	
	        bool wasgood = false;
	        
	        while (b[n] == 0)
	        {
	        	bool good = true;
	        	for (int i = 0; i < w; ++i)
	        	{
	        		bool was[16];
	        		memset(was, 0, sizeof(was));

	        		for (int j = 0; j < q[i]; ++j)
	        			was[ b[ p[i][j] ] ] = true;
	        		for (int j = 0; j < c; ++j) if (!was[j]) { good = false; break; }
	        	}
                
                if (good)
                {
	         		wasgood = true;
	         		cout << "Case #" << t << ": " << c << '\n';
	        		for (int i = 0; i < n - 1; ++i) cout << b[i] + 1 << ' ';
	        		cout << b[n - 1] + 1 << '\n';
	        		break;
                }
	        	
	        	b[0]++;
	        	for (int i = 0; b[i] >= c; ++i)
	        	{
	        		b[i] -= c; b[i + 1]++;
	        	}
	        }
	        if (wasgood) break;
	        
	    }
	}

	return 0;
}
