#include <iostream>
#include <stdlib.h>

using namespace std;

int main ()
{
    int t, n, i, buton, x=0,y=0, p,r, oPos, bPos, hamle, j;
    int *o, *b, *sonuc;
    char c, *sira, yerO, yerB;
    
    cin >> t;
    sonuc = new int[t];
    for (j=0; j<t; j++)
    {
	cin >> n;
	
	x = y = 0;
	oPos = bPos = 1;
	
	o = new int[n];
	b = new int[n];
	sira = new char[n];
    
	for (i=0; i<n; i++)
	{
	    cin >> c;
	    cin >> buton;
	    if (c == 'O') {
		o[x] = buton;
		x++;
	    }
	    else if (c=='B') {
		b[y] = buton;
		y++;
	    }
	    sira[i] = c;
	}

	for (hamle = 0, i=0, p=0, r=0; p<x || r<y ;hamle++)
	{
	    c = sira[i];
	    if (c == 'O')
	    {
		yerO = o[p];
		if (r<y)
		    yerB = b[r];
		if (yerO < oPos)
		    oPos--;
		else if (yerO >oPos)
		    oPos++;
		else {
		    p++;
		    i++;
		}
		if (r<y && yerB < bPos)
		    bPos--;
		else if (r<y && yerB > bPos)
		    bPos++;
	    }
	    else if (c == 'B')
	    {
		if (p<x)
		    yerO = o[p];
		yerB = b[r];
		if (p<x && yerO < oPos)
		    oPos--;
		else if (p<x && yerO >oPos)
		    oPos++;

		if (yerB < bPos)
		    bPos--;
		else if (yerB > bPos)
		    bPos++;
		else {
		    r++;
		    i++;
		}
	    }
	}
	sonuc[j] = hamle;
    }
    for (j=0; j<t; j++)
	cout << "Case #" << j+1 << ": " << sonuc[j] << endl;
    
    
    delete [] o;
    delete [] b;
    delete [] sonuc;
    delete [] sira;

 return 0;   
}