// Waters.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int w, h;
char vet[100][100];
int alt[100][100];

void CheckDown(int y, int x, int *yy, int *xx) {
	int min;
	
	*yy=y; *xx=x;
	if ((y<0)||(y>=h)||(x<0)||(x>=w)) return;

	min=alt[y][x];
	if ((y>0) && (alt[y-1][x]<min)) min=alt[*yy=(y-1)][*xx=x];
	if ((x>0) && (alt[y][x-1]<min)) min=alt[*yy=y][*xx=(x-1)];
	if ((x<(w-1)) && (alt[y][x+1]<min)) min=alt[*yy=y][*xx=(x+1)];
	if ((y<(h-1)) && (alt[y+1][x]<min)) min=alt[*yy=(y+1)][*xx=x];
}

void GoUp(int y, int x, char l) {
	int xx, yy;

	vet[y][x]=l;
	CheckDown(y-1,x,&yy,&xx);
	if ( ((xx==x)&&(yy==y)) && (vet[y-1][x]=='0') ) GoUp(y-1, x, l);
	CheckDown(y+1,x,&yy,&xx);
	if ( ((xx==x)&&(yy==y)) && (vet[y+1][x]=='0') ) GoUp(y+1, x, l);
	CheckDown(y,x-1,&yy,&xx);
	if ( ((xx==x)&&(yy==y)) && (vet[y][x-1]=='0') ) GoUp(y, x-1, l);
	CheckDown(y,x+1,&yy,&xx);
	if ( ((xx==x)&&(yy==y)) && (vet[y][x+1]=='0') ) GoUp(y, x+1, l);
}

void GoDown(int y, int x, char l) {
	int xx, yy;

	CheckDown(y,x,&yy,&xx);
	if ( ((xx!=x)||(yy!=y)) && (vet[yy][xx]=='0') )
	{
		GoUp(yy,xx,l);
		GoDown(yy,xx,l);
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	int t, i, x, y;
	char l;

	scanf("%d\n",&t);
	for (i=0;i<t;i++) {
		scanf("%d %d\n",&h, &w);
		for (y=0;y<h;y++)
			for (x=0;x<w;x++) {
				scanf("%d", &(alt[y][x]));
				vet[y][x]='0';
			}
		
		l='a';
		for (y=0;y<h;y++)
			for (x=0;x<w;x++)
				if(vet[y][x]=='0') {
					GoUp(y,x,l);
					GoDown(y,x,l++);
				}

		printf("Case #%d:\n",i+1);
		for (y=0;y<h;y++) {
			for (x=0;x<w;x++)
				printf("%c ",vet[y][x]);
			printf("\n");
		}		
	}
	return 0;
}   