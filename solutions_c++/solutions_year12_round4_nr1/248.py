#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
int N;
const int MN = 10*1000+15;
int ds[MN];
int ls[MN];
typedef pair<int,int> P;
P ps[MN];
int D;

int reach[MN];

int main() {
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>N;
		for(int i=0; i<N; ++i) {
			cin>>ps[i].first>>ps[i].second;
		}
		sort(ps,ps+N);
		for(int i=0; i<N; ++i) ds[i]=ps[i].first, ls[i]=ps[i].second;
		cin>>D;
		ds[N]=D;
		ls[N]=0;
		memset(reach,-1,sizeof(reach));

		reach[0] = ds[0];
		for(int i=0; i<N; ++i) {
			if (reach[i]<0) continue;
			for(int j=i+1; j<=N; ++j) {
				if (ds[i]+reach[i] < ds[j]) break;
				int r = min(ds[j]-ds[i], ls[j]);
//				cout<<"reaching "<<j<<" from "<<i<<" : "<<r<<'\n';
				reach[j] = max(reach[j], r);
			}
		}
		cout<<"Case #"<<a<<": "<<(reach[N]>=0 ? "YES" : "NO")<<'\n';
	}
}
