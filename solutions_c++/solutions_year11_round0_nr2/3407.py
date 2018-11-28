#include <iostream>
#include <fstream>
#include <utility>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

typedef vector<bool>  vbool;
typedef vector<vbool> vvbool;

typedef vector<int>  vint;
typedef vector<vint> vvint;

#define forn(i,n) for(int i=0; i<n; i++)
#define fornd(i,n) for(int i=n; i>0; i--)
#define fornx(i,x,n) for(int i=x; i<n; i++)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)

#define MAX 26

char intToChar(int i)
{
	return (char) (i + 'A');
}

int charToInt(char c)
{
	return (int)c - 'A';
}

int main(int argc, char** argv)
{       
    ifstream entrada("B-large.in");	
    ofstream salida("B-large.out");
    
    int cases;
    entrada >> cases;

	forn(caso, cases)
	{
		int C;
		entrada >> C;
		
		/* Con matríz de adyacencia. */
		vvint combinations (MAX, vint(MAX, -1));
		
		forn(i, C)
		{
			string comb;
			entrada >> comb;
			int i1, i2, i3;
			
			i1 = charToInt(comb[0]);
			i2 = charToInt(comb[1]);
			i3 = charToInt(comb[2]);
			
			combinations[i1][i2] = i3;
			combinations[i2][i1] = i3;
		}
		
		int D;
		entrada >> D;
		
		/* Con matríz de adyacencia. */
		vvbool opposed (MAX, vbool(MAX, false));
		
		forn(i, D)
		{
			string opp;
			entrada >> opp;
			int i1, i2;
			
			i1 = charToInt(opp[0]);
			i2 = charToInt(opp[1]);			
			
			opposed[i1][i2] = true;
			opposed[i2][i1] = true;
		}		
		
		int n;
		entrada >> n;
		
		vint elemsInt;		
		
		string elems;
		entrada >> elems;
		
		int cant = 0;
		
		forn(i, n)
		{
			elemsInt.push_back(charToInt(elems[i]));
			cant++;			
			
			/* Me fijo si se combina el último agregado con el anterior. */
			if (cant > 1)
			{
				int i1, i2;
				i1 = elemsInt[cant-1];
				i2 = elemsInt[cant-2];
				
				if (combinations[i1][i2] != -1)
				{
					/* Se combinan. Saco dos elementos y agrego uno.*/
					int nuevo = combinations[i1][i2];
					elemsInt.pop_back();										
					elemsInt.pop_back();
					elemsInt.push_back(nuevo);								
					
					/* Baja la cantidad. */
					cant--;
				}
				else
				{
					/* Busco si se opone a alguno. Necesito los subíndices desde 0 hasta cant-2 */
					forn(j, cant-1)
					{
						i2 = elemsInt[j];
						
						if (opposed[i1][i2])
						{
							/* Borrar todo. */
							elemsInt.clear();
							cant = 0;
							
							/* Fin. */
							break;
						}
					}					
				}
			}			
		}
		
		salida << "Case #" << caso+1 << ": [";
		
		forn(i, cant-1)
			salida << intToChar(elemsInt[i]) << ", ";
			
		if (cant > 0)
			salida << intToChar(elemsInt[cant-1]);
			
		salida << "]" << endl;
	}
	
	return 0;
}


