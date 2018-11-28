#include <cstdio>
#include <cstring>

using namespace std;

int nprison, nrelease, ans;
int rls[10];
bool occupied[105];

int calc() {
	memset(occupied, true, sizeof(occupied));

	int res = 0;
	for (int j, i = 0; i < nrelease; i++) {
		occupied[ rls[i] ] = false;

		j = rls[i] - 1;
		while (j >= 1 && occupied[j]) {
			j--;
			res++;
		}
		j = rls[i] + 1;
		while (j <= nprison && occupied[j]) {
			j++;
			res++;
		}
	}

	return res;
}//calc

void perm(int k) {
	if (k == nrelease) {
		/*for (int i = 0; i < nrelease; i++) {
			printf("%4d", rls[i]);
		}
		printf("\n");*/
		int n = calc();
		if (n < ans) ans = n;
		return;
	}

	perm(k + 1);
	int tmp;
	for (int i = k + 1; i < nrelease; i++) {
		tmp = rls[k]; rls[k] = rls[i]; rls[i] = tmp;
		perm(k + 1);
		tmp = rls[k]; rls[k] = rls[i]; rls[i] = tmp;
	}
}//perm

int main() {
	int nCase;

	scanf("%d", &nCase);
	for (int t = 1; t <= nCase; t++) {
		scanf("%d %d", &nprison, &nrelease);
		for (int i = 0; i < nrelease; i++) {
			scanf("%d", &rls[i]);
		}

		ans = 1000000000;
		perm(0);
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}
