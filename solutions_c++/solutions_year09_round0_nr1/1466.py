#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define VI vector<int>
#define FORR(i,a,b) for(i=a;i<b;i++)
#define pb(a) push_back(a)

int main() {
	ifstream cin("A.in");
	ofstream cout("A.txt");
	int i,j,k,l,n,m,p,r;
	cin >> l >> m >> n;
	vector<string> s(m);
	FOR(i, m) cin >> s[i];
	FOR(i, n) { string t;
		cin >> t;
		r = 0;
		l = t.length();
		FOR(j, m) {
			k = 0;
			bool f = true;
			FOR(p, s[j].size()) {
				f = 0;
				if (t[k] == '(') { while(t[++k]!=')') if (t[k] == s[j][p]) f=1; } else
					if (t[k] == s[j][p]) f = 1; 
				if (!f) break;
				k++;if (k>=l) break;
			}
			r += f; 
		}
		cout << "Case #" << (i+1) << ": " << r << endl;
	}
	return 0;
}