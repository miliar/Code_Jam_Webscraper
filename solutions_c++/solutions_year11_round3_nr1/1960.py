#include <iostream>
#include <algorithm>
#include <cmath>
#include <list>
#include <vector>
#include <map>
#include <string>

using namespace std;

int main()
{
	int casos, cont, R, C, i, j;
	bool hasTiles, possible;
	char picture[52][52];
	char newPicture[52][52];
	char letra;
	
	cin >> casos;
	cont = 1;
	
	while(cont <= casos)
	{
		hasTiles = false;
		possible = true;
		
		
		
		cin >> R;
		cin >> C;
		
		for(i=0; i<R; i++)
		{
			for(j=0; j<C; j++)
			{
				cin >> letra;
				
				if(!hasTiles && letra == '#') hasTiles = true;
				
				picture[i][j] = letra;
			}
			
		}
		
		cout << "Case #" << cont << ":" << endl;
		
		if(!hasTiles)
		{
			for(i=0; i<R; i++)
			{
				for(j=0; j<C; j++)
				{
					cout << picture[i][j];
				}
				cout << endl;
			}
		}
		else
		{
			bool leido;
			
			for(i=0; i<R; i++)
			{
				leido = false;
				
				for(j=0; j<C; j++)
				{
					if(!leido && picture[i][j] == '#') leido = true;
					else if(leido && picture[i][j] != '#')
					{
						possible = false;
					}
					else leido = false;
					
				}
				
				if(leido)
					possible = false;
			}
			
			for(i=0; i<C; i++)
			{
				leido = false;
				
				for(j=0; j<R; j++)
				{
					if(!leido && picture[j][i] == '#') leido = true;
					else if(leido && picture[j][i] != '#')
					{
						possible = false;
					}
					else leido = false;
					
				}
				
				if(leido)
					possible = false;
			}
			
		}
		
		if(!possible)
			cout << "Impossible" << endl;
		else if(hasTiles)
		{
			
			for(i=0; i<R; i++)
			{
				for(j=0; j<C; j++)
				{
					if(picture[i][j] == '#')
					{
						picture[i][j] = '/';
						picture[i][j+1] = '\\';
						picture[i+1][j] = '\\';
						picture[i+1][j+1] = '/';
					}
				}
			}
			
			for(i=0; i<R; i++)
			{
				for(j=0; j<C; j++)
				{
					cout << picture[i][j];
				}
				cout << endl;
			}
		}
		
		
		cont++;
	}
	
	return 0;
}
