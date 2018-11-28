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

const int mxn = 260;
int n, c, o;
char combine[mxn][mxn];
bool oppose[mxn][mxn];

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("B-small-attempt0.in", "r", stdin);
	//freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	string s;
	int t;
	s(t);
	for(int test = 1; test <= t; test++)
	{
		f(i, mxn) f(j, mxn) combine[i][j] = '-', oppose[i][j] = 0;
		s(c);
		f(i, c)
		{
			cin >> s;
			char a = s[0], b = s[1], x = s[2];
			combine[a][b] = combine[b][a] = x;
		}
		
		s(o);
		f(i, o)
		{
			cin >> s;
			char a = s[0], b = s[1];
			oppose[a][b] = oppose[b][a] = 1;
		}
		
		//for(int i = 'A'; i <= 'Z'; i++){ for(int j = 'A'; j <= 'Z'; j++) cout << combine[i][j]; cout << endl;} cout << endl;
		//for(int i = 'A'; i <= 'Z'; i++){ for(int j = 'A'; j <= 'Z'; j++) cout << oppose[i][j]; cout << endl;} cout << endl;
		
		s(n);
		cin >> s;
		char ret[1000];
		int p = 0;
		
		f(i, n)
		{
			ret[p++] = s[i];
			if(p > 1)
			{
				char a = ret[p - 1], b = ret[p - 2];
				char c = combine[a][b];
				//cout << a << " + " << b << " -> " << c << endl; 
				if(c != '-') ret[--p - 1] = c;
				else
				{
					f(j, p)
						if( oppose[ ret[j] ][ ret[p - 1] ] )
						{
							p = 0;
							break;
						}
				}
			}
			//ret[p] = 0; puts(ret);
		}
		
		ret[p] = 0;
		printf("Case #%d: [", test);
		if(p)
		{
			printf("%c", ret[0]);
			for(int i = 1; i < p; i++) printf(", %c", ret[i]);
		}
		puts("]");
	}
}
