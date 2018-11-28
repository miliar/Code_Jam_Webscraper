#include <stdio.h>
#define MAXN 102


struct _paso
{
	char color;
	int destino;
};

_paso pasos[MAXN];
int n;


int buscaOrangeNext(int donde)
{
	for(int i=donde; i<n; i++)
		if( pasos[i].color == 'O' )
			return pasos[i].destino;
	return 0;
}           
int buscaBlueNext(int donde)
{
	for(int i=donde; i<n; i++)
		if( pasos[i].color == 'B' )
			return pasos[i].destino;
	return 0;
}

void caso(int nCaso)
{
	int orange = 1, blue = 1;
	int orangeDest, blueDest;
	bool orangeCan = false, blueCan = false;
	int actual = 0;
	scanf("%d", &n);
	for(int i=0; i<n; i++)
		scanf(" %c %d", &pasos[i].color, &pasos[i].destino);
	orangeDest = buscaOrangeNext(actual);
	blueDest = buscaBlueNext(actual);
	for(int i=0; i< MAXN*MAXN; i++)
	{
		if( actual == n )
		{
			printf("Case #%d: %d\n", nCaso, i);
			return;
		}
		if( pasos[actual].color == 'B' && blue == blueDest )
		{
			blueDest = buscaBlueNext(++actual);
			if( orange > orangeDest )
				orange--;
			else if( orange < orangeDest )
				orange ++;
			continue;
		}
		else if( pasos[actual].color == 'O' && orange == orangeDest )
		{
			orangeDest = buscaOrangeNext(++actual);
			
			if( blue > blueDest )
				blue --;
			else if(blue < blueDest)
				blue ++;
			continue;
		}
		if( orange > orangeDest )
			orange--;
		else if( orange < orangeDest )
			orange ++;
		if( blue > blueDest )
			blue --;
		else if(blue < blueDest)
			blue ++;
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	pasos[MAXN-1].color = 'O';
	pasos[MAXN-2].color = 'B';
	for(int i=0; i<T; i++)
		caso(i+1);
	return 0;
}
