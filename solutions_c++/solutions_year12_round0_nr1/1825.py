#include<cstdio>
#define NMAX 105
using namespace std;

char A[3][NMAX] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char B[3][NMAX] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
char Sub[256];

int main()
{
	Sub[' '] = ' ';
	Sub['q'] = 'z';
	Sub['z'] = 'q';
	for(int i = 0; i < 3; ++i)
		for(int j = 0; A[i][j]; ++j)
			Sub[A[i][j]] = B[i][j];

	freopen("A-small-attempt2.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("A.small3.out", "w", stdout);

	int T;
	scanf("%d ", &T);
	for(int t = 1; t <= T; ++t)
	{
		char S[NMAX];
		gets(S);
		for(int i = 0; S[i]; ++i)
			S[i] = Sub[S[i]];
		printf("Case #%d: %s\n", t, S);
	}

	return 0;
}
