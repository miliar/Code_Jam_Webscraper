#include <vector>
#include <set>
#include <cstdio>
using namespace std;
#define maxint ((1<<31)-1)

int k, result;
char *s, *t;
set<int> ix;
vector<int> p;
vector<bool> used;

void test() {
	int l = strlen(s);
	for (int i=0; i<l; i++) {
		int n = i/k, z = i%k;
		t[p[z]+n*k] = s[i];
	}
	t[l] = '\0';
	int r = 0;
	char last = '\0';
	for (int i=0; i<l; i++) {
		if (t[i]!=last) r++;
		last = t[i];
	}
	result = min(result,r); 
}

void perm(int level) {
	if (level==k) test();
	for (int i=0; i<k; i++) if (!used[i]) {
		used[i] = true;
		p[level] = i;
		perm(level+1);
		used[i] = false;
	}
}

int main() {
	s = (char *) malloc(2000*sizeof(char));
	t = (char *) malloc(2000*sizeof(char));
	int n;
	scanf("%d", &n);
	for (int ixn=1; ixn<=n; ixn++) {
		scanf("%d %s", &k, s);
		result = maxint;
		used.resize(k);
		for (int i=0; i<k; i++) used[i] = false;
		p.resize(k);
		for (int i=0; i<k; i++) ix.insert(i);
		perm(0);
		printf("Case #%d: %d\n", ixn, result);
	}

	return 0;
}
