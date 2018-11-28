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

map <char, char> m;
string input[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jvzq"};
string output[] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give upqz"};
string a;

int main()
{
	f(i, 3) f(j, input[i].length()) m[ input[i][j] ] = output[i][j];
	//freopen("in.txt", "r", stdin);
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	
	int t = 0;
	s(t); getline(cin, a);
	for(int test = 1; test <= t; test++)
	{
		getline(cin, a);
		int n = a.length();
		string ret;
		
		f(i, n) ret.pb( m[a[i]] );
		printf("Case #%d: ", test);
		cout << ret << endl;
	}
}
