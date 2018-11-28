#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int dix[7] = {1,10,100,1000,10000,100000,1000000};

int main()
{
    int nbcas;
    scanf("%d", &nbcas);
    for(int cas = 1; cas <= nbcas; cas++)
    {
	int a, b;
	scanf("%d%d", &a, &b);
	int digits = ((int) log10(a)) + 1;
	int result = 0;
	for(int n = a; n < b; n++)
	{
	    int paires[digits-1];
	    int nbpaires = 0;
	    for(int shift = 1; shift < digits; shift++)
	    {
		int m = (n % dix[shift])*dix[digits-shift] + (n / dix[shift]);
		bool ok = true;
		if(m <= n || m > b) continue; //deals with leading zeroes problem
		for(int i = 0; i < nbpaires; i++)
		    if(m == paires[i]) ok = false;
		if(ok)
		{
		    paires[nbpaires] = m;
		    nbpaires++;
		}
	    }
	    result += nbpaires;
	}
	printf("Case #%d: %d\n", cas, result);
	}
    return 0;
}
