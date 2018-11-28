#include <stdio.h>
#include <vector>

using namespace std;

vector <int> kind, best;
vector < vector <int> > likes;
int n, m, ans;

void all(int i, int n) {
	int j, k;
	if (i == n) {
		for (j=0; j < m; j++) {
			for (k=0; k < likes[j].size(); k++) {
				if ((likes[j][k] < 0 && kind[-likes[j][k]-1] == 1) || (likes[j][k] > 0 && kind[likes[j][k]-1] == 0))
					break;
			}
			if (k == likes[j].size())
				return;
		}
		int cost = 0;
		for (j=0; j < n; j++)
			cost += kind[j];
		if (ans == -1 || cost < ans) {
			best = kind;
			ans = cost;
		}
	}
	else {
		kind[i] = 0, all(i+1,n);
		kind[i] = 1, all(i+1,n);
	}
}

int main() {
	int cases, T = 1;
	int i, j, k, t, type;
	
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d %d",&n,&m);
		likes = vector < vector <int> > (m);
		kind = vector <int> (n);
		best = vector <int> (n);
		
		for (i=0; i < m; i++) {
			scanf("%d",&t);
			likes[i] = vector <int> (t);
			for (j=0; j < t; j++) {
				scanf("%d %d",&likes[i][j],&k);
				if (k)
					likes[i][j] = -likes[i][j];
			}
		}
		
		ans = -1;
		all(0,n);
		
		printf("Case #%d:",T++);
		if (ans == -1)
			puts(" IMPOSSIBLE");
		else {
			for (i=0; i < n; i++)
				printf(" %d",best[i]);
			puts("");
		}
	}
	
	return 0;
}
