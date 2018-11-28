#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;


main(){
	int z;
	cin >> z;
	long long X[100], Y[100];

	for(int l=0; l<z; l++){


		long long x0, y0, a, b, c, d, m, n;
		
		cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		//cout << n << a << b << c << d << endl;
		X[0] = x0;
		Y[0] = y0;
		
		for(int i=1; i<n; i++){
			x0 = (a*x0 + b) % m;
			y0 = (c*y0 + d) % m;
			X[i] = x0;
			Y[i] = y0;
		}
		int ile = 0;
		for(int i=0; i<n; i++){
			for(int j=i+1; j<n; j++){
				for(int k=j+1; k<n; k++){
					if( (X[i]+X[j]+X[k]) % 3 == 0 && (Y[i]+Y[j]+Y[k]) % 3 == 0){
						ile++;
					}
				}
			}
		}

		cout << "Case #"<< l+1 << ": " << ile << endl;
		

	}
}

