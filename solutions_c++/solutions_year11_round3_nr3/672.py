#include <cstdio>

using namespace std;

int main(){
	int t, n, l, h, a[111];
	scanf("%d", &t);
	bool found;
	for (int T = 1; T <= t; T++){
		scanf("%d%d%d", &n, &l, &h);
		
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
			
		for (int i = l; i <= h; i++){
			found = true;
			for (int j = 0; j < n; j++)
				if (a[j] % i != 0 && i % a[j] != 0)
					found = false;
			if (found){
				printf("Case #%d: %d\n", T, i);
				break;
			}
		}
		
		if (!found){
			printf("Case #%d: NO\n", T);
		}
	}
}
