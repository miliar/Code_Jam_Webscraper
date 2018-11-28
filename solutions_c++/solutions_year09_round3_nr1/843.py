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
__int64 conv(string s, int n)
{
	__int64 res = 0, st = 1;
	for (int i = SZ(s)-1; i >= 0; --i)
	{
		res += (s[i]-48)*st;
		st *= n;
	}
	return res;
}
int main()
{
	int testCnt;
	cin >> testCnt;
	for (int T = 0; T < testCnt; ++T)
	{
		int num[10], rep[256];
		memset(rep, -1, sizeof rep);
		memset(num, -1, sizeof num);

		string s;
		cin >> s;
		int m = 0;
		for (int i = 0; i < SZ(s); ++i)
		{
			if (rep[s[i]] != -1)
			{
				s[i] = rep[s[i]];
				continue;
			}

			for (int j = i==0?1:0; j <= 9; ++j)
			{
				if (num[j] == -1)
				{
					num[j] = s[i];
					rep[s[i]] = j+48;
					s[i] = j+48;
					m = max(m, j);
					break;
				}
			}
		}
		__int64 res = -1;
		for (int i = m+1; i < 10; ++i)
		{
			__int64 t = conv(s, i);
			if (res == -1 || res > t)
				res = t;
		}
		cout << "Case #" << T+1 << ": " << res << endl;
	}
	return 0;
}