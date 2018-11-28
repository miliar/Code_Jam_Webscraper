#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <sstream>
#include <set>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <bitset>

#define f(i, n)             for(int i = 0; i < n; i++)
#define s(n)				scanf("%d",&n)
#define sl(n) 				scanf("%lld",&n)
#define sf(n) 				scanf("%lf",&n)
#define sc(n)               scanf("%s", &n)    
#define fill(a,v) 			memset(a, v, sizeof a)
#define ull 				unsigned long long
#define ll 					long long
#define bitcount 			__builtin_popcount
#define all(x) 				x.begin(), x.end()
#define pb          		push_back
#define gcd					__gcd
#define inf (int)1e9
#define gc getchar
#define maxn (int)1e6
using namespace std;

inline void ss(int &n)
{
     n = 0;
     char c = gc();
     while(c < 48 || c > 57) c = gc();
     while(c >= 48 && c <= 57) n = (n << 1) + (n << 3) + c - 48, c = gc();
}

bool a[110][110];
int R, x1, x2, Y1, y2;

int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	
	int t;
	s(t);
	for(int test = 1; test <= t; test++)
	{
		f(i, 110) f(j, 110) a[i][j] = 0;
		s(R);
		while(R--)
		{
			s(Y1); s(x1); s(y2); s(x2);
			for(int x = x1; x <= x2; x++)
				for(int y = Y1; y <= y2; y++)
					a[x][y] = 1;
		}
		
		int sec = 0;
		while(1)
		{
			//f(i, 6) {f(j, 6) cout << a[i + 1][j + 1]; cout << endl;} cout << endl;	
			bool b = 1;
			f(i, 101) f(j, 101) if(a[i][j]) {b = 0; i = 101; break;}
			if(b) break;
				
			for(int i = 100; i > 0; i--)
				for(int j = 100; j > 0; j--)
					if(a[i][j])
					{
						if(!a[i - 1][j] && !a[i][j - 1]) a[i][j] = 0;
					}
					else 
					{
						if(a[i][j - 1] && a[i - 1][j]) a[i][j] = 1;
					}
					
				
			sec++;
		}
		
		printf("Case #%d: %d\n", test, sec);
	}
}
