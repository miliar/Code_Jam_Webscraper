#include <cstdio>
#include <vector>
#include <set>
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int ixt=0; ixt<T; ixt++) {
		printf("Case #%d: ", ixt+1);
		int k;
		scanf("%d", &k);
		vector<int> deck(k,0);
		set<int> s;
		for (int i=0; i<k; i++) s.insert(i);

		set<int>::iterator ix = s.begin();
		for (int i=1; i<k; i++) {
			int index = *ix;
			ix++; if (ix==s.end()) ix = s.begin();
			deck[index] = i;
			s.erase(index);
			//for (int j=0; j<k; j++) fprintf(stderr, "%d ", deck[j]);
			//fprintf(stderr, "\n");
			for (int j=0; j<i; j++) {
				ix++;
				if (ix==s.end()) ix = s.begin();
			}
		}
		deck[*s.begin()] = k;

		int n;
		scanf("%d", &n);
		for (int i=0; i<n; i++) {
			int a;
			scanf("%d", &a);
			printf("%d", deck[a-1]);
			if (i+1!=n) printf(" ");
		}
		printf("\n");
	}

	return 0;
}
