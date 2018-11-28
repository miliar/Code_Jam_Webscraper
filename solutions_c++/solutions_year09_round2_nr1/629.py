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

int m;
struct z{
	string n;
	double d;
	int l, r;
};
z a[1000];
void f(int idx, int b){
	double x;

	scanf("(%lf", &x);
	char c;
	cin >> c;
	if (c == ')'){
		if (b == 1){
			a[idx].l = m;
			a[m].d = x;
			m++;
			scanf("\n");
			return;
		}
		else{
			a[idx].r = m;
			a[m].d = x;
			m++;
			scanf("\n");
			return;
		}
	}
	else{
		string name;
		getline(cin, name);
		a[m].n = c + name;
		a[m].d = x;
		if(b == 1)
			a[idx].l = m;
		else
			a[idx].r = m;
		m++;
		int kk = m - 1;
		scanf("\n");
		f(kk, 1);
		f(kk, 2);
		
		cin >> c;
		scanf("\n");
	}
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int n;
	cin >> n;
	forn(t, n){
		int l;
	
		m = 0;
		if (t == 85){
			m = 0;
		}
		scanf("%d\n", &l);
		forn(j, l){
			a[j].n = "";
			a[j].l = a[j].r = -1;
		}
			double x;
	
			scanf("(%lf", &x);
			char c;
				
			cin >> c;
			if (c == ')'){
				a[0].d = x;
				m++;
			}
			else{
				string name;
				getline(cin, name);
				a[0].n = c + name;
				a[0].d = x;
				m++;
				scanf("\n");
				f(0, 1);
				f(0, 2);
				
			}
		if (l > 1)	
			cin >> c;

		int k;
		cin >> k;
		cout << "Case #" << t + 1 << ":"<< endl;
		forn(i, k){
			string s;
			cin >> s;
			set<string> se;
			cin >> l;
			forn(j, l){
				cin >> s;
				se.insert(s);
			}
			double p = 1.0;
			int idx = 0;
			while (true){
				p *= a[idx].d;
				if (sz(a[idx].n) == 0)
					break;
				if (se.count(a[idx].n))
					idx = a[idx].l;
				else
					idx = a[idx].r;
			}
			printf("%.6lf\n", p);
		}
	}
	return 0;
}