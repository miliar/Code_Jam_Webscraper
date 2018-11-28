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
	//~ ifstream entrada("A-small.in");
	//~ ofstream salida("A-small.out");
	ifstream entrada("A-large.in");
	ofstream salida("A-large.out");
	
	int casos;
	entrada >> casos;
	
	forn(caso, casos)
	{
		int n, m;
		entrada >> n >> m;
		
		char matriz [n][m];
		
		forn(i, n)
		{
			forn(j, m)
			{
				char aux;
				entrada >> aux;
				matriz[i][j] = aux;
			}
		}
		
		char res [n][m];
		bool posible = true;
		
		//~ int cant = 0;
		
		forn(i, n)
		{
			forn(j, m)
			{
				res [i][j] = (matriz[i][j] == '#')? '0' : '.';				
			}
		}
		
		//~ forn(i, n)
		//~ {
			//~ forn(j, m)
				//~ cout << res[i][j] << " ";
			//~ cout << endl;
		//~ }
		
		forn(i, n)
		{
			if (!posible)
				break;
			
			forn(j, m)
			{
				if (res[i][j] == '0' && matriz[i][j] == '#')
				{					
					//~ cout << "valor: " << matriz[i][j] << " i: " << i << " j: " << j << endl;
					
					if( (j<m-1) && matriz[i][j+1] == '#' && (i<n-1) && matriz[i+1][j] == '#' && matriz[i+1][j+1] == '#')
					{
						if (res[i][j] == '0')
						{
							res [i][j] = '/';
							res [i][j+1] = 92;
							res [i+1][j] = 92;
							res [i+1][j+1] = '/';
						}
						else
						{
							posible = false;
							break;
						}
					}
					else
					{
						posible = false;
						break;
					}
				}				
			}
		}
		
		//~ forn(i, n)
		//~ {
			//~ forn(j, m)
				//~ cout << res[i][j] << " ";
			//~ cout << endl;
		//~ }
		
		salida << "Case #" << caso+1 << ": " << endl;
		if (!posible)
			salida << "Impossible" << endl;
		else
		{
			forn(i, n)
			{
				forn(j, m)
					salida << res[i][j];
				salida << endl;
			}
		}
	}
	
	return 0;	
}
