#include<cstdio>
#include<iostream>
#define L 2000

using namespace std;

typedef long long ll;

int T,I;
ll r,k,n,g[L],tim[L],cost[L];
ll s,i,st,now,tot;

int main(){
	cin >> T;
	while (T--){
		cout << "Case #" << ++I << ": ";
		cin >> r >> k >> n;
		s=0;
		for (i=0;i<n;++i) {cin >> g[i];s+=g[i];}
		if (s<=k){
			cout << s*r << endl;
			continue;
		}
		for (i=0;i<n;++i) {
			tim[i]=-1;
			cost[i]=0;
		}
		st=0;now=0;
		for (i=0;i<r;){
			tot=0;
			while (tot+g[st]<=k) {
				tot+=g[st++];
				if (st==n) st=0;
			}
			now+=tot;
			if (tim[st]==-2) {
				++i;
			}
			else if (tim[st]==-1){
				tim[st]=i;
				cost[st]=now;
				++i;
			}
			else{
				now+=(r-i-1)/(i-tim[st])*(now-cost[st]);
				r=(r-i-1)%(i-tim[st]);
				for (i=0;i<n;++i) tim[i]=-2;
				i=0;
			}
		}
		cout << now << endl;
	}
}
