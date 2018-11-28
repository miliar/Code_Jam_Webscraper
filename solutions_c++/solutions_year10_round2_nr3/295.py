#include <iostream>
#include <algorithm>
using namespace std;
int N;
int bin[1024][1024];
const int Z = 100003;
int arr[1024][1024];
int main()
{
	bin[0][0]=1;
	for(int i=1; i<1024; ++i) {
		bin[i][0]=1;
		for(int j=1; j<1024; ++j)
			bin[i][j] = (bin[i-1][j-1] + bin[i-1][j]) % Z;
	}

	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>N;
		for(int i=2; i<=N; ++i) arr[i][1]=1;
		for(int n=3; n<=N; ++n) {
			for(int k=2; k<n; ++k) {
				int x=0;
				for(int i=1; i<k; ++i)
					x = (x + arr[k][i] * bin[n-k-1][k-i-1]) % Z;
				arr[n][k] = x;
//				cout<<"asd "<<n<<' '<<k<<' '<<x<<'\n';
			}
		}
		int r=0;
		for(int k=1; k<N; ++k) r = (r + arr[N][k]) % Z;
		cout<<"Case #"<<a<<": "<<r<<'\n';
	}
}
