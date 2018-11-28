#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <utility>
using namespace std;

#define TRACE(x...) 
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

char buf[1000];
int has_feat[110][10010];

map<string,int> m_feat;

template <class T1, class T2>
ostream& operator<<(ostream& o, pair<T1,T2> p) {
	return o << "<" << p.first << "," << p.second << ">";
}

typedef pair< pair<double,int>, pair<int,int> > retorno_t;

pair< pair<double,int>, pair<int,int> > parse_node(const char *s) {
	int p=0, paux;
	double prob;
	int feat_idx=-1;
	int t1=-1, t2=-1;

	while (s[p] < '0' || s[p] > '9') p++;
	sscanf(s+p, "%lf%n", &prob, &paux);
	p += paux;

	while (s[p] == ' ') p++;

	if (s[p] >= 'a' && s[p] <= 'z') {
		char tmp[1000];
		sscanf(s+p, " %s%n", tmp, &paux);
		p += paux;
		feat_idx = m_feat[ string(tmp) ];

		while (s[p] != '(') p++;
		t1 = p;
		int open_p=0;
		for (int i=p; s[i]; i++) {
			if (s[i] == '(') open_p++;
			else if (s[i] == ')') open_p--;

			if (!open_p) {
				t2=i;
				while (s[t2] != '(') t2++;
				break;
			}
		}
	}

	return make_pair( make_pair(prob,feat_idx), make_pair(t1,t2) );
}

int main() {
	int T;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
		memset(has_feat, 0, sizeof(has_feat));
		m_feat.clear();
		printf("Case #%d:\n", _42);

		int L;
		scanf(" %d", &L);
		string S="";
		for (int i=0; i < L; i++) {
			scanf(" %[^\n]", buf);
			S += " " + string(buf);
		}
		WATCH(S);

		int A;
		scanf(" %d", &A);
		for (int i=0; i < A; i++) {
			scanf(" %s", buf);
			int n;
			scanf(" %d", &n);
			PRINT("%s", buf);
			for (int j=0; j < n; j++) {
				scanf(" %s", buf);
				int f_idx = m_feat.insert( make_pair(string(buf),m_feat.size())).first->second;
				has_feat[i][f_idx] = 1;
				PRINT(" %d", f_idx);
			}
			PRINT("\n");
		}

		for (int i=0; i < A; i++) {
			double p=1.0;
			int acc_p=0;

			retorno_t r = parse_node(S.c_str());
			WATCH(r);
			p *= r.first.first;
			while (r.first.second != -1) {
				if (has_feat[i][r.first.second]) acc_p += r.second.first;
				else acc_p += r.second.second;

				r = parse_node(S.c_str()+acc_p);
				WATCH(r);
				p *= r.first.first;
			}
			printf("%.8lf\n", p);
		}
		PRINT("\n");
	}


	return 0;
}
