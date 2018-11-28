#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

VPII ab;

bool cmp_b(const PII &i, const PII &j) {
	return ab[i.first].second<ab[j.first].second;
}


int main() {
	int t,c;
	cin>>t;
	for (c=1;c<=t;++c) {
		int n;
		cin>>n;
		ab=VPII(n);
		VPII aa(n);
		for (int i=0;i<n;++i) {
			cin>>ab[i].first>>ab[i].second;
			aa[i].first=aa[i].second=i;
		}
		sort(ab.begin(),ab.end());
		sort(aa.begin(),aa.end(),cmp_b);
		int s=0;
		for (int i=0;i<n;++i)
			s+=abs(aa[i].second-i);
		cout<<"Case #"<<c<<": "<<s/2<<endl;
	}
	return 0;
}
