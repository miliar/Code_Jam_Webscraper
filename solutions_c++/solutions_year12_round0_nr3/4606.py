#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cassert>
#include <ctime>
#include <sstream>

using namespace std;

#ifdef WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<ll> vll;
typedef vector<vll> vvll;

ll rdtsc() {
    ll tmp;
    asm("rdtsc" : "=A"(tmp));
    return tmp;
}

#define TASKNAME "text"
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
#define INF ((int)1e9)
#define sqr(x) ((x) * (x))         
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

int main() {
	srand(rdtsc());
	freopen(TASKNAME".in", "r", stdin);
	freopen(TASKNAME".out", "w", stdout);

	int t;
	while (scanf("%d", &t) >= 1) {
		for (int iter = 0; iter < t; iter++) {
			int a, b;
			scanf("%d%d", &a, &b);
			int ans = 0;
			for (int n = a; n < b; n++) {
				eprintf("%d\n", n);
				for (int m = n + 1; m <= b; m++) {
					string s1, s2;
					stringstream ss;
					ss << n;
					ss >> s1;
					stringstream ss1;
					ss1 << m;
					ss1 >> s2;
					int n = s1.length();
					if ((int)s2.length() != n)
						break;
					int ok = 0;
					for (int i = 1; i < n; i++) {
						if (string(s1, i) == string(s2, 0, n - i) && string(s1, 0, i) == string(s2, n - i)) {
							ok = 1;
							break;
						}
					}
					ans += ok;	
				}
			}                    	

			printf("Case #%d: %d\n", iter + 1, ans);
		}	
		//break;
	}   
	return 0;
}
