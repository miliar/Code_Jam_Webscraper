#include <iostream>
#include <cstdio>
using namespace std;

class snapper {
	public:
	bool power;
	bool on;
} a [12];

void reset (int n)
{
	for ( int i = 0; i < n; i++ ) {
		i[a].power = false;
		i[a].on = false;
	}
	0[a].power = true;
}

int main ()
{
	int t;
	scanf ("%d", &t);
	int cases = 0;

	while ( t-- ) {
		int n;
		int k;
		scanf ("%d %d", &n, &k);

		reset (n);

		for ( int i = 0; i < k; i++ ) {
			for ( int j = 0; j < n; j++ ) {
				if ( a [j].power )
					a [j].on = !(j[a].on);
			}
			for ( int j = 0; j < n; j++ ) {
				if ( a [j].power && a [j].on )
					a [j + 1].power = true;
				else
					a [j + 1].power = false;
			}
		}

		if ( a [n - 1].power && a [n - 1].on )
			printf ("Case #%d: ON\n", ++cases);
		else
			printf ("Case #%d: OFF\n", ++cases);
	}

	return 0;
}
