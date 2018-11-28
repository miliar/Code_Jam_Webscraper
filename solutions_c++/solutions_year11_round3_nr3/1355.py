#include <cstdio>

using namespace std; 
int f[1000];
int T, n, l, h; 
int main(){
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\GoogleJam\\input\\C-small-attempt41.in","r",stdin); 
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\GoogleJam\\input\\c.out","w",stdout); 
	scanf("%ld", &T); 
	for (int cnt = 1; cnt <= T; cnt ++) {
		scanf("%ld %ld %ld", &n, &l, &h); 
		for (int i = 0; i < n; i++) scanf("%ld", &f[i]); 
		printf("Case #%ld: ", cnt);  
		bool yes; 
		bool no = true; 
		for (int k = l; k <= h; k++) {
			yes = true; 
			for (int i = 0; i < n; i++) {
				if (f[i]%k !=0 && k%f[i]!=0) {
					yes = false; 
					break;
				}
			}
			if (yes) {printf("%ld\n", k); no = false; break;} 
		}
		if (no) printf("NO\n"); 
	}
	//fclose(stdout); 
}