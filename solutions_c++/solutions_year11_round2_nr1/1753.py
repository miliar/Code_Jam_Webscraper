/** Librerias **/
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <iomanip>

/** Namespaces **/
using namespace std;

/** Constantes **/

/** Macros **/
#define FOR(i,max) for ((i) = 0; (i) < (max); (i)++)
#define FORD(i,max) for ((i) = (max) - 1; (i) >= 0; (i)--)
#define FOR1(i,max) for ((i) = 1; (i) <= (max); (i)++)
#define FOR1D(i,max) for ((i) = (max); (i) >= 1; (i)--)

/** Tipos **/

/** Globales **/

/** Prototipos de funciones **/ 

/** Cuerpo principal **/
int main()
{
	int casos, ii, jj, kk;
	char matriz[101][101];
	double result[101], WP[101], OWP[101];
	cin >> casos;
	FOR1(ii,casos)
	{
		cout << "Case #" << ii << ":" <<  endl;
		int N, gan, jug;
		cin >> N;
		FOR(jj,N)
		{	
			jug = gan = 0;
			FOR(kk,N)
			{
				cin >> matriz[jj][kk];
				if (matriz[jj][kk] != '.'){
					jug++;
					if (matriz[jj][kk] == '1')
						gan++;
				}
			}
			WP[jj] = (gan / double(jug));
			result[jj] = WP[jj] * 0.25;
		}
		
		int rr, cont;
		double acum;
		FOR(jj,N){
			acum = 0.0;
			cont = 0;
			FOR(kk,N){
				if ((kk == jj) || (matriz[kk][jj] == '.'))
					continue;
				jug = gan = 0;
				cont++;
				FOR(rr, N){
					if (rr == jj)
						continue;
						
					if (matriz[kk][rr] != '.'){
						jug++;
						if (matriz[kk][rr] == '1')
							gan++;
					}
				}
				acum += (gan / double(jug));
			}
			OWP[jj] = acum / cont;
			result[jj] += 0.50 * OWP[jj];
		}
		
		FOR(jj,N){
			acum = 0.0;
			cont = 0;
			FOR(kk,N){
				if ((kk == jj) || (matriz[kk][jj] == '.'))
					continue;
				cont++;
				acum += OWP[kk];
			}
			result[jj] += 0.25 * (acum / cont);
		}
		
		cout << fixed;
		FOR(jj, N)
			cout << setprecision (6) << result[jj] << endl;
	}
	
	
	//Fin
	return 0;
}

/** Implementacion de funciones **/

