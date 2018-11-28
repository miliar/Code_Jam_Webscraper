#include <stdio.h>

char rule[100][5];
char opp[100][5];
char a[1000];
char st[10000];
int m, C, D, N;

char check_rule(char x, char y) {
	int i;
	for(i=0;i<C;i++)
		if(rule[i][0]==x && rule[i][1]==y || 
			rule[i][0]==y && rule[i][1]==x)
			return rule[i][2];
	return 0;
}

bool check_opp(char x) {
	for(int i = 0; i < m-1; i++) {
		for(int j = 0; j < D;j++)
			if(opp[j][0] == x && opp[j][1] == st[i] ||
					opp[j][0]==st[i] &&opp[j][1] == x)
				return true;
	}
	return false;
}

int main(void) {
	int T, cs, i;
	scanf("%d", &T);
	for(cs=1;cs<=T;cs++){
		scanf("%d", &C);
		for(i=0;i<C;i++)
			scanf("%s", rule[i]);
		scanf("%d", &D);
		for(i=0;i<D;i++)
			scanf("%s", opp[i]);
		scanf("%d", &N);
		scanf("%s", a);
		m = 0;
		for(i=0;i<N;i++) {
			st[m++] = a[i];
			while (m>1 && check_rule(st[m-1], st[m-2])) {
				st[m-2] = check_rule(st[m-1], st[m-2]);
				--m;
			}
			if (m > 1 && check_opp(st[m-1]))
				m = 0;
		}
		printf("Case #%d: [", cs);
		fprintf(stderr, "Case #%d: [", cs);
		for(i=0;i<m;i++){
			printf("%c%s", st[i], i==m-1?"":", ");
			fprintf(stderr, "%c%s", st[i], i==m-1?"":", ");
		}
		printf("]\n");
		fprintf(stderr, "]\n");
	}
	return 0;
}
