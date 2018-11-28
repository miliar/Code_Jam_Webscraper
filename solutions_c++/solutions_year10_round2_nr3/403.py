#include <iostream>
#include <gmpxx.h>
#define MAX_N 501
using namespace std;

mpz_class comb[MAX_N][MAX_N];
mpz_class res[MAX_N][MAX_N];

int main(void)
{
	for(int i = 0; i <= 500; i++)
	{
		comb[i][0] = 1;
		comb[i][i] = 1;
	}
	for(int i = 2; i <= 500; i++)
		for(int j = 1; j <= i; j++)
			comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
	
	
	for(int i = 1; i <= 500; i++)
	{
		res[i][1] = 1;
		res[i][i - 1] = 1;
	}
	for(int i = 4; i <= 500; i++)
	{
		for(int j = 2; j < i - 1; j++)
		{
			for(int k = 1; k < j; k++)
			{
				res[i][j] += res[j][k] * comb[i - j - 1][j - k - 1];
			}
		}
	}
	
	int T, n, numCase = 1;
	for(cin >> T; numCase <= T; numCase++)
	{
		cin >> n;
		
		mpz_class total = 0;
		for(int i = 1; i < n; i++) total += res[n][i];
		
		cout << "Case #" << numCase << ": " << total % 100003 << endl;
	}
		
}
			
