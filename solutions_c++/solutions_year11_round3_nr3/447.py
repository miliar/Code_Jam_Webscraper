#include<cstdio>
#include<vector>

using namespace std;

int main() {
	int T = 0;
	scanf("%d", &T);

	for(int caseNum = 1; caseNum <= T; caseNum++) {
		int n = 0, l = 0, h = 0;
		scanf("%d %d %d", &n, &l, &h);

		vector<int> notes;

		for(int i = 0; i < n; i++) {
			int x = 0;
			scanf("%d", &x);
			notes.push_back(x);
		}

		printf("Case #%d: ", caseNum);

		bool printed = false;
		for(int i = l; i <= h && !printed; i++) {
			bool possible = true;
			for(int j = 0; j < n && possible; j++) {
				if((notes[j] % i != 0) && (i % notes[j] != 0))
					possible = false;
			}
			if(possible) {
				printf("%d\n", i);
				printed = true;
			}
		}

		if(!printed)
			printf("NO\n");
	}

	return 0;
}
