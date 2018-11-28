#include <iostream>

#define forn(i, n) for(int i = 0; i < int(n); i++)
using namespace std;
typedef long long li;
li g[2000];
li s[2000];
int idx[2000];
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t, n, r, k;
	cin >> t;
	forn(q, t){
		cin >> r >> k >> n;
		forn(i, n){
			cin >> g[i];
			
		}
		forn(i, n){
			li a = g[i];
			int j = (i + 1) % n;
			while(j != i && a + g[j] <= k){
				a += g[j];
				j++;
				
				j %= n;
			}
			s[i] = a;
			idx[i] = j;

		}
		int id = 0;
		li ans = 0;
		forn(i, r){
			ans += s[id];
			id = idx[id];
		}
		cout << "Case #" << q + 1 << ": " << ans << endl;
	}
	return 0;
}