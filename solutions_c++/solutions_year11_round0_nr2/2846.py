#include <stdio.h>
#include <string.h>

int c, d, n;
struct Combine {
	char cb1, cb2, cb;
} sc[50];
struct Oppose {
	char op1, op2;
} so[50];

char str[200], ans[200];
int len, l;

void comb() {
	int x=l;
	for (int i=0; i<c; i++) {
		if ((ans[x-2]==sc[i].cb1&&ans[x-1]==sc[i].cb2)||
			(ans[x-1]==sc[i].cb1&&ans[x-2]==sc[i].cb2)) {
			ans[x-2]=sc[i].cb;
			l--;
			return;
		}
	}
}
void opp() {
	int x=l;
	for (int i=0; i<d; i++) {
		if (ans[x-1]==so[i].op1) {
			for (int j=0; j<=x-2; j++)
				if (ans[j]==so[i].op2) {
					l=0;
					return;
				}
		}
		if (ans[x-1]==so[i].op2) {
			for (int j=0; j<=x-2; j++)
				if (ans[j]==so[i].op1) {
					l=0; 
					return;
				}
		}
	}
}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int cas, k;
	scanf("%d", &cas);
	for (k=1; k<=cas; k++) {
		scanf("%d", &c);
		for (int i=0; i<c; i++)
			scanf(" %c%c%c", &sc[i].cb1, &sc[i].cb2, &sc[i].cb);
		scanf("%d", &d);
		for (int i=0; i<d; i++) 
			scanf(" %c%c", &so[i].op1, &so[i].op2);
		scanf("%d%s", &len, str);
		l=1;
		ans[0]=str[0];
		for (int i=1; i<len; i++) {
			ans[l++]=str[i];
			comb();
			opp();
		}
		printf("Case #%d: [", k);
		if (l==0) printf("]\n");
		else {
			printf("%c", ans[0]);
			for (int i=1; i<l; i++)
				printf(", %c", ans[i]);
			printf("]\n");
		}
	}
	return 0;
}
