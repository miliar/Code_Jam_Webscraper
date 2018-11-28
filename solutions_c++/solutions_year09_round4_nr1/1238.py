#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cfloat>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <string>

using namespace std;

#define loop(a, b) for(a = 0; a < b; ++a)
#define iter(a, b, c) for(a = b; a < c; ++a)

vector< vector<bool> > tb(64, vector<bool>(64));

struct st{
	vector<int> ln;
	int d;

	st(vector<int> tba, int da) {
		ln = tba;
		d = da;
	}

	st(){}
};

deque<st> fl;
st u, v;

set<vector<int> > X;

vector<int> start(10), ln(10);

int main(){
	int ds, n, i, j, k, l, tc=1;
	char c;
	scanf("%d", &ds);
	while(ds--) {
		scanf("%d", &n);
		loop(i, n) {
			loop(j, n) {
				scanf(" %c", &c);
				tb[i][j] = (c == '1');
			}
			for(j = n-1; j >= 0 and !tb[i][j]; --j);
			ln[i] = j;
			start[i] = i;
		}

		fl.clear();
		fl.push_back(st(start, 0));
		X.clear();
		X.insert(start);

		while(!fl.empty()) {
			u = fl.front();
			fl.pop_front();

			loop(i, n)
				if (ln[u.ln[i]] > i)
					break;

			if (i == n) {
				printf("Case #%d: %d\n", tc++, u.d);
				break;
			}

			loop(i, n-1) {
				v = u;
				v.d++;
				swap(v.ln[i], v.ln[i+1]);

				if (X.find(v.ln) == X.end()) {
					X.insert(v.ln);
					fl.push_back(v);
				}
			}
		}
	}
	return 0;
}
