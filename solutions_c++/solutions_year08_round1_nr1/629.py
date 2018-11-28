#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	long long int testes, n, minimo, j, k;
	
	cin >> testes;
	
	for(long long int i=1; i<=testes; i++) {
		cout << "Case #" << i << ": ";
		
		cin >> n;
		
		long long int a[n], b[n];
		
		for(j=0; j<n; j++)
			cin >> a[j];
		for(j=0; j<n; j++)
			cin >> b[j];
		
		sort(&a[0], &a[n-1]+1);
		sort(&b[0], &b[n-1]+1);
		
		minimo = 0;
		
		
		for(j=0, k=n-1; j<n; j++, k--)
			minimo += a[j]*b[k];
		
		cout << minimo << endl;
	}
	
	
	return(0);
}
