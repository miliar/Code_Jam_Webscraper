#include <iostream>

using namespace std;

int main()
{
	int i, t, n, k, l, j, a[30];
	
	a[0]=1;
	for (i=1; i<30; i++)
		a[i]=a[i-1]*2;
		
//	cout << a[29] << endl;
	
	cin >> t;
	
	for (i=0; i<t; i++) {
		cin >> n >> k;
		l=1;
		for (j=1; j<=n; j++) {
			if ((k%a[j])<a[j-1]) l=0;
		} 
		if (l) cout << "Case #" << i+1 << ": ON" << endl;
	  else cout << "Case #" << i+1 << ": OFF" << endl;
	}
		
	return 0;
}
