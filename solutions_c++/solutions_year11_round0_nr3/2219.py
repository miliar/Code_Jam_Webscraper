#include <iostream>
#include <fstream>

using namespace std;

int N, S, T, R;
int A[1005];

int main()
{
	#ifdef _PRJ
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	#endif
	#ifdef _CP
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	#endif
	#ifdef _CXT
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	#endif
	int TestCase;
	cin >> TestCase;
	for (int t = 1; t <= TestCase; ++ t)
	{
		cout << "Case #" << t << ": ";
		cin >> N;
		for (int i = 1; i <= N; ++ i)
			cin >> A[i];
		S = 0, T = 0, R = 100000000;
		for (int i = 1; i <= N; ++ i)
			S ^= A[i], T += A[i], R = min(R, A[i]);
		if (S == 0)
			cout << T - R << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}