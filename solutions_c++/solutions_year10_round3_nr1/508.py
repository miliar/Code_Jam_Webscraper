//be name oo
#include <cstdio>

const int MAX_N = 1000 + 10;

int n;
int a[MAX_N];
int b[MAX_N];

int main(){
	int t;
	scanf("%d", &t);
	for(int k = 1; k <= t; k++){
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
			scanf("%d %d", &a[i], &b[i]);
		int ans = 0;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				if(a[i] < a[j] && b[j] < b[i])
					ans++;
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}
