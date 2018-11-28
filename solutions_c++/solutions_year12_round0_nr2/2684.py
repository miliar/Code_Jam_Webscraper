#include <stdio.h>
#include <string.h>

#define LEN 100

typedef unsigned short _int;

_int s, p, n, goo[LEN], surp, best, max;

void go(_int a)
{
	unsigned char quo, modu, temp;

	if(a == n)
	{
		if(surp == s && best > max)   //match!
			max = best;
		return;
	}

	modu = goo[a] % 3;
	quo = goo[a] / 3;

	temp = best;

	if(modu < 2) //3x; (x-1,x,x+1) or x,x,x
	{               //OR 3x+1;
		if(quo > 0)
		{
			surp++; //x-1,x,x+1 for mod==0 OR x-1,x+1,x+1 for mod==1; has 1 surprise
			if(quo + 1 >= p)
				best++;
		}
		go(a + 1);

		if(quo > 0)
			surp--; //x,x,x for mod==0 OR x,x,x+1 for mod==1; no surprise

		best = temp;    //restore status
		if(modu == 0 && quo >= p || modu == 1 && quo + 1 >= p)
			best++;
		go(a + 1);
	}
	else    //3x+2; (x,x,x+2) or x,x+1,x+1
	{
		surp++; //x,x,x+2; surprise
		if(quo + 2 >= p)
			best++;
		go(a + 1);

		best = temp;    //restore status
		if(quo + 1 >= p)
			best++;
		surp--; //x,x+1,x+1; no surpries
		go(a + 1);
	}
	best = temp;
}

int main()
{
	_int t, x, a, b;
	FILE *in, *out, *inp, *hint;

	in = fopen("A-small.in", "r");
	out = fopen("out.txt", "w");

	if(in == 0 || out == 0)
		return -1;

	fscanf(in, "%hd%c", &t, &x);
	for(x = 0; x < t; x++)
	{
		fscanf(in, "%hd %hd %hd", &n, &s, &p);
		for(a = 0; a < n; a++)
			fscanf(in, "%hd", &goo[a]);

		surp = max = best = 0;
		go(0);

		fprintf(out, "Case #%d: %d\n", x + 1, max);
	}

	fclose(in);
	fclose(out);

	return 0;
}
