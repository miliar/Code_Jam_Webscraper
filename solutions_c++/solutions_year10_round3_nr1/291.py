#include <cstdio>

int a[1010], b[1010], n, t, cnt, total;

int main(){
	scanf("%d", &t);
	for(cnt=1; cnt<=t; cnt++){
		total= 0;
		scanf("%d", &n);
		for(int i=0; i<n; i++){
			scanf("%d%d", a+i, b+i);
		}
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
				if(a[i]<a[j] && b[i]>b[j])
					total++;
		printf("Case #%d: %d\n", cnt, total);
	}
}
