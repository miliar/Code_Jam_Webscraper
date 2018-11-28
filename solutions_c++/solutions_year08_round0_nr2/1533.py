#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

typedef pair<int,int> stav;

int scantime() {
	int a,b;
	scanf("%d:%d ", &a, &b);
	return a*60+b;
}

struct lttime {
  bool operator()(const pair<int,stav> s1, const pair<int,stav> s2) const {
    int smer1 = s1.second.first+s1.second.second, smer2 = s2.second.first+s2.second.second;
		return s1.first<s2.first || (s1.first==s2.first && smer1>smer2);
  }
};

int main() {
	int n;
	scanf("%d\n", &n);
	for (int ixn = 1; ixn<=n; ixn++) {
		int t,na,nb;
		vector<pair<int,stav> > fronta;
		scanf("%d %d %d ", &t, &na, &nb);
		for (int i=0; i<na+nb; i++) {
			int t1 = scantime(), t2 = scantime();
			fronta.push_back(make_pair(t1, (i<na)?make_pair(-1,0):make_pair(0,-1)));
			fronta.push_back(make_pair(t2+t, (i<na)?make_pair(0,1):make_pair(1,0)));
		}

		sort(fronta.begin(), fronta.end(), lttime());
		stav cur = make_pair(0,0), res = make_pair(0,0);
		for (int i=0; i<2*(na+nb); i++) {
			/*pair<int,stav> t = fronta[i];
			fprintf(stderr, "cas %d zmena %d %d\n", t.first, t.second.first, t.second.second);*/
			stav c = fronta[i].second;
			if (cur.first+c.first<0) res.first++; else cur.first += c.first;
			if (cur.second+c.second<0) res.second++; else cur.second += c.second;
		}

		printf("Case #%d: %d %d\n", ixn, res.first, res.second);
	}

	return 0;
}
