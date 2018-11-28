#include <cstdio>
#include <cstdlib>
#include <string>
#include <queue>


char frase[5064];
int cont;
int tam;
	
typedef struct meu
{
	meu(int state , int i)
	{
		this->state = state;
		this->i = i;
	}

	int state;
	int i;
}BUNDA;	
	
using namespace std;	
	
int main (void)
{
	int num;

	int teste = 1;
	queue<BUNDA> fila;
	
	scanf("%d" , &num);
	while(getchar()!='\n');
	
	while(num > 0)
	{
		gets(frase);
		
		tam = strlen(frase);
		
		cont = 0;

		for (int i = 0; i < tam; ++i)
		{
			if (frase[i] == 'w')
			{
				fila.push(BUNDA(1 , i + 1));
			}
		}
		
		while(fila.empty() == false)
		{
			BUNDA b = fila.front();
			
			fila.pop();
			
			while(b.i < tam)
			{
				switch(b.state)
				{
					case 1: 
					case 6:
					case 14:
					{
						if (frase[b.i] == 'e')
						{
							fila.push(BUNDA(b.state + 1, b.i + 1));
						}
						break;
					}
					case 2:
					{
						if (frase[b.i] == 'l')
						{
							fila.push(BUNDA(b.state + 1, b.i + 1));
						}
						break;
					}
					case 3:
					{
						if (frase[b.i] == 'c')
						{
							fila.push(BUNDA(b.state + 1, b.i + 1));
						}
						break;
					}
					case 4:
					case 9:
					case 12:
					{
						if (frase[b.i] == 'o')
						{
							fila.push(BUNDA(b.state + 1, b.i + 1));
						}
						break;
					}
					case 5:
					{
						if (frase[b.i] == 'm')
						{
							fila.push(BUNDA(b.state + 1, b.i + 1));
						}
						break;
					}
					case 7:
					case 10:
					case 15:
					{
						if (frase[b.i] == ' ')
						{
							fila.push(BUNDA(b.state + 1, b.i + 1));
						}
						break;
					}
					case 8:
					{
						if (frase[b.i] == 't')
						{
							fila.push(BUNDA(b.state + 1, b.i + 1));
						}
						break;
					}
					case 11:
					{
						if (frase[b.i] == 'c')
						{
							fila.push(BUNDA(b.state + 1, b.i + 1));
						}
						break;
					}
					case 13:
					{
						if (frase[b.i] == 'd')
						{
							fila.push(BUNDA(b.state + 1, b.i + 1));
						}
						break;
					}
					case 16:
					{
						if (frase[b.i] == 'j')
						{
							fila.push(BUNDA(b.state + 1, b.i + 1));
						}
						break;
					}
					case 17:
					{
						if (frase[b.i] == 'a')
						{
							fila.push(BUNDA(b.state + 1, b.i + 1));
						}
						break;
					}
					case 18:
					{
						if (frase[b.i] == 'm')
						{
							cont++;
						}
						break;
					}
				}	
				b.i++;
			}
		}
		printf("Case #%d: %04d\n" , teste++, cont);
		
		num--;
	}
	
	return 0;
}
