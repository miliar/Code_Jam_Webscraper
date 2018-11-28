#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	char c,s[1000];
	int i,N,L,cnt;
	scanf("%d",&N);
	for (int testcase=1;testcase<=N;testcase++) {
		scanf("%s",s);
		L = strlen(s);
		if (next_permutation(s,s+L)) {
			printf("Case #%d: %s\n",testcase,s);
		} else {
			sort(s,s+L);
			for (i=0;i<L;i++) if (s[i] != '0') break;
			swap(s[0],s[i]);
			printf("Case #%d: %c0%s\n",testcase,s[0],&s[1]);
		}
	}
	return 0;
}
