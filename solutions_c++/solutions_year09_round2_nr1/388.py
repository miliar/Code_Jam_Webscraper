#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(v) (int(v.size()))

#include <iostream>
#include <string>
#include <map>
#include <iomanip>

using namespace std;

typedef long long ll;

map<string, int> dict;
int tot_v, cur_label;
bool kach[2000];

struct node {
	bool leaf;
	int prop, l, r;
	double prob;
} d[2000];

bool good(char c) {
	return (c != '\n') && (c != ' ');
}

char getNext() {
	char c;
	while (!good(c=getchar()));
	return c;
}

void BugTree() {
	cerr << "BAD TREE DESCRIPTION";
	exit(0);
}

void getTree(int v) {
	if (getNext() != '(') BugTree();
	scanf("%lf",&d[v].prob);
	char c = getNext();
	if (c == ')') {d[v].leaf = 1;return;}
	d[v].leaf = 0;
	string s; s.pb(c);
	while (good(c = getchar())) s.pb(c);
	if (dict.find(s) == dict.end()) dict[s] = cur_label++;
	d[v].prop = dict[s];
	d[v].l = ++tot_v;
	getTree(d[v].l);
	d[v].r = ++tot_v;
	getTree(d[v].r);
	if (getNext() != ')') BugTree();
}

void tr(int v, double &res) {
	res *= d[v].prob;
	if (d[v].leaf) return;
	if (kach[d[v].prop]) tr(d[v].l,res); else tr(d[v].r,res);
}

int main() {
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int tests, l, n, k;
	char c;
	string s;
	scanf("%d\n",&tests);
	for (int i=1; i<=tests; i++) {
		printf("Case #%d:\n",i);
		scanf("%d\n",&l);
		dict.clear(); cur_label = 0, tot_v = 1;
		getTree(1);
		scanf("%d\n",&n);
		for (int j=1; j<=n; j++) {
			getline(cin,s,' ');
			scanf("%d ",&k);
			memset(kach,0,sizeof(kach));
			for (int j1=0; j1<k; j1++) {
				s.clear();
				while (good(c=getchar()) && c!=EOF) s.pb(c);
				if (dict.find(s) != dict.end()) kach[dict[s]] = 1;
			}
			double ans = 1.0;
			tr(1,ans);
			printf("%.7lf\n",ans);
		}
		cerr << "test " << i << " passed\n";
	}

}
