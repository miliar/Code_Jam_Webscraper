#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int i, j, t, k, n, s, p, count, desired, required;
	
	cin >> t;	
	for ( i = 0; i < t; i++ ) {
		cin >> n >> s >> p;
		count = 0;
		desired = 3 * p - 2;
		required = 3 * p - 4;
		for ( j = 0; j < n; j++ ) {
			cin >> k;
			if ( !p ) {
				count++;
			} else {
				if ( k >= desired )
					count++;
				else if( required >= 0 && k >= required && s ) {
					count++;
					s--;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
	
	return 0;
}	
