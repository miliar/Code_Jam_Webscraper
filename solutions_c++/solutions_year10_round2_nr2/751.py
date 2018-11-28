#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

int m, t, n, a[1000], b[1000], T, k, q, f, u[1000];
double d[1000], ff, eps = 1e-8;

int main(){
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++){
		int cnt = 0, ans = 0, max = -9999;
		printf("Case #%d: ", tt);
		for (int i=0; i<1000; i++){
			d[i] = 0.0;
			u[i] = 1;
		}
		scanf("%d%d%d%d", &n, &k, &f, &t);
		ff = f;
		for (int i=0; i<n; i++)
			scanf("%d", &a[i]);
		for (int i=0; i<n; i++)
			scanf("%d", &b[i]);
		for (int i=0; i<n; i++)
			if ((double)((ff-a[i])/b[i])<=t){
				d[i] = (double)((ff-a[i])/b[i]);
				ans++;
			}
		if (ans<k) {printf("IMPOSSIBLE\n"); continue;}
		else
		for (int r=0; r<k; r++){
			max = -9999;
			for (int i=0; i<n; i++)
				if ((a[i]>max) && (u[i]!=0) && d[i]>eps){
					max =a[i];
					q = i;
				}
			u[q] = 0;
//			printf("%d\n", max);
//			printf("%d\n", a[q]);
			for (int i=0; i<n; i++)
				if (a[i]>a[q]){
					if (d[i] < eps)
						cnt++;
					else {
						if (b[q]>b[i])
							if ((((double)(a[i]-a[q])/(b[q]-b[i])) + (ff - (a[i]+(double)((a[i]-a[q])/(b[q]-b[i]))*b[i]))/b[i])>t)
								cnt++;
					}
				}
		}
		printf("%d\n", cnt);
	}
	return 0;
}
