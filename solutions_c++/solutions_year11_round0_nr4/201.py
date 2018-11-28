#include<iostream>
#include<vector>
#include<iomanip>
#define MAX 10000
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; cin>>T;
	for (int t=1; t<=T; t++) {
		int N; cin>>N;
		int v[N], counter[MAX];
		for (int i=0; i<MAX; i++) counter[i]=0;
		for (int i=0; i<N; i++) cin>>v[i];
		for (int i=0; i<N; i++) {
			int c=0;
			int j=i;
			while(1) {
				j=v[j]-1; c++;
				if(i==j) break;
			}
			counter[c]++;
		}
		for (int i=2; i<MAX; i++) counter[i]/=i;
		double ans=0;
		for (int i=2; i<MAX; i++) ans+=counter[i]*i;
		cout << setprecision(6) << fixed << "Case #" << t << ": " << ans << endl;		
	}
	return 0;
}
