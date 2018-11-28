#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int t;
	scanf("%i", &t);
	for(int i = 0; i < t; i++) {
		printf("Case #%i: ", i + 1);
		int n, s, p;
		scanf("%i%i%i", &n, &s, &p);
		int c1 = 0, c2 = 0;
		for(int j = 0; j < n; j++) {
			int num;
			scanf("%i", &num);
			if(num >= 3 * p - 2) c1++;
			else if(num >= 3 * p - 4 && num >= 2) c2++;
			/*
			if((num + 2) / 3 >= p) {
				if(num >= 1) c1++;
			} else if((num + 4) / 3 >= p) {
				if(num >= 2) c2++;
			}*/
		}
		printf("%i\n", c1 + min(s, c2));
	}
}

