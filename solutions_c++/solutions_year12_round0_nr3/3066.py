#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	int t, n, m, d, i, j, k, l, x, y, z, lx;
	
	cin >> t;
	for (l=0; l<t; l++) {
		cin >> n >> m;
		k=0;
		d=int(log10(n)) + 1;
		z=pow(10,d-1);
		for (i=n; i<=m; i++) {
			y=i;
			for (j=1; j<d; j++){
				x=z*(y%10);
				x+=int(y/10);
				if ((x>=n)&&(x<=m)&&(i<x)&&(x!=lx)) {
					k++;
//					cout << i << ":" << x << endl;
					lx=x;
				}
				y=x;
			}
		}
		cout << "Case #" << l+1 << ": " << k << endl;
	}	
	return 0;
}
