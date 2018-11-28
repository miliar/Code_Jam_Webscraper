#include <map>
#include <set>
#include <deque>
#include <cstdio>
#include <vector>
using namespace std;

int n,s,q;

typedef vector<int> stav;
struct ltstr {
  bool operator()(const char* s1, const char* s2) const {
    return strcmp(s1, s2) < 0;
  }
};

int main() {
	scanf("%d\n", &n);
	for (int ixn = 1; ixn<=n; ixn++) {
		map<char *,int,ltstr> engine;
		vector<int> query;
		int ce = 0;
		
		scanf("%d\n", &s);
		for (int i=0; i<s; i++) {
			char *str = (char *) malloc(101*sizeof(char));
			scanf("%[^\n] ", str);
			engine[str] = ce++;
		}
		char *str = (char *) malloc(101*sizeof(char));
		scanf("%d\n", &q);
		for (int i=0; i<q; i++) {
			scanf("%[^\n] ", str);
			query.push_back(engine[str]);
		}

		set<vector<int> > old;
		deque<stav> fronta;
		for (int i=0; i<s; i++) {
			stav st; st.push_back(0); st.push_back(0); st.push_back(i);
			fronta.push_back(st);
		}
		/*fprintf(stderr, "%d\n", q);
		for (int i=0; i<q; i++) fprintf(stderr, "%d ", query[i]);
		fprintf(stderr, "\n");*/
		while (true) {
			stav st = fronta.front(); fronta.pop_front();
			//fprintf(stderr, "seeing %d %d %d\n", st[0], st[1], st[2]);
			while (st[0]<q && st[2]!=query[st[0]]) st[0]++;
			if (st[0]==q) {
				printf("Case #%d: %d\n", ixn, st[1]);
				break;
			} else {
				st[1]++;
				for (int i=0; i<s; i++) if (i!=st[2]) {
					st[2] = i;
					vector<int> st2;
					st2.push_back(st[0]); st2.push_back(st[2]);
					if (old.find(st2)==old.end()) {
						old.insert(st2); fronta.push_back(st);
					}
				}
			}
		}
	}

	return 0;
}
