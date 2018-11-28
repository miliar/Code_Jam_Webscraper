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

const int mxn = 2000010;
int A, B;
int vis[mxn], id;

int get(int n)
{
	int tmp = n, cnt = 0, pow = 1, cur = 10, ret = 0;
	id++;
	while(tmp)
	{
		cnt++;
		tmp /= 10;
		pow *= 10;
	}
	
	pow /= 10;
	for(int i = 1; i < cnt; i++)
	{
		int a = n % cur;
		int b = n / cur;
		int x = a * pow + b;
		
		cur *= 10;
		pow /= 10;
		
		//cout << n << " " << x << endl;
		if(x > n && x <= B && vis[x] != id) 
		{
			ret++;	
			vis[x] = id;
		}
	}
	
	return ret;
}

int main()
{	
	//freopen("in.txt", "r", stdin);
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	
	int t;
	s(t);
	for(int test = 1; test <= t; test++)
	{
		s(A); s(B);
		int ret = 0;
		
		for(int i = max(10, A); i <= B; i++) 
		{
			int x = get(i);
			if(x)
			{
				ret += x;
				//cout << i << " -> " << x << endl;
			}
		}
		printf("Case #%d: %d\n", test, ret); 
	}
}
