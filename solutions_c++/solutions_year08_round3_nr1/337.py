
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

#define FOR(i,a) for(int i=0;i<a;i++)
#define FORIT(it,a) for(__typeof(a.begin()) it=a.begin();ii!=a.end();it++)
#define ALL(a) a.begin(),a.end()

typedef long long ll;

int main(){
	int nn;
	cin>>nn;
	for(int npr=1;npr<=nn;npr++){
		set<int> s;
		int p,k,l;
		cin>>p>>k>>l;
		vector<int> v(l);
		for(int i=0;i<l;i++){
			cin>>v[i];
		}
		sort(ALL(v));
		reverse(ALL(v));

		int pos=0;
		ll ans=0;
		for(int i=1;;i++){
			for(int t=0;t<k;t++){
				ans+=i*v[pos];
				pos++;
				if(pos==l)goto end;
			}
		}
end:

		cout<<"Case #"<<npr<<": "<<ans<<endl;
	}

	return 0;
}
