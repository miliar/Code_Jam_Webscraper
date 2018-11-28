#include <cstdio>
#include <algorithm>

using namespace std;
unsigned t, d, T, A, B, V;
unsigned vA[8], vB[8], vV[8], L;
unsigned long long C;

void put(unsigned value, unsigned * arr, bool compute)
{
	if (compute)
	{
		unsigned auxiliary = value;
		unsigned size = 0;
		while (auxiliary)
		{
			++size;
			auxiliary /= 10;
		}
		L = size;
	}
	
	for (unsigned size = L - 1; value; --size) 
	{
		arr[size] = value % 10;
		value /= 10;
	}
}

void read()
{
	scanf("%u%u", &A, &B);
}

inline unsigned modulus(unsigned v)
{
	return v < L? v: v - L;
}

bool compareLessEqual(unsigned * v1, unsigned p1, unsigned * v2, unsigned p2)
{
	if (v1[modulus(p1)] == 0 || v2[modulus(p2)] == 0)
		return false;

	for (unsigned s = 0, i = modulus(p1), j = modulus(p2); s < L; ++s, i = modulus(i + 1), j = modulus(j + 1))
	{
		if (v1[i] < v2[j])
		{
			return true;
		}

		if (v1[i] > v2[j])
		{
			return false;
		}
	}

	return true;
}

bool compareEqual(unsigned * v1, unsigned p1, unsigned * v2, unsigned p2)
{
	for (unsigned s = 0, i = modulus(p1), j = modulus(p2); s < L; ++s, i = modulus(i + 1), j = modulus(j + 1))
	{
		if (v1[i] != v2[j])
		{
			return false;
		}
	}

	return true;
}


void printPermutation(unsigned * v1, unsigned p1)
{
	for (unsigned s = 0, i = modulus(p1); s < L; ++s, i = modulus(i + 1))
	{
		printf("%u", v1[i]);
	}
}

void solve()
{
	put(A, vA, true);
	put(B, vB, false);

	if (L <= 1)
		return;

	for (V = A; V <= B; ++V)
	{
		put(V, vV, false);

		for (d = 1; d < L; ++d)
		{
			if (compareLessEqual(vA, 0, vV, 0) && compareLessEqual(vV, 0, vV, d) && !compareEqual(vV, 0, vV, d) && compareLessEqual(vV, d, vB, 0))
			{
				++C;
				
				/*

				printPermutation(vA, 0);
					printf(" ");
				printPermutation(vV, 0);
					printf(" ");
				printPermutation(vV, d);
					printf(" ");
				printPermutation(vB, 0);
					printf("\n");

				*/
			}
		}
	}
}

void write()
{
	printf("Case #%u: %llu\n", t, C);
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	
	/*

	while (T--)
	{
		unsigned a, b, c, d;
		scanf("%u%u%u%u", &a, &b, &c, &d);
		if (!(a <= b && b < c && c <= d))
			printf("NO! %u %u %u %u", a, b, c, d);
	}

	*/

	for (t = 1; t <= T; ++t)
	{
		read();
		solve();
		write();
		C = 0;
	}

	return 0;
}