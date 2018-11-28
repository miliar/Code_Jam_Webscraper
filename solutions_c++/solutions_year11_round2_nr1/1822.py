#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<list>
#include<queue>
#include<algorithm>

#define forn(i,n) 	 for(int i=0; i<n; i++)
#define fornd(i,n) 	 for(int i=n-1; i>=0; i--)
//~ #define fornd(i,n) 	 for(int i=n; i>0; i--)
#define fornx(i,x,n) for(int i=x; i<n; i++)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)

using namespace std;

int main(int argc, char** argv)
{
	ifstream entrada("A-large.in");
	ofstream salida("A-large.out");
	
	int casos;
	entrada >> casos;
	
	forn(caso, casos)
	{
		int n;
		entrada >> n;
		char matriz [n][n];
		
		forn(i, n)
		{
			forn(j, n)
			{
				char aux;
				entrada >> aux;
				matriz[i][j] = aux;
			}
		}
		
		salida.precision(12);
		salida << "Case #" << caso+1 << ": " << endl; 
		
		vector<int> ganados (n, 0);
		vector<int> jugados (n, 0);
		vector<double> wp (n, 0);
		vector<double> owp (n, 0);
		vector<double> oowp (n, 0);
		vector<double> rpi (n, 0);
		
		forn(i, n)
		{
			forn(j, n)
			{
				if (matriz[i][j] != '.')
					jugados[i]++;								
				if (matriz[i][j] == '1')
					ganados[i]++;
			}
					
			wp[i] = (double) ganados[i]/ (double) jugados[i];
			//~ cout << wp[i] << endl;
		}
		
		for(int i=0; i<n; i++)
		{				
			double aux;
			int cant = 0;
			
			for(int j = 0; j<n; j++)
			{
				if (j != i && matriz[i][j] != '.')
				//~ if (j != i && (matriz[i][j] == 1 || matriz[i][j] == 0))
				{					
					int resta = (matriz[j][i] == '1')? 1: 0;
					//~ cout << "i: " << i << " " << "j: " << j << " " << ganados[j] << " " << resta << endl;
					aux = (double) (ganados[j] - resta)/ (double) (jugados[j] - 1);
					//~ cout << aux << endl;
					owp[i] += aux;
					cant++;
				}				
			}
			owp[i] = owp[i] / (double) cant;
			//~ cout << owp[i] << endl;
		}
		
		forn(i, n)
		{				
			double aux;
			int cant = 0;
			forn(j, n)
			{
				//~ if (j != i && (matriz[i][j] == 1 || matriz[i][j] ==0))
				if (j != i && matriz[i][j] != '.')
				{
					oowp[i] += owp[j];
					cant++;
				}				
			}
			oowp[i] = oowp[i] / (double) cant;
		}
		
		forn(i, n)
		{				
			rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			salida << rpi[i] << endl;
		}		
		
	}
	
	return 0;	
}
