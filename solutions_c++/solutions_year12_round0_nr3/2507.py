#include <iostream>
using namespace std;

bool flag[2000001];

int main() {
	int t;
	
	scanf("%d", &t);
	int a, b;
	
	for (int k = 0; k < t; k++) {
		scanf("%d%d", &a, &b);
		
		int res = 0;
		for (int n = a; n < b; n++) {
			int tmp = n;
			int dig = 0;
			int t1 = 1;
			int t2 = 10;
			
			while (tmp > 0) {
				tmp /= 10;
				t1 *= 10;
				dig++;
			}
			t1 /= 10;
			
			//printf("(%d, %d)\n", t1, t2);
			for (int i = 0; i < dig; i++) {
				int x = n % t1;
				int y = n / t1;
				
				int m = x * t2 + y;
				
				if (m > n && m <= b && flag[m] == false) {
				 res++;
				 flag[m] = true;
				}
				t1 /= 10; 
				t2 *= 10;
			}
			
			
			t2 /= 100;
			t1 = 10;
		//	printf("(%d, %d)\n", t1, t2);
			
			for (int i = 0; i < dig; i++) {				
				int x = n % t2;
				int y = n / t2;
				
				int m = x * t1 + y;

				if (m > n && m <= b && flag[m] == true) {
				 flag[m] = false;
				}
				
				t1 *= 10; 
				t2 /= 10;
			}

		}
		
		printf("Case #%d: %d", k+1, res);
		if (k < t - 1) printf("\n");
	}
	
	return 0;
}