#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#include <iostream>
#include <string>

using namespace std;

string p = "welcome to code jam", s;
int d[501][19];


int main() {
	int t;
	scanf("%d\n",&t);
	for (int test=1; test<=t; test++) {
		memset(d,0,sizeof(d));
		getline(cin,s);
		int n = s.length();
		for (int i=0; i<n; i++)
			for (int j=0; j<19; j++) if (p[j] == s[i]) {
				if (j == 0)
					d[i][j] = 1;
				else
					for (int k=0; k<i; k++) d[i][j] += d[k][j-1], d[i][j] %= 10000;
			}
		int ans = 0;for (int i=0; i<n; i++) ans += d[i][18], ans %= 10000;
		printf("Case #%d: %04d\n",test,ans);
	}
}
