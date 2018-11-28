#include <stdio.h>
#include <values.h> 

#define hmax 105
#define wmax 105
#define tmax 105

int t, h, w, num=0, bazin, dh []={0, -1, 0, 0, 1}, dw []={0, 0, -1, 1, 0}, m [hmax] [wmax];
char a [hmax] [wmax];

void scan ()
{
	int i, j;
	scanf ("%d%d", &h, &w);
	for (i=1; i <= h; ++i) 
		for (j=1; j <= w; ++j) 
			scanf ("%d", &m [i] [j]);
}

void fill (int h, int w)
{
	int i, min=m [h] [w], pmin=0;
	for (i=1; i <= 4; ++i)
	{
		if (a [h+dh [i]] [w+dw [i]] == 1) continue;
		if (m [h+dh [i]] [w+dw [i]] < min) 
		{
			min=m [h+dh [i]] [w+dw [i]];
			pmin=i;
		}
	}

//fprintf(stderr, "(%d, %d) %d %d %d\n", h+dh [pmin], w+dw [pmin], pmin , min, m [h] [w]); 

	if (pmin == 0) 
	{
		if (bazin == num)
		       ++num;
		a [h] [w]=bazin+'a';
		return;
	}


	if (a [h+dh [pmin]] [w+dw [pmin]] != 0)
	{
		bazin=a [h+dh [pmin]] [w+dw [pmin]]-'a';
		a [h] [w]=bazin+'a';
		return;
	}
	fill (h+dh [pmin], w+dw [pmin]);

	a [h] [w]=bazin+'a';
}

void rez ()
{
	int i, j;
	for (i=1; i <= h; ++i) 
		for (j=1; j <= w; ++j) 
			a [i] [j]=0;
	for (i=0; i <= h+1; ++i) 
		a [i] [w+1]=a [i] [0]=1;
	for (j=0; j <= w+1; ++j) 
		a [h+1] [j]=a [0] [j]=1;

	for (i=1; i <= h; ++i) 
		for (j=1; j <= w; ++j) 
			if (a [i] [j] == 0) 
			{
				bazin=num;
				fill (i, j);
			}
			
}

void print (int n)
{
	int i, j;
	printf ("Case #%d:\n", n);
	for (i=1; i <= h; ++i) 
	{
		for (j=1; j < w; ++j) 
			printf ("%c ", a [i] [j]);
		printf ("%c\n", a [i] [j]);
	}
}

int main ()
{
	freopen ("watersheds.in", "r", stdin);
	freopen ("watersheds.out", "w", stdout);
	int i;
	scanf ("%d", &t);
	for (i=1; i <= t; ++i) 
	{
		scan ();
		rez ();
		print (i);
		num=0;
		//fprintf(stderr, "num=%d\n", num); 
	}
}

