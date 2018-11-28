#include <iostream>
using namespace  std;
int max(int a, int b){
	if (a>b)
		return a;
	return b;
}
int main()
{
	int n;
	cin>>n;
	for(int icase=1; icase<=n; icase++){
		int t, loc;
		char c;
		cin>> t;
		pair<int, int> a, b;
		a=make_pair(0,1);
		b=make_pair(0,1);
		while(t--){
			cin>> c >> loc;
			if(c=='O'){
				a.first=max(a.first+abs(loc-a.second)+1, b.first+1);
				a.second=loc;
			}
			else{
				b.first=max(b.first+abs(loc-b.second)+1, a.first+1);
				b.second=loc;
			}
			//cerr<<a.first<<" " << a.second<<endl;
			//cerr<<b.first<<" " << b.second<<endl;
			//cerr<<endl;
		}
		cout<<"Case #"<<icase<<": "<<max(a.first, b.first)<<endl;
	}
}

