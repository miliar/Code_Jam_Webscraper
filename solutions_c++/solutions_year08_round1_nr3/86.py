#include <iostream>

using namespace std;

int	nCase, N;

void	compute(int N, int &A, int &B)
{
	if (!N)
	{
		A = 1;
		return ;
	}
	compute(N / 2, A, B);
	int tmp;

	tmp = 2 * A * B % 1000;
	A = A * A % 1000 + 5 * B * B % 1000;
	B = tmp;
	if (N & 1)
	{
		tmp = (A + 3 * B) % 1000;
		A = (3 * A + 5 * B) % 1000;
		B = tmp;
	}
}

int	main()
{
	cin >> nCase;
	for (int nowCase = 1; nowCase <= nCase; ++nowCase)
	{
		cin >> N;
		int A = 0, B = 0;
		compute(N, A, B);
		printf("Case #%d: ", nowCase);
		A = (2 * A + 999) % 1000;
		if (A < 10) printf("00%d\n", A); else
		if (A < 100) printf("0%d\n", A); else
		if (A < 1000) printf("%d\n", A);
	}
}
