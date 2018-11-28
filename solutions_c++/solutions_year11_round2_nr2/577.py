#include <cstdlib>
#include <cstdio>
#include <algorithm>
using namespace std;

struct VENDOR
{
	double pos;
	int count;
};

bool comp( VENDOR a , VENDOR b )
{
	return a.pos < b.pos;
}

VENDOR v[300];


int main()
{
	FILE * fin = fopen( "in.txt" , "r" );
	FILE * fout = fopen( "out.txt" , "w" );
	
	int T;
	fscanf( fin , "%d" , &T );
	for( int t = 1 ; t <= T ; t++ )
	{
		int C;
		double D;
		fscanf( fin , "%d %lf" , &C , &D );
		for( int i = 0 ; i < C ; i++ ) fscanf( fin , "%lf %d" , &v[i].pos , &v[i].count );
		sort( v , v+C , comp );
		double maxtime = D*300 , mintime = 0;
		while( maxtime - mintime > 0.000001 )
		{
			double time = ( maxtime + mintime )/2;
			//printf( "%lf %lf\n" , mintime , maxtime );
			double initpos = v[0].pos - time;
			for( int i = 0 ; i < C ; i++ )
			{
				initpos = max( initpos , v[i].pos - time );
				if( initpos > v[i].pos + time ) goto FAIL;
				if( initpos + (v[i].count-1)*D > v[i].pos + time ) goto FAIL;
				initpos += (v[i].count)*D;
			}
			maxtime = time;continue;		
FAIL:;
			mintime = time;continue;
		}
		fprintf( fout , "Case #%d: %lf\n" , t , (maxtime+mintime)/2 );
	}
	fclose(fout);
	//system("PAUSE");
	return 0;
}
