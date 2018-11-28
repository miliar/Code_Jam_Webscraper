#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("ans.out", "w", stdout);
	int i, T, cas = 1;
	int n, k;
	scanf("%d", &T);
	while (T--){
		scanf("%d %d", &n, &k);
		i = 0;
		while (k & 1){
			i++;
			k /= 2;
		}
		printf("Case #%d: ", cas++);
		if (i >= n){
			puts("ON");
		}
		else puts("OFF");
	}
	return 0;
}

