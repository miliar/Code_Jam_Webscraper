#include <iostream>
#include <fstream>
#include <utility>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0; i<n; i++)
#define fornd(i,n) for(int i=n; i>0; i--)
#define fornx(i,x,n) for(int i=x; i<n; i++)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)

int main(int argc, char** argv)
{
    ifstream entrada("A-large.in");	
    ofstream salida("A-large.out");
    
    int cases;
    entrada >> cases;

	forn(caso, cases)
	{
		int n;
		entrada >> n;
		
		queue<pair<int, int> > b;
		queue<pair<int, int> > o;
		
		forn(i, n)
		{
			char bot;
			int aux;
			entrada >> bot >> aux;
			
			if (bot == 'O')
				o.push(make_pair(aux, i));
			else
				b.push(make_pair(aux, i));
		}
		
		long long int res = 0;
		int pos_b = 1;
		int pos_o = 1;		
		bool boton_o = false;
		pair<int, int> aux_o, aux_b;
				
		while(!o.empty() && !b.empty())
		{
			aux_o = o.front();
			aux_b = b.front();
						
			/* o */	
			
			/* ¿Estoy dónde tengo que estar? */
			if (pos_o == aux_o.first)
			{					
				/* ¿Puedo apretar el botón? */
				if (aux_o.second < aux_b.second)
				{				
					/* Tardo un movimiento en apretar el botón. */
					res++;
					/* Estoy apretando el botón. */
					boton_o = true;
					/* Saco ese movimiento porque ya lo hice. */
					o.pop();
				}
				else
				{
					/* Tardo un movimiento igual porque tengo que esperar*/
					res++;
					boton_o = false;
				}
			}
			else
			{
				if (pos_o < aux_o.first)
				{
					/* Tardo un movimiento en avanzar. */
					res++;						
					/* Avanzo. */
					pos_o++;						
					/* No estoy apretando el botón. */
					boton_o = false;	
				}
				else /* pos_o > aux_o.first */
				{
					/* Tardo un movimiento en retroceder. */
					res++;						
					/* Retrocedo. */
					pos_o--;						
					/* No estoy apretando el botón. */
					boton_o = false;	
				}
			}
			
			
			/* b */
			
			/* ¿Estoy dónde tengo que estar? */
			if (pos_b == aux_b.first)
			{
				/* ¿Puedo apretar el botón? */
				if (aux_b.second < aux_o.second && !boton_o)
				{
					/* Saco ese movimiento porque ya lo hice. */
					b.pop();
				}				
			}
			else
			{
				if (pos_b < aux_b.first)
				{
					/* Avanzo. */
					pos_b++;				
				}
				else /* pos_b > aux_b.first */
				{
					/* Retrocedo. */
					pos_b--;					
				}
			}
		}
				
		while(!o.empty())
		{			
			aux_o = o.front();
			
			/* ¿Estoy dónde tengo que estar? */
			if (pos_o == aux_o.first)
			{
				res++;
				o.pop();				
			}
			else
			{
				if (pos_o < aux_o.first)
				{
					/* Tardo un movimiento en avanzar. */
					res++;					
					/* Avanzo. */
					pos_o++;
				}
				else /* pos_o > aux_o.first */
				{
					/* Tardo un movimiento en retroceder. */
					res++;						
					/* Retrocedo. */
					pos_o--;
				}
			}			
		}
		
		while(!b.empty())
		{			
			aux_b = b.front();
			
			/* ¿Estoy dónde tengo que estar? */
			if (pos_b == aux_b.first)
			{
				res++;
				b.pop();
			}
			else
			{
				if (pos_b < aux_b.first)
				{
					/* Tardo un movimiento en avanzar. */
					res++;					
					/* Avanzo. */
					pos_b++;
				}
				else /* pos_b > aux_b.first */
				{
					/* Tardo un movimiento en retroceder. */
					res++;						
					/* Retrocedo. */
					pos_b--;
				}
			}			
		}
		
		salida << "Case #" << caso+1 << ": " << res << endl;
	}
	
	return 0;
}


