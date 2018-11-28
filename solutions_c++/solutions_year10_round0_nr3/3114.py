#include<cstdio>
#define MAX 1024
using namespace std;

typedef struct c{
	int value;
	struct c *next;
}cel;
typedef long long int llu;
static cel v[MAX];
cel *ref;
int main () {
	int i, n, r, t, k, x, j, m, p;
	llu ans, cst;
	scanf("%d", &t);
	for (i = 0; i != t; i++) {
		ans = 0;
		scanf("%d %d %d", &r, &k, &n);		
		for (j = 0; j != n; j++) {
			scanf("%d", &x);
			v[j].value = x;
			v[j].next = &v[j+1];
		}
		ref = &v[0];
		v[j-1].next = &v[0];
	/*	for (j = 0; j < n*2; j++) {	
			printf("%d\n", ref->value);
			ref= ref->next;
		}*/
		for (m = 0; m != r; m++) {
			cst = 0;
			p = 0;
			while (cst + ref->value <= k && p < n) {
				p++;
				cst += ref->value;
				//printf("cst = %lld  value[] = %d\n",cst, ref->value);	
				ref = ref->next;
			}
			ans += cst;
		//	printf("Opa fecho 1 vagao: Ans %d = %lld\n\n", m, ans);
		}
		printf("Case #%d: %lld\n", i+1, ans);
	}
	return 0;
}
