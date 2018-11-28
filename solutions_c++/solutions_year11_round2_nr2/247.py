#include<stdio.h>
#include<algorithm>

using namespace std;

#define maxn ( 1<< 20 )

int Nr, D, Nr_total;
double V[ maxn ];

bool merge( const long long &val)
{
	double vaal = val / 2.0;
	
	double lim_st = -1000000;
	lim_st *= lim_st;
	lim_st = -lim_st;
	
	for( int i = 1; i <= Nr_total; ++i)
	{
		if( V[ i ] + vaal < lim_st + D) return false;
		lim_st = max (lim_st + D, V[ i ] - vaal );
	}
	return true;
}

void solve()
{
	Nr_total = 0;
	scanf("%d %d", &Nr, &D);
	for( int i = 1; i <= Nr; ++i)
	{
		int P, Nr_omuleti;
		scanf("%d %d", &P, &Nr_omuleti);
		while( Nr_omuleti > 0 )
		{
			V[ ++Nr_total ] = P;
			Nr_omuleti--;
		}
	}
	merge(5);
	long long dr = 2000000, st = 0;
	dr = dr * dr;
	while( st != dr )
	{
		long long mij = ( st + dr ) /2;
		if( merge( mij ) )
			dr = mij ;
		else st = mij + 1;
	}
	printf("%.1lf\n",(double)(st)/2);
	
}

int main()
{
	//freopen("ROTHD.in","r",stdin);
	//freopen("ROTHD.out","w",stdout);
	
	int TT;
	scanf("%d", &TT);
	for( int ii = 1; ii <= TT; ++ii)
	{
		printf("Case #%d: ", ii);
		solve();
	}


	return 0;
}
