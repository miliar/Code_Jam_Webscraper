#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

int T, m, n, a[100000], need, poww, temp, fi, ww;

int main(){
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++){
		printf("Case #%d: ", tt);
		scanf("%d", &m);
		int sum = 0;
		poww = 1;
		for (int i=0; i<m; i++)
			poww *=2;
		n = m;
		ww = poww;
		for (int i=0; i<poww; i++)
			scanf("%d", &a[i]);
		for (int i=0; i<poww-1; i++)
			scanf("%d", &temp);
		for (int r=0; r<m; r++){
			need = 0;
			for (int j=0; j<ww/poww; j++){
				fi = 0;
				for (int i=poww*(j); i<poww*(j+1); i++)
					if (a[i]<n){
						fi = 1;
					}
				if (fi==1) {sum++;}// printf("r = %d\n", r);}
				for (int k=poww*j; k<poww*(j+1); k++)
					a[k]++;
			}
			poww/=2;
		}
		printf("%d\n", sum);
	}
	return 0;
}
