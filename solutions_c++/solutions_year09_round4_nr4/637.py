#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <list>
#include <algorithm>
#include <stdio.h>
#include <string.h>

using namespace std;
#define FOR(VAR,START,STOP) for(int VAR=START;VAR<STOP;++VAR)
#define ZERO(V) memset( &V, 0, sizeof(V) )
#include <math.h>
#define SIZE 200
int X[SIZE],Y[SIZE],R[SIZE];
double sqr(double v) { return v*v; }
double dist(int i,int j)
{
	return sqrt( sqr( X[i]-X[j] ) + sqr( Y[i] - Y[j] ) );
}
int main()
{
	int G;
	cin >> G;
	FOR(g,0,G)
	{
		ZERO(X);
		ZERO(Y);
		ZERO(R);
		int N;
		cin >> N;
		// assert( N <= 3 );
		FOR(i,0,N)
		{
			cin >> X[i] >> Y[i] >> R[i];
		}
		double result = 0;
		switch( N )
		{
			case 1:
			result = R[0];
			break;
			case 2:
			result = std::max(R[0], R[1]);
			break;
			case 3:
			result = 9e99;
			FOR(j,0,3)
			{
				double r1=R[j];
				int j1 = (j+1)%3;
				int j2 = (j+2)%3;
				double d = dist( j1, j2) + R[j1] + R[j2];
				d *= 0.5;

				d = max( r1, d );

				if (d < result)
					result = d;
			}
			break;
		}
		cout << "Case #" << g+1 << ": " << result << endl;
	}

	return 0;
}

/* vim: set shiftwidth=4:tabstop=4:autoindent:noexpandtab: */
