#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;
#define maxd 1000000000

struct cor{ int st,end,speed;
	bool operator <( const cor &a) const{
		if( st < a.st) return 1;
		return 0;
	}
};
bool comparator( const cor &a, const cor&b) 
{
	if( a.speed > b.speed)
		return 0;
	return 1;
}

cor coridor[ 1024 ];
int timpi[ 2048 ];
int X, S, R, t2, Nr;

void citire()
{
	scanf("%d %d %d %d %d", &X, &S, &R, &t2, &Nr);
	for( int i = 0; i < Nr; ++i)
		scanf("%d %d  %d", &coridor[ i ].st, &coridor[ i ].end, &coridor[ i ].speed);
	
	 
}
double sol[ 1000002 ][ 2 ];


void solve()
{
	sort( coridor, coridor + Nr);
	timpi[ 0 ] = 0;
	for( int i = 0; i < Nr; ++i)
		timpi[ i * 2 + 1] = coridor[ i ].st, timpi[ i * 2 + 2 ] = coridor[ i ].end;
	timpi[ Nr * 2 + 1 ] = X;
	int N = Nr * 2 + 1;
	double timp = 0;
	double t1 = t2;
	for( int i = 1; i <= N; i +=2)
	{
		double dist = timpi[ i ] - timpi[ i - 1];
		if( dist <= t1 * R )
		{
			timp += dist / R;
			t1 -= dist / R;
		}
		else
		{
			timp += t1 + (dist - t1 * R) / S;
			t1 = 0;
		}
	}
	for( int i = 0; i < N; ++i)
	{
		int aux = coridor[ i ].st;
		coridor[ i ].st = coridor[ i ].speed;
		coridor[ i ].speed = aux;
	}
	sort( coridor, coridor +Nr);
	for( int i = 0; i < N; ++i)
	{
		int aux = coridor[ i ].st;
		coridor[ i ].st = coridor[ i ].speed;
		coridor[ i ].speed = aux;
	}
	
	for( int i = 0; i < Nr; ++i)
	{
		double dist = coridor[ i ].end - coridor[ i ].st;
		/*if( coridor[ i ].speed + S >= R || t1 == 0)
		{
			timp += dist / (coridor[ i ].speed + S);
			continue;
		}*/
		double runspeed = R + coridor[ i ]. speed;
		if( dist <= t1 * runspeed)
		{
			timp += dist / runspeed;
			t1-= dist / runspeed;
		}
		else
		{
			timp += t1 + (dist - t1 * runspeed) / (S + coridor[ i ].speed);
			t1 = 0;
		}
		
	}
	
	/*for( int j = 0; j <= t; ++j)
		for( int l = 0; l <= 1; ++l)
			sol[ j ][ i ] = maxd;
	sol[ t ][ 0 ] = 0;
	for( int i = 0; i < N; ++i)
	{
		int r = i % 2;
		for( int j = t; j >= 0; ++j)
			if( sol[ j ][ r ] < maxd)
			{
				double mers = sol[ j ][ r ] + (timpi[ i + 1 ] - timpi[ i ] ) / (double)S;
				if( sol[ j ][ !r ] > mers) sol[ j ][ !r ] = mers;
				double alergat = 
			}
	}*/
	printf("%.10lf\n",timp);
}


int main()
{
	freopen("airport.in","r",stdin);
	freopen("airport.out","w",stdout);
	
	int TT;
	scanf("%d", &TT);
	for( int ii = 1; ii <= TT; ++ii)
	{
		printf("Case #%d: ", ii);
		citire();
		solve();
	}
	
	
	
	
	
	return 0;
}
