#include <cstdio>
#include <iostream>
#include <cstdlib>
using namespace std;

int orange;
int blue;

int t_b;
int t_o;

typedef struct _mov
{
	int pos;
	char color;
} _mov;

_mov lista[105];

int Next(char color,int pl)
{
	while(lista[pl].color != color && pl < 105)
		pl++;
	if ( pl == 105 )
	{
		if ( color == 'O' )
		{	
			t_o = 1;
			//cout << "Termino el naranja" << endl;
			return orange;
		}
		else
		{
			t_b = 1;
			//cout << "Termino el azul" << endl;
			return blue;
		}
	}
	return lista[pl].pos;	
}

int main()
{
	
	
	int t;
	int i,j,k;
	cin >> t;	
	for ( i = 1 ; i <= t ; i++ )
	{
		int cont = 0;
		int n;
		cin >> n;
		int fb = 1;
		int fo = 1;
		for ( j = 0 ; j < n ; j++ )
		{
			cin >> lista[j].color;
			cin >> lista[j].pos;
			//printf("Elemento leido %c %d",lista[j].color,lista[j].pos);
		}

		int next_blue;
		int next_orange;

		orange = 1;
		blue = 1;
		
		int pl = 0;
		
		next_blue = Next('B',pl);
		next_orange = Next('O',pl);
		
		t_b = 0;
		t_o = 0;
		
		while( pl < n)
		{		
			cont++;
			int f = 0;
			
			//cout << "Orange tiene que ir a " << next_orange << endl;
			//cout << "Blue tiene que ir a " << next_blue << endl;
			
			if ( !t_o && lista[pl].color == 'O' && lista[pl].pos == orange )
			{
				f = 1;
				//cout << "Orange presiono boton" << endl;
			}
			else
			{
				if ( orange < next_orange ) 
					orange++;
				else if ( orange > next_orange )
					orange--;
				//cout << "Orange se movio a " << orange << endl;
			}
			
			if ( !t_b && lista[pl].color == 'B' && lista[pl].pos == blue )
			{	
				f = 1;
				//cout << "Blue presiono boton" << endl;
			}
			else
			{
				if ( blue < next_blue)
					blue++;
				else if ( blue > next_blue )
					blue--;
				//cout << "Blue se movio a " << blue << endl;
			}
			
			if ( f )
			{
				pl++;
				if ( pl < n )
				{
					next_orange = Next('O',pl);
					next_blue = Next('B',pl);
				}
			}			
		}
		
		printf("Case #%d: %d\n",i,cont);
	}
	
	return 0;
}
