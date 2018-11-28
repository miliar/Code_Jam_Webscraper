

#include <iostream>

using namespace std;





int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int t;
	cin >> t;
	for (int u=1;u<=t;u++){
		int n;		cin >>n;
		int ans=n,a;

		for (int i=1;i<=n;i++) {cin >>a;if (a==i) ans--;}
		cout <<"Case #"<<u<<": "<<ans<<".000000"<<endl;
	
	}


	return 0;

}

