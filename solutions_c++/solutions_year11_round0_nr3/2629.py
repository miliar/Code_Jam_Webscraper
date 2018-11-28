#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int n, k, a, tab[1005], minimum, suma;

bool wczytaj()
{
    suma = 0;
    minimum = 1000000007;
    int sum = 0;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
    {
        scanf("%d", &a);
        sum ^= a;
        suma += a;
        minimum = min(minimum, a);
    }
    return sum == 0;
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int i=0; i<tests; i++)
	{
		printf(wczytaj() ? "Case #%d: %d\n" : "Case #%d: NO\n", i+1, suma - minimum);
	}

	return 0;
}
