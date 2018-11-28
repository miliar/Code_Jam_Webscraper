#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define fr(i, N) for(i = 0; i < (int)N; i++)
#define setContains(i,j) (((1<<j)&i) != 0)
#define MP make_pair
#define F first
#define S second
#define pb push_back
#define Eps 1e-11

char A[600];
int D[30][600], Mod = 10000;

void input()
{
	fgets(A, 600, stdin);
	int L = strlen(A);

	while (L > 0 && A[L-1] != 'm') A[--L] = 0;
}

void process()
{
	int i, j, k;
	char B[30] = "welcome to code jam";
	int Alen = strlen(A);
	int Blen = strlen(B);

	fr (i, Blen) fr (j, Alen) {
		D[i][j] = (j == 0 ? 0 : D[i][j-1]);
		if (i == 0 && B[i] == A[j]) D[i][j]++;
		else D[i][j] += (i > 0 && j > 0 && B[i] == A[j]) ? D[i-1][j-1] : 0;
		D[i][j] %= Mod;
	}

	printf("%04d\n", D[Blen-1][Alen-1]);
}

int main()
{
	int t, T;
	scanf("%d ", &T);

	fr(t, T)
	{
		input();
		printf("Case #%d: ", t+1);
		process();
	}
	return 0;
}
