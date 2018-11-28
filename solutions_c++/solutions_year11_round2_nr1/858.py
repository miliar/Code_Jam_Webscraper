#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
	int i, j, k, n, t, w[110], l[110], g[110], a[110][110];
	double wp[110],owp[110], oowp[110], pri[110];
	char c;
	
	cin >> t;
	for (k=0; k<t; k++) {
		cin >> n;
		for (i=0; i<n; i++) w[i]=0;
		for (i=0; i<n; i++) l[i]=0;
		for (i=0; i<n; i++) {
			for (j=0; j<n; j++) {
				a[i][j]=0;
				cin >> c;
					if (c=='1') {
						w[i]++;
						a[i][j]=1;
					}
					if (c=='0') {
						l[i]++;
						a[i][j]=2;
					}
			}
		}
		for (i=0; i<n; i++) g[i]=w[i]+l[i];
		for (i=0; i<n; i++) {
			wp[i]=1.0*w[i]/g[i];
			owp[i]=0.0;
			for (j=0; j<n; j++) {
				if (a[i][j]) owp[i]+=1.0*(w[j]-a[i][j]+1)/(g[j]-1)/g[i];
			}
		}
		for (i=0; i<n; i++) {
			oowp[i]=0.0;
			for (j=0; j<n; j++) {
				if (a[i][j]) oowp[i]+=1.0*owp[j]/g[i];
			}
		}
		for (i=0; i<n; i++) pri[i]=0.25*wp[i]+0.50*owp[i]+0.25*oowp[i];
		cout << "Case #" << k+1 << ":" << endl;
		for (i=0; i<n; i++) cout << pri[i] << endl;
	}
	return 0;
}
