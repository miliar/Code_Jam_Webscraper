#include <iostream>
#define forn(i, n) for(int i = 0; i < int(n); i++)
using namespace std;
int c[2000];
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	cin >> tests;
	forn(test, tests){
		int n;
		cin >> n;
		int sum = 0;
		int mn = 1000 * 1000 * 1000;
		int xor = 0;
		forn(i, n){
			scanf("%d", &c[i]);
			xor ^= c[i];
			mn = min(mn, c[i]);
			sum += c[i];
		}
		sum -= mn;
		printf("Case #%d: ", test + 1);
		if(xor != 0){
			printf("NO\n");
		}else{
			printf("%d\n", sum);
		}
	}
	return 0;
}