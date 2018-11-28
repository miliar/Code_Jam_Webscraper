#define CAPP2

#ifdef CAPP2

#include<stdio.h>
#include<string.h>
#include<memory.h>
#include <stdlib.h>
#include <math.h>

#define maxbfr 100

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	if ( !fp )
		return 0;
	int N = 0;
	fscanf(fp, "%d\n", &N);
	for( int i = 1 ; i <= N ; i++ )
	{
		int A = 0;
		fscanf(fp, "%d\n" , &A);
		int sx=0,sy=0,sz=0,sdx=0,sdy=0,sdz=0;
		for( int j = 0 ; j < A ; j++ )
		{
			int x,y,z,dx,dy,dz;
			fscanf(fp,"%d",&x);
			fscanf(fp,"%d",&y);
			fscanf(fp,"%d",&z);
			fscanf(fp,"%d",&dx);
			fscanf(fp,"%d",&dy);
			fscanf(fp,"%d\n",&dz);
			sx+=x;
			sy+=y;
			sz+=z;
			sdx+=dx;
			sdy+=dy;
			sdz+=dz;
		}
		double a = (double)sdx*(double)sdx+(double)sdy*(double)sdy+(double)sdz*(double)sdz;
		double time = 0.0;
		if( a == 0.0 )
			time = 0.0;
		else
			time = (-1.0)*( (double)sx*(double)sdx + (double)sy*(double)sdy + (double)sz*(double)sdz ) / a;
		if( time < 0 )
			time = 0.0;
		double dist = 0.0;
		double b = ( (double)sx + time * (double)sdx ) / (double)A;
		double c = ( (double)sy + time * (double)sdy ) / (double)A;
		double d = ( (double)sz + time * (double)sdz ) / (double)A;
		dist = sqrt( b*b+c*c+d*d );
		fprintf(ofp, "Case #%d: %.8f %.8f\n" , i , dist , time );
	}
	fclose(ofp);
	fclose(fp);
	return 0;
}
#endif