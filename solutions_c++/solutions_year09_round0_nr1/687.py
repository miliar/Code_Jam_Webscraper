#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#include <iostream>

using namespace std;

int l, d, n;
char s[5000][15];
bool bad[5000], p[5000];

int main() {
	char c;
	scanf("%d%d%d\n",&l,&d,&n);
	for (int i=0; i<d; i++) {
		for (int j=0; j<l; j++) s[i][j] = getchar();
		getchar();
	}
	for (int test=1; test<=n; test++) {
		memset(bad,0,sizeof(bad));
		for (int i=0; i<l; i++) {
			if ((c=getchar()) != '(') {
				for (int j=0; j<d; j++) if (s[j][i] != c) bad[j] = 1;
			} else {
				memset(p,0,sizeof(p));
				while ((c=getchar()) != ')')
					for (int j=0; j<d; j++) if (s[j][i] == c) p[j] = 1;
				for (int j=0; j<d; j++) if (!p[j]) bad[j] = 1;
			}
		}
		int ans = 0; for (int i=0; i<d; i++) if (!bad[i]) ans++;
		printf("Case #%d: %d\n",test,ans);
		getchar();
	}
}
