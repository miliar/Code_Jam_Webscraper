#include <iostream>

using namespace std;

int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int t;
	cin >>t;
	for (int u=1;u<=t;u++){
		int n;
		cin >>n;
		int minn=1e10;
		int sum=0;
		int xsum=0;
		for (int i=0;i<n;i++) {
			int a;
			cin >> a;
			xsum^=a;
			sum+=a;
			minn=min(minn,a);
		}
		cout <<"Case #"<<u<<": ";
		if (xsum) cout <<"NO" <<endl; else cout << sum-minn<<endl;

	
	}
	return 0;
}
