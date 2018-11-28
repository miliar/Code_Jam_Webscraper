#include <iostream>
using namespace std;
int main ()
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int tt;
	cin >> tt;
	for ( int t = 1; t <= tt ; t ++)
	{
		int n,k;
		cin >> n >> k;
		int on = (1<<n)-1;
		if ( k && on && k % (on+1) == on )
			printf("Case #%d: ON\n",t);
		else
			printf("Case #%d: OFF\n",t);
	}
	return 0;
}
