#include <stdio.h>
#include <string.h> 


long long rez;
char s [75];
int n, N, x [75]; 


void init ()
{
	n=0;
	rez=0;
	for (int i=0; i <= 75; ++i) 
		x [i]=-1;
}

inline int poz (char c)
{
	if (c <= 'z' && c >= 'a') 
		return c-'a';
	else
		return 'z'-'a'+1+c-'0';	
}

void frecventa ()
{
	int i;
	x [poz (s [0])]=1;
	for (i=1; s [i]; ++i) 
	{
		if (x [poz (s [i])] == -1) 
		{
			x [poz (s [i])]=n;
		//	fprintf(stderr, "poz = %d\n n=%d\n", poz (s [i]), n); 
			++n;
			if (n == 1)
		       		++n;
		}	
	}
	N=i-1;
	if (n < 2)
	       n=2;	
	//fprintf(stderr, "%d\n", n); 
}

void calc ()
{
	int i;
	long long prod=1;
	for (i=N; i >= 0; --i)
	{
		rez += prod * x [poz (s [i])];
		//fprintf(stderr, "rez = %d\n", rez); 
		prod*=n;
	}	
}

int main ()
{
	freopen ("base.in", "r", stdin);
	freopen ("base.out", "w", stdout);
	int t, i;
	scanf ("%d\n", &t);
	for (i=1; i <= t; ++i)
	{	
		gets (s);
		init ();
		frecventa ();
		calc ();
		printf ("Case #%d: %lld\n", i, rez);
	}
}

