#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i < int(n); i++)
#define mp(a, b) make_pair(a, b);
#define X first
#define Y second
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;

typedef long long li;
typedef pair<int, int> pt;

char used[100];
map<char, li> m;
char mm[100];
bool us[100];
li b[100];
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	string s, s1;
	forn(i, 10){
		mm[i] = char(i + '0');
		m[char(i + '0')] = i;
	}
	char c = 'a';
	for(int i = 10; i < 26 + 10; i++){
		mm[i] = c;
		m[c] = i;
		c++;
	}
	forn(q, t){
		cin >> s;
		s1 = s;
		memset(us, false, sizeof(us));
		memset(b, 0, sizeof(b));
		forn(i, 100)
			used[i] = 'A';
		int a = 1;
		forn(i, sz(s)){
			if (used[m[s[i]]] == 'A'){
				used[m[s[i]]] = mm[a];
				us[a] = true;
				s1[i] = mm[a];
				for(int j = 0; j < 100; j++)
					if (!us[j]){
						a = j;
						break;
					}
			}
			else{
				s1[i] = used[m[s[i]]];
			}

		}
		long long base = -1;
		forn(i, sz(s1)){
			if (m[s1[i]] > base)
				base = m[s1[i]];
		}
		base++;
		forn(i, sz(s1)){
			if (i == 0)
				b[i] = 1;
			else
				b[i] = base * b[i - 1];
		}
		li ans = 0;
		forn(i, sz(s1)){
			ans += m[s1[i]] * b[sz(s1) - 1 - i]; 
		}
		cout << "Case #" << q + 1 <<": " << ans << endl;

	}
	return 0;
}