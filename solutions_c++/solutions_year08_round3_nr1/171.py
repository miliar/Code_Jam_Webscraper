#include <iostream>
#include <algorithm>

using namespace std;

const int nmax = 1005;

int a[nmax*nmax];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int test;
	cin >> test;

	for (int t = 1;t <= test; ++t){
		int p,k,l;
		cin >> p >> k >> l;
		for (int i = 0;i < l; ++i) cin >> a[i];
		sort(a,a+l);
		reverse(a,a+l);
		long long ans = 0;

		for (int i = 0;i < l; ++i)
			ans += (long long)((long long)(i / k + 1)) * a[i];
		cout << "Case #"<<t<<": "<<ans<<endl;		
	}
	return 0;
}