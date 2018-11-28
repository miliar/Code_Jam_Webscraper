#include <iostream>
#include <vector>
#include <map>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)

int main(void) {
	int N;
	cin >> N;
	fu(ts,1,N+1) {
		map<string,int> engines;
		cout << "Case #" << ts << ": ";
		int M;
		cin >> M;
		vector<int> v,w;
		int x;
		fu(i,0,M) { cin >> x; v.push_back(x); }
		fu(i,0,M) { cin >> x; w.push_back(x); }
		sort(v.begin(),v.end());
		sort(w.begin(),w.end());
		int ret=1000000000;
		do {
			int cur=0;
			fu(i,0,M) cur+=v[i]*w[i];
			ret<?=cur;
		} while(next_permutation(w.begin(),w.end()));
		cout << ret << endl;
	}
}
