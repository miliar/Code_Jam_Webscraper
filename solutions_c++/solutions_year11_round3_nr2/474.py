#include<cstdio>
#include<algorithm>

using namespace std;

const int MAXN = 1100000;

int stars[MAXN];
int l, t, n, c;

int simulate() {
	if(l == 0) {
		int res = 0;
		for(int i = 0; i < n; i++)
			res += stars[i];

		return res;
	}
	else {
		int res = 1000000000;
		// place to constroy the booster
		for(int i = 0; i < n; i++) {
//			printf("Booster at %d\n", i);

			int total = 0;
			for(int j = 0; j < i; j++)
				total += stars[j];

//			printf("Until star[%d] => %d\n", i, total);

			if(total > t) {
				total += (stars[i]/2);
			}
			else {
				if(total+stars[i] > t) {
					int aux = total;
					aux += (t - total);
					aux += (total+stars[i]-t)/2;
					total = aux;
				}
				else
					total += stars[i];
			}

//			printf("After star[%d] => %d\n", i, total);

			for(int j = i+1; j < n; j++)
				total += stars[j];

//			printf("Final => %d\n\n", total);

			res = min(res, total);
		}

		if(l == 1)
			return res;

		// in small case, l = 2
		// places to constroy the booster
		for(int i = 0; i < n; i++) {
			for(int j = i+1; j < n; j++) {
//				printf("Booster at %d\n", i);

				int total = 0;
				for(int k = 0; k < i; k++)
					total += stars[k];

//				printf("Until star[%d] => %d\n", i, total);
	
				if(total > t) {
					total += (stars[i]/2);
				}
				else {
					if(total+stars[i] > t) {
						int aux = total;
						aux += (t - total);
						aux += (total+stars[i]-t)/2;
						total = aux;
					}
					else
						total += stars[i];
				}

//				printf("After star[%d] => %d\n", i, total);

				for(int k = i+1; k < j; k++)
					total += stars[k];

				if(total > t) {
					total += (stars[j]/2);
				}
				else {
					if(total+stars[j] > t) {
						int aux = total;
						aux += (t - total);
						aux += (total+stars[j]-t)/2;
						total = aux;
					}
					else
						total += stars[j];
				}

				for(int k = j+1; k < n; k++)
					total += stars[k];

//				printf("Final => %d\n\n", total);

				res = min(res, total);
			}
		}

		return res;
	}
}

int main() {
	int T = 0;
	scanf("%d", &T);

	for(int caseNum = 1; caseNum <= T; caseNum++) {
		l = t = n = c = 0;
		scanf("%d %d %d %d", &l, &t, &n, &c);

		for(int i = 0; i < c; i++) {
			int a = 0;
			scanf("%d", &a);
			for(int j = 0; (c*j)+i < n; j++)
				stars[(c*j)+i] = a*2;
		}

//		for(int i = 0; i < n; i++)
//			printf("[%d] = %d; ", i, stars[i]);
//		printf("\n");

		printf("Case #%d: %d\n", caseNum, simulate());
	}

	return 0;
}
