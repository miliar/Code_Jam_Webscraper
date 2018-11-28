#include <iostream>
#include <string>
#include <set>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define sz(s) s.size()

using namespace std;

string p[6000], s;
bool q[20][30];
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int l, d, n;
	cin >> l >> d >> n;
	forn(i, d)
		cin >> p[i];
	forn(i, n){
		cin >> s;
		memset(q, false, sizeof(q));
		int k = 0;
		bool b = false;
		forn(j, sz(s)){
			if (isalpha(s[j])){
				q[k][s[j] - 'a'] = true;
				if (!b)
					k++;
			}
			if (s[j] == '('){
				b = true;
			}
			if (s[j] == ')'){
				b = false;
				k++;
			}
		}
		int ans = 0;
		forn(j, d){
			b = false;
			forn(i1, l){
				if (!q[i1][p[j][i1] - 'a'])
					b = true;
			}
			if (!b)
				ans++;
		}
		cout << "Case #" << i + 1 << ": " << ans << endl; 
		
	}
	return 0;
}