#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

long long comb[41][41];
double prob[41][41];
double memo[41];
int C, N;

double doit(int alreadyFound)
{
    if(alreadyFound >= C) return 0;
    if(memo[alreadyFound] != -1) return memo[alreadyFound];
    double retVal = prob[alreadyFound][0];

    for(int i = 1; i <= N; i++)
	retVal += prob[alreadyFound][i] * (1 + doit(alreadyFound + i));

    return memo[alreadyFound] = retVal/(1 - prob[alreadyFound][0]);
}

int main()
{
    memset(comb, 0, sizeof comb);
    comb[0][0] = 1;
    for(int i = 1; i <= 40; i++)
    {
	comb[i][0] = 1;
	for(int j = 1; j <= 40; j++)
	    comb[i][j] = comb[i-1][j] + comb[i-1][j-1];
    }

    int T;
    cin >> T;
    for(int z = 0; z < T; z++)
    {
	cin >> C >> N;
	for(int i = 0; i <= 40; i++) 
	{
	    memo[i] = -1;
	    for(int j = 0; j <= 40; j++) 
		prob[i][j] = 0;
	}

	for(int i = 0; i <= C; i++)
	    for(int j = 0; j <= N; j++)
		prob[i][j] = (comb[i][N - j] * comb[C - i][j])/(double)(comb[C][N]);

	printf("Case #%d: %.7lf\n", z + 1, doit(0));
    }
    return 0;
}
