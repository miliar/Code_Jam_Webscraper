// 2011_2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

FILE * in, * out;

#define fo(a,b,c) for(int a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

int ri() { int a; fscanf(in, "%d", &a ); return a; }
double rf() { double a; fscanf(in, "%lf", &a ); return a; }
char sbuf[100005]; string rs() { fscanf(in, "%s", sbuf ); return sbuf; }
long long rll() { long long a; fscanf(in, "%lld", &a ); return a; }

bool isCenter(double * m, int w, int h, int i, int j, int b)
{
	double cx =0, cy = 0;
	for(int x = -b; x<=b; x++)
	for(int y = -b; y<=b; y++)
	{
		if((x == b || x == -b) && (y == b || y == -b)) continue;
		cx += x*m[(i+x)+(j+y)*w];
		cy += y*m[(i+x)+(j+y)*w];
	}
	return ((cx == 0)&&(cy==0));
}


int getBestPart(double * m, int w, int h, int i, int j, int cb)
{
	int b = cb/2;
	while(1)
	{
		if(b > i) break;
		if(b > j) break;
		if(b+i >= w) break;
		if(b+j >= h) break;

		if(isCenter(m,w,h,i,j,b)) 
		{
			isCenter(m,w,h,i,j,b);
			cb = b*2+1;
		}
		b++;
	}

	return cb;
}


bool isCenter2(double * m, int w, int h, int i, int j, int b)
{
	double cx =0, cy = 0;
	for(int x = -b; x<b; x++)
	for(int y = -b; y<b; y++)
	{
		if((x == b-1 || x == -b) && (y == b-1 || y == -b)) continue;
		cx += (x+0.5)*m[(i+x)+(j+y)*w];
		cy += (y+0.5)*m[(i+x)+(j+y)*w];
	}
	return ((cx == 0)&&(cy==0));
}

int getBestPart2(double * m, int w, int h, int i, int j, int cb)
{
	int b = cb/2;
	while(1)
	{
		if(b > i) break;
		if(b > j) break;
		if(b+i > w) break;
		if(b+j > h) break;

		if(isCenter2(m,w,h,i,j,b)) 
		{
			cb = b*2;
		}
		b++;
	}

	return cb;
}

int _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("B-small-attempt4.in","rt");
	out	= fopen("s_out.txt","wt");
	
	int T = ri(); 
	for(int i = 0; i<T; i++)
	{
		int X = ri();
		int Y = ri();
		double D = ri();

		vector<double> m(X*Y);
		fj(X)
		{
			string st = rs();
			fk(Y)
				m[j*Y+k] = st[k]-'0'+D;
		}

		int best = 2;
		int cb;
		fj(X)
			fk(Y)
		{
			cb = getBestPart(&m[0],Y,X,k,j,best);
			if(cb > best) 
				best = cb;
			cb = getBestPart2(&m[0],Y,X,k,j,best);
			if(cb > best) 
				best = cb;
		}

		if(best >= 3)
			fprintf(out,"Case #%d: %d\n",i+1, best);
		else
			fprintf(out,"Case #%d: IMPOSSIBLE\n",i+1);
	}

	fclose(in);
	fclose(out);
	return 0;
}

