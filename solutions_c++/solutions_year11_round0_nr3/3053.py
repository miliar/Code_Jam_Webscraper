#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;


int TC, n, i, j;
int a[20], sum;

int main(void){
	scanf("%d", &TC);
	for (int t = 1; t <= TC; t++){
		scanf("%d", &n);
		sum = 0;
		for (i = 0; i < n; i++){
			scanf("%d", &a[i]);
			sum += a[i];
		}
		
		int lim = (1 << n);
		bool flag = 0;
		int ans = 0;
		for (int x = 1; x < lim-1; x++){
			int s1, s2, tot;
			s1 = s2 = tot = 0;
			for (i = 0; i < n; i++){
				if (x & (1 << i)){
					s1 ^= a[i];
					tot += a[i];
				} else
					s2 ^= a[i];
			}
			if (s1 == s2){
				flag = 1;
				ans = max(tot, ans);
			}
		}
		
		printf("Case #%d: ", t);
		if (!flag)
			printf("NO\n");
		else
			printf("%d\n", ans);
	}
	
	return 0;

}







		
		
		
		
		