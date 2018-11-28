#include <iostream>
#include <string>
#include <set>
#include <vector>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i < int(n); i++)

#define sz(s) s.size()
#define X first
#define Y second
using namespace std;
int d[1000][30];
string s;
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int n;
	scanf("%d\n", &n);
	string p = "*welcome to code jam";
	forn(t, n){
		getline(cin, s);
		memset(d, 0, sizeof(d));
		s = '*' + s;
		d[0][0] = 1;
		for1(i, sz(s)){
			forn(j, sz(p)){
				d[i][j] += d[i - 1][j];
				d[i][j] %= 100000;
				if (d[i - 1][j] != 0){
					if (s[i] == p[j + 1]){
						d[i][j + 1] += d[i - 1][j];
						d[i][j + 1] %= 100000;
					}
				}
			}
		}
		printf("Case #%d: %.4d\n", t + 1, d[sz(s) - 1][sz(p) - 1] % 10000);
	}
	return 0;
}