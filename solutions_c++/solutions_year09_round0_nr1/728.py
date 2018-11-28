#include <stdio.h>
#define ML 15
#define MD 5001
int L, D;
char d[MD][ML], str[ML*30];
int ch[ML];
void process()
{
	int r, i, j;

	r = 0;
	for (i = 0; i < D; i++) {
		for (j = 0; j < L; j++) {
			if (!(ch[j]&(1<<(d[i][j]-'a')))) break;
		}
		r += j==L;
	}
	printf("%d\n", r);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, t, i, p, v;

	scanf("%d%d%d",&L,&D,&T);
	for (i = 0; i < D; i++) scanf("%s",d[i]);
	for (t = 1; t <= T; t++) {
		scanf("%s",str);
		p = 0; v = 0;
		for (i = 0; str[i]; i++) {
			if (str[i] == '(') {ch[p] = 0; v++;}
			else if (str[i] == ')') {p++; v--;}
			else if (v) ch[p] |= 1<<(str[i]-'a');
			else ch[p++] = 1<<(str[i]-'a');
		}
		printf("Case #%d: ", t);
		process();
	}
	return 0;
}