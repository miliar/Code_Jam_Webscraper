#include <iostream>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int Test;
	cin>>Test;
	long n, k;
	long m = 1;
	for (int cas = 1; cas <= Test; ++cas) {
		m = 1;
		cout <<"Case #"<<cas<<": ";
		
		cin>>n>>k;
		//cout<<"k = "<<k<<" m = "<<m<<endl;
		if ( k == 0) {
			cout <<"OFF"<<endl;
			continue;
		}
		for (int i = 1; i <= n; ++i) {
			m *= 2;
		}
		k -= (m-1);
		//cout<<"k = "<<k<<" m = "<<m<<endl;
		if (k % m == 0) {
			cout<<"ON"<<endl;
		}
		else 
			cout <<"OFF"<<endl;
		
	}
	return 0;
}	
