#include <iostream>
#include <cmath>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);

	int t;
	cin>>t;
	for (int i=1; i<=t; i++) {
		int n,s,p;
		int count=0;
		cin>>n>>s>>p;
		for (int j=0; j<n; j++) {
			int tmp;
			cin>>tmp;
			int a,b,c;
			a=b=c=floor((double)tmp/3);
			if (tmp%3 == 1) {
				c++;
				if (c >= p) count++;
			}
			else if (tmp%3 == 2) {
				b++;c++;
				if (c >= p) count++;
				else if (c+1 >= p && s) {count++;s--;}
			}
			else {
				if (c >= p) count++;
				else if (c+1 >= p && s && a-1 >= 0) {count++;s--;}
			}
		}
		cout<<"Case #"<<i<<": "<<count<<"\n";
	}

	return 0;
}
