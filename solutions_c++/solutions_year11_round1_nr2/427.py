#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define pb push_back

typedef long long ll;

struct vertex {
	map<ll, int> p;

	void clear() {
		p.clear();
	}

	vertex() {
		cnt = 0;
		s = 0;
	}
	int cnt;
	string *s;
	int wn;
};


vector<vertex> t[11];
vector<string> w;
char c[30];
char buf[300];
int n, m;
int len;

int pans;
int ans;

void go(int v, int cans) {
	if (t[len][v].cnt == 1) {
		if (cans > ans || cans == ans && pans > t[len][v].wn) {
			ans = cans;
			pans = t[len][v].wn;
		}
		return;
	}
	if (t[len][v].p.count(0)) {
		if (t[len][v].p.size() == 1) {
			go(t[len][v].p[0], cans);
		} else {
			go(t[len][v].p[0], cans + 1);
			for(map<ll, int>::iterator it = t[len][v].p.begin(); it != t[len][v].p.end(); ++it)
				if (it->second != 0) {
					go(it->second, cans);
				}
		}
	} else {
		for(map<ll, int>::iterator it = t[len][v].p.begin(); it != t[len][v].p.end(); ++it)
			go(it->second, cans);
	}
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d\n", &tk);

    for  (int tc = 1; tc <= tk; ++tc) {
    	printf("Case #%d:", tc);
    	w.clear();
    	scanf("%d %d\n", &n, &m);
    	forn(i, n) {
    		gets(buf);
    		w.pb(buf);	
    	}

    	while (m --> 0) {
    		gets(c);

    		forn(i, 11) {
    			t[i].clear();
    			t[i].pb(vertex());
    		}

    		forn(i, n) {
    			len = w[i].length();
    			int v = 0;
    			t[len][0].cnt++;
    			t[len][0].wn = i;
    			forn(j, 26) {
    				ll hash = 0;
    				forn(k, len)
    					if (w[i][k] == c[j]) hash = hash * 9973 + k + 43;
    				if (!t[len][v].p.count(hash)) {
    					t[len][v].p[hash] = t[len].size();
    					t[len].pb(vertex());
    				}
    				v = t[len][v].p[hash];
    				t[len][v].cnt++;
    				t[len][v].wn = i;
    			}
    				
    		}

    		ans = -1;
    		pans = 9999999;
    		for (len = 1; len <= 10; ++len) {
    			if (t[len][0].cnt == 0) continue;
    			go(0, 0);
    		}
    		//cout << " " << *pans << "(" << ans << ")";
    		cout << " " << w[pans];
    	}
    	cout << endl;
    			
    	cerr << "Solved: " << tc << endl;
    }
	
	return 0;
}