#include <cstdio>

const int MAX = 1001;

int ncas, cas, n;
int a[MAX], b[MAX];

int main(){
	scanf("%d", &ncas);
	while (ncas--){
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d %d", &a[i], &b[i]); 
		int res = 0;
		for (int i = 0; i < n; ++i)
			for (int j = i+1; j < n; ++j)
				if (a[i] < a[j] && b[i] > b[j])
					res++;
				else if (a[i] > a[j] && b[i] < b[j])
					res++;
		printf("Case #%d: %d\n", ++cas, res);
	}
	return 0;
}
