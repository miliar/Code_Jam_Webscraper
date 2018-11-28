#include <stdio.h> 

#define nmax 105
#define kmax 505
#define r 10000

char x [kmax], y [55]={"0welcome to code jam"};
int k, a [kmax] [55];


int res ()
{

	for (k=1; x [k]; ++k);

	int i, j;


	for (i=0; i <= k; ++i) 
		for (j=0; j <= 20; ++j) 
			a [i] [j]=0;

	for (i=1; i <= k; ++i) 
	{
		a [i] [1]=a [i-1] [1];
		if (x [i] == y [1]) 
			++a [i] [1];
	}

	for (i=2; i <= k; ++i) 
		for (j=2; j <= 19; ++j) 
		{
			if (x [i] == y [j]) 
				a [i] [j]=a [i-1] [j]+a [i-1] [j-1];
			else
				a [i] [j]=a [i-1] [j];	
			a [i] [j] %= r;
		}

/*	for (i=1; i <= k; ++i) 
	{
		for (j=1; j <= 19; ++j) 
			printf ("%d ", a [i] [j]);
		printf ("\n");
	}*/

	return a [k] [19];
}
	

int main ()
{
	freopen ("welcome.in", "r", stdin);
	freopen ("welcome.out", "w", stdout);
	int n, i, o;
	scanf ("%d\n", &n);
	for (i=1; i <= n; ++i) 
	{
		gets (x+1);
		o=res ();
	//	o=2345;
		printf ("Case #%d: ", i);
		if (o < 10)
		       printf ("000%d", o);	
		else
		{
			if (o < 100) 
				printf ("00%d", o);
			else
			{
				if (o < 1000) 
					printf ("0%d", o);
				else
					printf ("%d", o);
			}
		}
		printf ("\n");
	}
	return 0;
}

