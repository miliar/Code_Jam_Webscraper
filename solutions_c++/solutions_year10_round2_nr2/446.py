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
#define gc getchar_unlocked
#define maxn (int)1e6
using namespace std;

inline void ss(int &n)
{
     n = 0;
     char c = gc();
     while(c < 48 || c > 57) c = gc();
     while(c >= 48 && c <= 57) n = (n << 1) + (n << 3) + c - 48, c = gc();
}

int n, k, B, T, x[110], v[110];
ull fp[110];
vector <ull> buff;

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("B-small-attempt1.in", "r", stdin);
	//freopen("B-small-attempt1.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int t;
	s(t);
	for(int test = 1; test <= t; test++)
	{
		buff.clear();
		s(n); s(k); s(B); s(T);
		f(i, n) s(x[i]);
		f(i, n) s(v[i]);
		
		int cnt = 0;
		f(i, n) fp[i] = x[i] + (ull)(T) * v[i];
		//f(i, n) cout << fp[i] << " "; cout << endl;
		
		int p = n - 1;
		
		for(int i = n - 1; i >= 0 && k > 0; i--)
			if(fp[i] >= B)
			{
				k--;
				cnt += buff.size();
			}
			else buff.pb(fp[i]);
		
		/*while(k > 0)
		{
			if(fp[p] >= B)
			{
				k--;
				cnt += buff.size();
			}
			
			else buff.pb(fp[p]);
			p--;
				
		}
		
		for(int i = n - 1; i >= 0 && k > 0; i--)
			if(fp[i] < B) cnt++;
			else k--;
		*/
		
		if(k != 0) printf("Case #%d: IMPOSSIBLE\n", test);
		else printf("Case #%d: %d\n", test, cnt);
	}
}
