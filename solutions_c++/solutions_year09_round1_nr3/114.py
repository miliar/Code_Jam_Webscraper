#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <sstream>

using namespace std;

long long z[50][50];
double f[50];
int c,n;

int main() {
	cout.precision(7);
	cout<<fixed;
	z[0][0]=1;
	z[1][0]=1;
	z[1][1]=1;
	for(int i=2;i<42;i++) {
		z[i][0]=1;
		z[i][i]=1;
		for(int j=1;j<i;j++) z[i][j]=z[i-1][j]+z[i-1][j-1];
	}
	int TT;
	cin>>TT;
	for(int T=1;T<=TT;T++) {
		cin>>c>>n;
		f[0]=0;
		for(int i=1;i<=c;i++) {
			double p0=z[c-i][n]*1.0/z[c][n];
			f[i]=0;
			for(int k=1;k<=i && k<=n;k++) {
				double p=(z[i][k]*1.0*z[c-i][n-k]*1.0/z[c][n]);
				f[i]+=(f[i-k]+1)*p;
				//cout<<i<<' '<<k<<' '<<f[i-k]<<' '<<p<<' '<<f[i]<<endl;
			}
			f[i]+=p0;
			f[i]/=(1-p0);
			//cout<<p0<<"  "<<f[i]<<endl;
		}

		cout<<"Case #"<<T<<": ";
		cout<<f[c]<<endl;
	}
	return 0;
}

