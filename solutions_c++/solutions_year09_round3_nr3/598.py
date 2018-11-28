#include <vector>        
#include <map>        
#include <set>        
#include <deque>        
#include <algorithm>        
#include <utility>        
#include <sstream>        
#include <iostream>        
#include <cstdio>        
#include <cmath>        
#include <cstdlib>       
#include <conio.h>

using namespace std;   

#define SZ(a) ((int)(a).size())   
#define pii pair<int, int>  
#define mp make_pair  
template<class A, class B> A convert(B x) {stringstream s; s << x; A r; s >> r; return r;}
int calc(int P, vector<int> c)
{
	int res = 0;
	int cells[200];
	memset(cells, 0, sizeof cells);
	for (int i = 0; i < SZ(c); ++i)
	{
		cells[c[i]] = 1;
		int j = c[i]-1;
		while (j > 0 && !cells[j]) { ++res; --j; }
		j = c[i]+1;
		while (j <= P && !cells[j]) { ++res; ++j; }
	}
	return res;
}
int main()
{
	int testCnt;
	cin >> testCnt;
	for (int T = 0; T < testCnt; ++T)
	{
		int P, Q;
		cin >> P >> Q;
		vector<int> c;
		for (int i = 0; i < Q; ++i)
		{
			int t;
			cin >> t;
			c.push_back(t);
		}
		int res = calc(P, c);
		while (next_permutation(c.begin(), c.end()))
		{
			res = min(res, calc(P, c));
		}
		cout << "Case #" << T+1 << ": " << res << endl;
	}
	return 0;
}