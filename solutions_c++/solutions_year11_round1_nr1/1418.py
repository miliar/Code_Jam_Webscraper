#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int TC = 1, T, N, PD, PG, M=1000000;
double e = 10e-6;

int main ()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	for (cin>>T; TC <= T; TC++)
    {
		cin>>N>>PD>>PG;
		int D, flag = 1;
		double W, G;
		if ((PD < 100 && PG == 100) ||(PD > 0 && PG == 0))
			printf ("Case #%d: Broken\n", TC);
		else
		{	
			for (D = floor(100.0/PD); D <= N; D++)
			{
				W = D*PD/100.0;
				if (fabs(W-(int)W)<e)
				{
//					G = W*100.0/PG;
//					if (fabs(G-(int)G)<e)
//					{
						printf ("Case #%d: Possible\n", TC);
						flag = 0;
//					}
				}
				if (flag==0) break;
			}
			if (flag)
				printf ("Case #%d: Broken\n", TC);
		}
    }
	fclose(stdin);
	fclose(stdout);
    return 0;
}


