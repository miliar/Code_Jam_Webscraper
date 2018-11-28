#include <iostream>

using namespace std;

int A[800], B[800];

int main()
{
	int tt, n;
	
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
		
	cin >> tt;
	
	for (int ii = 1; ii <= tt; ++ii)
	{
		cin >> n;
		
		for (int i = 0; i < n; ++i) cin >> A[i];
		for (int i = 0; i < n; ++i) cin >> B[i];
		
		sort(A, A + n);
		sort(B, B + n);
		
		int s = 0;
		
		for (int i = 0; i < n; ++i)
			s += A[i] * B[n - i - 1];
		
		printf("Case #%d: %d\n", ii, s);
	}
}
