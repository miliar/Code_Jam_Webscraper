#include <iostream>
#include <cmath>
using namespace std;

int main(){
	register long long int aux, k, suma;
	register int z, a, i, j, n, t, R;
	long long int v[1010];
	cin >> t;
	for(z = 1; z <= t; z++){
		cin >> R >> k >> n;
		for(i = 0; i < n; i++)
			cin >> v[i];
		suma = 0;
		for(i = j = 0; i < R; i++){
			aux = 0;
			for(a = 0; a < n && aux <= k; a++, j = (j+1)%n)
				aux+=v[j];
			if(a == n && aux <= k)
				suma+=aux;
			else{
				j = (j+n-1)%n;
				suma+=(aux-v[j]);
			}
		}
		cout << "Case #"<< z<<": "<<suma << endl;
	}
	return 0;
}
