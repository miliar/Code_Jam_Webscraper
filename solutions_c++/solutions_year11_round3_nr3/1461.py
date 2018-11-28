#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;
/*int gcd(int a, int b){
	if(b == 0) return a;
	return gcd(b, a % b);
}

int lcm(int a, int b){
	return abs(a * b) / gcd(a, b);
}
*/
int main(){
	FILE *f = fopen("out.txt", "w");
	int T = 0, c = 0;
	cin >> T;
	while(c++ < T){
		int n = 0, l = 0, h = 0;
		cin >> n >> l >> h;
		int numbs[n];
		fill_n(numbs, n, 0);
		for(int i = 0; i < n; i++) cin >> numbs[i];
		sort(numbs, numbs + n);
		int past = 0;
		/*for(int i = 1; i < n; i++){
			if(!(past >= l && past <= h) || numbs[i] % past != 0)
				past = lcm(past, numbs[i]);
		}*/
		for(int i = l; i <= h && past == 0; i++){
			bool go = true;
			for(int j = 0; j < n && go; j++){
				if(numbs[j] % i == 0 || i % numbs[j] == 0)
					continue;
				else
					go = false;
			}
			if(go)
				past = i;
			
		}
		//if(past >= l && past <= h){
		if(past != 0){
			printf("Case #%d: %d\n", c,  past);
			fprintf(f, "Case #%d: %d\n", c,  past);
		}else{
			printf("Case #%d: NO\n", c);
			fprintf(f, "Case #%d: NO\n", c);
		}
	}
	return 0;
}