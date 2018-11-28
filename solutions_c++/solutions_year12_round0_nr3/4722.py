#include <stdio.h>
#include <set>

using namespace std;
int pow10[] = { 1, 10, 100, 1000, 1000, 10000, 100000, 1000000, 10000000, 100000000};

int rotate(int n, int num_digit) {
	return n/10 + (n%10)*pow10[num_digit-1];
}

int A, B; 

int count(int n) {
	int res = 0;
	while(n) {res++; n/=10; }
	return res;
}

int solve(int n) {
	int num_digit = count(n);
	set<int> s; s.insert(n);

	int res = 0;
	int t = n;
	while(true) {
		t = rotate(t, num_digit);
		if(s.count(t)) break;
		s.insert(t);
		if(A<=t &&t<n) res++;
	}

	return res;
}

int main(void) {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int T; scanf("%d", &T);

	for(int tc=1; tc<=T; tc++) {
		int res = 0;
		scanf("%d %d", &A, &B);

		for(int i=A;i<=B;i++) {
			res += solve(i);
		}
		printf("Case #%d: %d\n", tc, res);
	}	
	return 0;
}