/*
 * =====================================================================================
 *
 * Nazwa pliku:  	A.cpp
 * Autor:		Szymon Stankiewicz (Daku)
 * Kontakt:		dakurels@gmail.com
 * Stworzony:		13.04.2013 22:11:38
 *
 * =====================================================================================
 */
#include<cstdio>
#include<algorithm>

using namespace std;

int test[4][4];
char mapa[4][4];

bool wygrana(char A)
{
	for(int i = 0; i<4; i++)
		for(int j = 0; j<4; j++)
			if(mapa[i][j]==A)
				test[i][j]=2;
			else if(mapa[i][j]=='T')
				test[i][j]=1;
			else
				test[i][j]=0;
	int maxi=0, licznik[2][4], ukos[2];
	for(int i = 0; i<2; i++)
	{
		ukos[i]=0;
		for(int j = 0; j<4; j++)
			licznik[i][j]=0;
	}
	for(int i = 0; i<4; i++)
	{
		for(int j = 0; j<4; j++)
		{
			if(i==j)
				ukos[0]+=test[i][j];
			if(i==3-j)
				ukos[1]+=test[i][j];
			licznik[0][i]+=test[i][j];
			licznik[1][j]+=test[i][j];
		}
	}
	for(int i = 0; i<2; i++)
	{
		maxi=max(maxi, ukos[i]);
		for(int j = 0; j<4; j++)
			maxi=max(maxi, licznik[i][j]);
	}
	return maxi>6;
}

void licz()
{
	bool puste=false;
	for(int i =0; i<4; i++)
	{
		scanf("%s", mapa[i]);
		for(int j=0; j<4; j++)
			if(mapa[i][j]=='.')
				puste=true;
	}
	if(wygrana('O'))
		printf("O won");
	else if(wygrana('X'))
		printf("X won");
	else if(puste)
		printf("Game has not completed");
	else
		printf("Draw");
}

int N;

int main()
{
	scanf("%d", &N);
	for(int i = 1; i<=N; i++)
	{
		printf("Case #%d: ", i);
		licz();
		printf("\n");
	}
}
