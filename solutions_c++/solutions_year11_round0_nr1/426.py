#include <cstdio>
using namespace std;

int TC = 1, T, NC = 1, N, P;
char R;

int main ()
{
	freopen("small.in", "r", stdin);
    for (scanf ("%d", &T); TC <= T; TC++)
    {
		int A = 1, B = 1, Y = 0;
		for (scanf ("%d", &N); NC <= N; NC++)
		{
			scanf ("%c %d", &R, &P);
			if R=='O'
				Y+=P>A ? P-A : A-P;
			else if R=='B'
				Y+=P>B ? P-B : B-P;
		}
			printf ("Case #%d: %d", TC, Y);
    }
	fclose(stdin);
    return 0;
}
