#include <iostream>
using namespace std;

int main()
{
	int t, n, s, p, i, j, k, l, a[101];
	
	cin >> t;
	for (l=0; l<t; l++) {
		cin >> n >> s >> p;
		for (i=0; i<n; i++)
			cin >> a[i];
		k=0; j=0;
		for (i=0; i<n; i++) {
			if (a[i] > (3*p-3)) k++;
			if ((a[i] > (3*p-5)) && (a[i] < (3*p-2))) j++;
		}
		if (j<s) s=j;
		k=k+s;
		if (p==1) {
			k=0;
			for (i=0; i<n; i++) 
				if (a[i] > 0) k++;
		}
		cout << "Case #" << l+1 << ": " << k << endl;;
	}	
	return 0;
}
