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
#include <cassert>

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

llint inll() {
	llint a;
	scanf("%lld ", &a);
	return a;
}

int main() {
	int T = in();
	rep(tst, T) {
		printf("Case #%d: ", tst + 1);
		
		int N = in();
		int pd = in();
		int pg = in();
		
		if(pg == 100) {
			if(pd == 100) cout << "Possible" << endl;
			else cout << "Broken" << endl;
			continue;
		}
		else if(pg == 0) {
			if(pd == 0) cout << "Possible" << endl;
			else cout << "Broken" << endl;
		}
		else if(N >= 100) {
			cout << "Possible" << endl;
		}
		else {
			int hoge = 0;
			bool ok = false;
			rep(i, N) {
				hoge += pd;
				if(hoge % 100 == 0) {
					ok = true;
					break;
				}
			}
			if(ok) cout << "Possible" << endl;
			else cout << "Broken" << endl;
		}
	}
	return 0;
}
