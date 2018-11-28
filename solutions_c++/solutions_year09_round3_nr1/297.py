#include <iostream>
#include <map>
#include <fstream>

using namespace std;

#define cin fin
ifstream fin( "A-large.in" ) ;
ofstream fout( "A-large.out" ) ;
#define cout fout

int main()
{
	int T;
	cin >> T;
	for (int run = 1; run <= T; ++run)
	{
		string s;
		cin >> s;
		
		int x = 0, m = 2;
		int n = s.length();
		map<char, int> mark;
		
		mark.clear();
		
		for (int i = 0; i < n; ++i)
			if (!mark[s[i]])
			{
				mark[s[i]] = m;
				if (m == 2) m = 1;
				else 
					if (m == 1) m = 3;
					else ++m;
				++x;
			}
		
		if (x == 1) ++x;
		
		long long res = 0;
		long long p = 1;
		for (int i = n - 1; i >= 0; --i)
		{
			int u = mark[s[i]];
			res += (long long)(u - 1) * p;
			p *= x;
		}
		
		cout << "Case #" << run << ": " << res << endl;
	}
	return 0;
}
