#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

typedef long long ll;

bool fin[64];
int num[64], idx;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, NT, i, j, n, b, k, t, p, res;
	int x[64], v[64];
	cin>>NT;
	for(T = 1; T <= NT; ++T) {
		cin>>n>>k>>b>>t;
		memset(fin, 0, sizeof(fin));
		memset(num, 0, sizeof(num));
		for(i=0; i<n; ++i) {
			cin>>x[i];
		}
		for(i=0; i<n; ++i) {
			cin>>v[i];
		}
		p=0;
		idx=0;
		res=0;
		for(i=0; i<n; ++i) {
			if (x[i] + v[i]*t >= b) {
				++p;
				fin[i] = true;
			}
		}
		if (p<k) {
			cout<<"Case #"<<T<<": IMPOSSIBLE"<<endl;
			continue;
		}
		for(i=0; i<n; ++i) {
			if (fin[i]) {
				for(j=0; j<n; ++j) {
					if (!fin[j] && x[i] < x[j]) {
						++num[idx];
					}
				}
				++idx;
			}
		}
		sort(num, num+idx);
		for(i=0; i<k; ++i) {
			res+=num[i];
		}
		cout<<"Case #"<<T<<": "<<res<<endl;
	}
	return 0;
}