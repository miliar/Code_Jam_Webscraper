#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;

const char	*sign	=	"welcome to code jam";
const int	MAXL	=	500 + 10;
const int	L		=	20;

char	s[MAXL];
int		F[L];
int		T;

int answer ()
{
	gets (s);
	memset (F, 0, sizeof (F));
	F[0] = 1;

	for (int i = 0; i < strlen (s); ++i)
		for (int j = 18; j >= 0; --j)
			if (s[i] == sign[j])
				F[j + 1] = (F[j + 1] + F[j]) % 10000;

	return F[19];
}

int main()
{
	freopen ("in.txt", "r", stdin);
	freopen ("ou.txt", "w", stdout);

	scanf ("%d\n", &T);
	for (int i = 1; i <= T; ++i)
		printf ("Case #%d: %04d\n", i, answer ());

	return 0;
}
