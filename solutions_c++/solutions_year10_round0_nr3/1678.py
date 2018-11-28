#include <iostream>
#include <iterator>

using namespace std;


unsigned long long	a[1002];
unsigned long long	value[1002];
unsigned long long	inc[1002];

void
fill(int n, unsigned long long k) {
	int		i, j, in;
	unsigned long long	s;

	for (i=0;i<n;i++) {
		s = 0;
		in = 0;
		j = i;

		while ((s+a[j]) <= k) {
			s += a[j];
			j = (j+1) % n;
			in++;
			if (j == i) break;
		}
		inc[i] = in;
		value[i] = s;
	}
}

unsigned long long
get(unsigned long long r, int n, unsigned long long k) {
	int		start = 0;
	unsigned long long	i, ans = 0;

	fill (n, k);

	for (i=0;i<r;i++) {
		if (value[start]) {
			ans += value[start];
			start = (start + inc[start]) % n;
		}
		else
			break;
	}

	return ans;
		
}

int
main(void) {
	int		t, n, i, j;
	unsigned long long	r, k;

	cin >> t;

	for (i=0;i<t;i++) {
		cin >> r >> k >> n;
		for (j=0;j<n;j++) cin >> a[j];
		cout << "Case #" << (i+1) << ": " << get(r, n, k) << endl;
	}

	return 0;	
}
