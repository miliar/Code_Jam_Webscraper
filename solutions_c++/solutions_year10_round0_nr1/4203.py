#include <iostream.h>
#include <conio.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
int main()
{
	FILE *in,*out;
	int ncases,c;
	in=fopen("AL.txt","r+");
	out=fopen("AO.out","w+");
	fscanf(in,"%d",&ncases);
	for(c=0;c<ncases;c++)
	{

	}
	fclose(in);
	fclose(out);
	clrscr();
	return 0;
}