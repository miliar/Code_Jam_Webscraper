#include <iostream>
#define MAXN 100+10
using namespace std;

typedef long long lli;

int a, b;
int ta[ MAXN ], tb[ MAXN ];
lli wa[ MAXN ], wb[ MAXN ];
lli ans;

void solve( int _alast, int _blast, lli sum )
{
	lli alast = _alast;
	lli blast = _blast;
//cout << alast << " " << blast << " " << sum << endl;

	for(; alast<a  &&  wa[alast] == 0; alast++);
	if( alast == a )
		return;

//cout << "INCREASE" << endl;	
	solve( alast + 1, blast, sum );
	
	for(; blast<b  &&  ( tb[blast] != ta[alast]  ||  (tb[blast] == ta[alast]  &&  wb[blast] == 0) ); blast++);
	if( blast == b )
		return;
	
	if( ta[alast] == tb[blast] )
	{
		lli minval = min( wa[ alast ], wb[ blast ] );
		wa[alast] -= minval;
		wb[blast] -= minval;
		ans = max( ans, sum + minval );
//cout << "DODAJ " << sum << " " << minval << endl;
		solve( alast, blast, sum + minval );
		wa[alast] += minval;
		wb[blast] += minval;
	}
}


int main()
{
	int ilz;
	cin >> ilz;
	for (int xz = 1; xz <= ilz; xz++)
	{
		cin >> a >> b;
		for(int i=0; i<a; i++)
			cin >> wa[i] >> ta[i];
		for(int i=0; i<b; i++)
			cin >> wb[i] >> tb[i];
		ans = 0;
		solve( 0, 0, 0 );
		cout << "Case #" << xz << ": " << ans << endl;
	}
	return 0;
}

