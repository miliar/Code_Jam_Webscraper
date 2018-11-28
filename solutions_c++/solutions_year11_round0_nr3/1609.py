#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int T;
	cin >> T;
	for( int t = 1; t <= T; ++t ){
		int N;
		cin >> N;
		int m = 10000000, sum = 0, x = 0;
		int c;
		while(N--){
			cin >> c;
			m <?= c;
			sum += c;
			x ^= c;
		}
		printf("Case #%d: ", t);
		if (x) printf("NO\n");
		else printf("%d\n", sum - m);
	}
}
