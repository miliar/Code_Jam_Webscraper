#include <iostream>
using namespace std;
int main(){
	int T;
	scanf("%d", &T);
	for (int m = 0; m < T; ++m){
		int N, K;
		cin >> N >> K;
		if ((K + 1) % (1 << N) == 0)
			printf("Case #%d: ON\n", m+1);
		else 
			printf("Case #%d: OFF\n", m+1);
	}
	return 0;
}