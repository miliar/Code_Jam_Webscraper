#include <iostream>
#include <stdio.h>
#include <fstream>
#include <math.h>
using namespace std;

int main()
{
	int T;

	int i, j,k,t;
	int N;
	int played[101];
	double prv;
	char Shed[101][101];
	double WP[101], OWP[101], OOWP[101];

	cin >> T;
	for (i=1;i<=T; i++)
	{
		cin >> N;
		for (j=0;j<N;j++)
		{
			WP[j] = 0.;
			OWP[j]= 0.;
			OOWP[j] = 0.;
			for (k=0;k<N;k++)
			{
				cin >> Shed[j][k];
			}
		}


		for (j=0;j<N;j++)
		{
			played[j] = 0;
			for (k=0;k<N;k++)
			{
				if (Shed[j][k] == '0') played[j] ++;
				if (Shed[j][k] == '1')
				{
					played[j] ++;
					WP[j] = WP[j] + 1;
				}
			}
			WP[j] = WP[j] / played[j];
		}

		for (j=0;j<N;j++)
		{

			for (k=0;k<N;k++)
			{
				if (Shed[j][k] != '.')
				{
					prv = 0;
					for (t=0;t<N;t++)
					{
						if (t!=j)
						{
							if (Shed[k][t] == '1') prv = prv + 1;
						}
					}
					OWP[j] = OWP[j] + prv/(played[k]-1);
				}
			}
			OWP[j] = OWP[j]/played[j];
		}

		for (j=0;j<N;j++)
		{

			for (k=0;k<N;k++)
			{
				if (Shed[j][k]!='.')
				{
					OOWP[j] = OOWP[j] + OWP[k];
				}
			}

			OOWP[j]=OOWP[j]/played[j];
		}

		cout << "Case #" <<i << ":" << endl;
		for (j=0;j<N;j++)
		{
			cout.fixed;
			cout.precision(12);
			cout << (0.25*WP[j] + 0.5*OWP[j] + 0.25*OOWP[j]) << endl;
		}

	}
	return 0;
}