#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define MAXN 50010

int k, n;
int res;
char a[MAXN];
char tmp[MAXN];
int b[20];

int compress() {
	int cur, i, val=0;
	cur=-1;
	for (i=0; i<n; i++) {
		if ((int)tmp[i]!=cur)
			val++;
		cur=(int)tmp[i];
	}
	return val;
}

void solve() {
	int i, j;
	for (i=0; i<n/k; i++)
		for (j=0; j<k; j++)
			tmp[i*k+j]=a[i*k+b[j]];
	res=min(compress(),res);
}

int main () {
	int t, c;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	for (scanf("%d", &t), c=1; c<=t; c++) {
		printf("Case #%d: ", c);
		scanf("%d", &k);
		gets(a);
		gets(a);
		n=strlen(a);
		res=n;

		for (int i=0;i<k;i++)	b[i]=i;
		do {
			solve();
		} while (next_permutation(b,b+k));

		printf("%d\n",res);
	}
	return 0;
}