#include <iostream>
#include <fstream>
#include <map>

using namespace std;

long long g[1111];
map<int,pair<int,long long>> H;

long long getSum(int hod) {
	for (map<int,pair<int,long long>>::iterator i = H.begin(); i!=H.end(); i++)
		if (i->second.first == hod)
			return i->second.second;
	return 0;
}

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T; cin>>T;
	for (int t=1; t<=T; t++) {
		long long res = 0;
		long long R,k,n;
		cin>>R>>k>>n;
		for (int i=0; i<n; i++)
			cin>>g[i];
		H.clear();
		H.insert(make_pair(0,make_pair(0,0)));
		long long hod = 0, pos = 0, sum = 0;
		while (true) {
			long long ss = 0; hod++;
			for (int j=0; j<n; j++) {
				int pp = (pos+j)%n;
				if (ss+g[pp]<=k)
					ss+=g[pp];
				else {
					pos = pp;
					break;
				}
			}
			sum+=ss;
			if (H.count(pos)==0)
				H.insert(make_pair(pos,make_pair(hod,sum)));
			else
				break;
		}
		if (R<H[pos].first) {
			res = getSum(R);
			R = 0;
		} else {
			R -= H[pos].first;
			res = H[pos].second;
		}
		int len = hod - H[pos].first;
		res += (R/len)*(sum-H[pos].second);
		R %= len;
		res += getSum(H[pos].first+R)-getSum(H[pos].first);
		cout<<"Case #"<<t<<": "<<res<<"\n";
	}
}