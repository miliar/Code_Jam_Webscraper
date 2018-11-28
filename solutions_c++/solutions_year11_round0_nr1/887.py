#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cctype>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i = 0; i < (n); i++)
#define repr(i,b,e) for(int i = (b); i <= (e); i++)
#define INF (1001001001)
#define EPS (1e-15)

#define pr(x) do{cout << (#x) << " = " << (x) << endl;}while(0)
#define pri(x,i) do{cout << (#x) << "[" << i << "] = " << (x[i]) << endl;}while(0)
#define pra(x,n) rep(__i,n) pri(x,__i);
#define prar(x,b,e) repr(__i,b,e) pri(x,__i);

typedef long long llint;
typedef pair<int, int> pint;
typedef vector<int> vint;

int in() {
	int a;
	scanf("%d ", &a);
	return a;
}

int main() {
	int T = in();
	
	rep(tst, T) {
		int N = in();
		
		int opos = 1, bpos = 1;
		int ostore = 0, bstore = 0;
		int ans = 0;
		rep(i, N) {
			char c;
			scanf("%c ", &c);
			int a = in();
			
			int n = 1 + abs(a - (c == 'O' ? opos : bpos));
			if(c == 'O') {
				n -= ostore;
				ostore = 0;
				if(n < 1) n = 1;
				bstore += n;
				opos = a;
			}
			else {
				n -= bstore;
				bstore = 0;
				if(n < 1) n = 1;
				ostore += n;
				bpos = a;
			}
			
			ans += n;
		}
		printf("Case #%d: %d\n", tst+1, ans);
	}
	return 0;
}
