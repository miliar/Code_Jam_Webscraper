#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;

const int L=1000;
ll fills[L];
int next[L];
int size[L];
int seen[L];
ll got[L];

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;++t) {
		int R,k,N;
		cin >> R >> k >> N;
		for (int i=0;i<N;++i) cin >> size[i];
		memset(next,-1,sizeof(next));
		for (int i=0;i<N;++i) {
			fills[i]=0;
			int j;
			for (int kk=0;kk<N;++kk) {
				j=(i+kk)%N;
				if (fills[i]+size[j]>k) break;
				fills[i]+=size[j];
			}
			next[i]=j;
		}
		memset(seen,-1,sizeof(seen));
		int x=0;
		ll money=0;
		bool cycled=false;
		for (int i=0;i<R;++i) {
			if (cycled || seen[x]==-1) {
				seen[x]=i;
				got[x]=money;
				money+=fills[x];
				x=next[x];
			}
			else {
				int length=i-seen[x];
				ll get=money-got[x];
				int more=(R-i)/length;
				i+=more*length;
				money+=more*get;
				cycled=true;
				i--;
			}
		}
		cout << "Case #" << t << ": " << money << endl;
	}
}
