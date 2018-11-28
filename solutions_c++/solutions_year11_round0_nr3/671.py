#include <iostream>
using namespace std;

int sum(int a, int b){
	int t = 0;
	for (int i = 0, j = 1; i <= 20; i++, j <<= 1){
		t += ((((a & j) >= 1) + ((b & j) >= 1)) == 1) * j;
	}
	return t;
}

int main(){
	int T, n;
	int S, minimum;
	int c[1050];
	
	cin >> T;
	for (int C = 1; C <= T; C++){
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> c[i];
			
		int t = 0;
		S = 0, minimum = 2147483647;
		for (int i = 0; i < n; i++){
			t = sum(t, c[i]);
			S += c[i];
			minimum = min(minimum, c[i]);
		}
		printf("Case #%d: ", C);
		if (t != 0){
			printf("NO");
		}
		else{
			printf("%d", S - minimum);
		}
		printf("\n");
	}
	return 0;
}
