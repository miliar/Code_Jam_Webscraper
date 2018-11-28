#include <cstdio>
#include <vector>
#include <set>

using namespace std;

int Q,P;

const int MAX = 105;
int used[MAX]={0};
set<int> empty;
vector<int> QL;
int minv = 1000001;

void bribe (int n,int gold) {
	if (gold > minv) return;
	if (n == Q && gold < minv) {
		minv = gold;
		return;
	}

	for (int i = 0; i < Q; i++) {
		if (!used[i]) {
			used[i] = 1;

			set<int>::iterator left = empty.lower_bound (QL[i]);
			set<int>::iterator right = empty.upper_bound (QL[i]);
			left--;
			int coins = *right-QL[i]-1;
			coins += QL[i] - *left - 1;

			empty.insert (QL[i]);

			bribe (n+1,gold+coins);

			empty.erase (QL[i]);
			used[i] = 0;
		}
	}
}

int main () {

	int cases;
	scanf ("%d",&cases);
	for (int i = 1; i <= cases; i++) {
		scanf ("%d %d",&P,&Q);
		empty.clear();
		empty.insert(0);
		empty.insert(P+1);

		QL.clear();
		minv = 1000001;
		for (int j = 0; j < Q; j++) {
			int nc; scanf ("%d",&nc);
			QL.push_back (nc);
		}
		bribe (0, 0);
		printf ("Case #%d: %d\n",i,minv);
	}

	return 0;
}
