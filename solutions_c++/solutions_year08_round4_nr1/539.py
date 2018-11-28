#include <iostream>
#include <vector>
#include <map>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)
typedef long long i64;

int main(void) {
	int N;
	cin >> N;
	fu(ts,1,N+1) {
		cout << "Case #" << ts << ": ";
		int M;
		cin >> M;
		vector<i64> v,w;
		i64 x;
		fu(i,0,M) { cin >> x; v.push_back(x); }
		fu(i,0,M) { cin >> x; w.push_back(x); }
		sort(v.begin(),v.end());
		sort(w.begin(),w.end());
		reverse(w.begin(),w.end());
		i64 ret=1000000000;
		//do {
			i64 cur=0;
			fu(i,0,M) cur+=v[i]*w[i];
			ret<?=cur;
		//} while(next_permutation(w.begin(),w.end()));
		cout << ret << endl;
	}
}
