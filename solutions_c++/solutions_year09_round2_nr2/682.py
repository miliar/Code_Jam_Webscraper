#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int i,T,t;
	string a,b;
	
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	cin >> T;
	char c;
	
	for(t=1;t<=T;t++) {
		cin >> a;
		b=a;
		next_permutation(a.begin(),a.end());
		
		cout << "Case #"<<t<<": ";
		
		if(a>b) cout << a << endl;
		else {
			for(i=0;i<a.size();i++) {
				if(a[i]=='0') continue;
				b=a[i];
				a.erase(a.begin()+i);
				a.insert(0,b);
				break;
			}
			
			a.insert(1,"0");
			
			cout << a << endl;
		}
	}
}
