#include <cstdio>
#include <algorithm>

using namespace std;

int t, n, s, p, r[100], o;

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d\n", &t);
	for(int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		scanf("%d%d%d", &n, &s, &p);
		for(int j = 0; j < n; j++){
			scanf("%d", &r[j]);
		}
		sort(r, r + n);
		o = 0;
		for(int j = n - 1; j >= 0; j--){
			if (r[j] < 1){
				if (p == 0) o++;
			}else if (r[j] % 3 == 0){
				if (r[j] / 3 == p - 1){
					if (s){
						s--;
						o++;
					}
				}else if (r[j] / 3 >= p){
					o++;
				}
			}else if (r[j] % 3 == 1){
				if (r[j] / 3 >= p - 1){
					o++;
				}
			}else{
				if (r[j] / 3 == p - 2){
					if (s){
						s--;
						o++;
					}
				}else if(r[j] / 3 > p - 2){
					o++;
				}
			}
		}
		printf("%d\n", o);
	}
	return 0;
}
