#include <iostream>
#include <boost/dynamic_bitset.hpp>

using namespace std;
using namespace boost;

typedef unsigned long ulong;
dynamic_bitset<> sum,tmp;

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	ulong t,n,num,minnum,allsum; cin>>t;
	for (ulong k=1; k<=t; k++) {
		minnum = 1<<20;
		allsum = 0;
		dynamic_bitset<> sum(20,0);
		cin>>n;
		for (int i=0; i<n; i++) {
			cin>>num;
			if (minnum>num) minnum=num;
			allsum+=num;
			dynamic_bitset<> tmp(20, num);
			sum^=tmp;
		}

		cout<<"Case #"<<k<<": ";
		if (sum.to_ulong()!=0) {
			cout<<"NO\n";
		}
		else {
			cout<<allsum-minnum<<endl;
		}
	}
}
