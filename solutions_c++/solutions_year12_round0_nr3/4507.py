#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int ipow(int n, int r)
{
	return r==0?1:n*ipow(n, r-1);
}

int number_of_length(int n)
{
	return (n > 0)?1+number_of_length(n/10):0;
}

int shift(int n, int len)
{
	int t = ipow(10, len-1);
	int head = n/t;
	int tail = n%t;
	return tail*10 + head;
}

bool check(int n, int m)
{
	int len = number_of_length(m);
	for (int i = 0; i < len; i++) {
		if (n == m)
			return true;
		m = shift(m, len);
	}
	return false;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int ans = 0;
		int A, B;
		cin >> A >> B;
		for (int m = A+1; m <= B; m++)
			for (int n = A; n < m; n++)
				if (n != m && check(n, m)) {
					//printf("%d %d\n", n, m);
					ans++;
				}

		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}
