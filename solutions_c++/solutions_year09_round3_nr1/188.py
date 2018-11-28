#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <sstream>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <list>
using namespace std;
typedef long long int64;
#define showbit(a, b) (((a) >> (b)) & 1)
#define move(n) ((1) << (n))
#define sz(x) (int)x.size()
const double eps = 1e-8;
int sgn(double x)  { return (x > eps) - (x < -eps); }
char s[88];
int hash[128];
int main() {
	freopen("A.out", "w", stdout);
	int t;
	scanf("%d", &t);
	int Case = 1;
	while(t--)  {
printf("Case #%d: ", Case++);
		scanf("%s", s);
		
		memset(hash, -1, sizeof(hash));
		hash[s[0]] = 1;
		int k = 0;
		for(int i = 1; s[i]; i++)  {
			if(hash[s[i]] != -1)  continue;
			hash[s[i]] = k++;
			if(k == 1) k++;
		}
		int64 ans = 0;
        if(k <= 1)  k = 2;
		for(int i = 0; s[i]; i++)  {
			ans = ans * k + hash[s[i]];
		}
		//cout << k << endl;
		
		cout << ans << endl;
	}
	return 0;
}

