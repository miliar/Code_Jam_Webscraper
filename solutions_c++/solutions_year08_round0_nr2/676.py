#include <cstdio>
#include <algorithm>
using namespace std;

int la[100], lb[100], aa[100], ab[100];

int solve(int *arr, int *dep, int narr, int ndep){
	sort(arr, arr+narr);
	sort(dep, dep+ndep);

	int ap = 0, dp = 0;

	int ret = 0;

	while (ap < narr && dp < ndep){
		if (arr[ap] <= dep[dp])
		{
			ap++;
			dp++;
		}
		else
		{
			ret++;
			dp++;
		}
	}

	if (dp < ndep) ret += ndep - dp;
	
	return ret;
}

int main(){
	int N;
	scanf("%d", &N);
	for (int tc=1; tc<=N; tc++){
		int t,na,nb;
		scanf("%d %d %d", &t, &na, &nb);
		
		for (int i=0; i<na; i++){
			int h1,h2,m1,m2,x;
			scanf("%d%c%d %d%c%d", &h1, &x,&m1, &h2, &x, &m2);
//			printf("read %d %d %d %d\n", h1, m1, h2, m2);
			la[i] = 60*h1 + m1;
			ab[i] = 60*h2 + m2 + t;
		}
		for (int i=0; i<nb; i++){
			int h1,h2,m1,m2,x;
			scanf("%d%c%d %d%c%d", &h1, &x,&m1, &h2, &x, &m2);
//			printf("case 2 read %d %d %d %d\n", h1, m1, h2, m2);
			lb[i] = 60*h1 + m1;
			aa[i] = 60*h2 + m2 + t;
		}

/*		for (int i=0; i<na; i++){
			printf("a->b %d:%d %d:%d\n", la[i]/60, la[i]%60, ab[i]/60, ab[i]%60);
		}
		for (int i=0; i<nb; i++){
			printf("b->a %d:%d %d:%d\n", lb[i]/60, lb[i]%60, aa[i]/60, aa[i]%60);
		}
*/

		printf("Case #%d: %d %d\n", tc, solve(aa,la,nb,na), solve(ab,lb,na,nb));
	}
}
