#include <algorithm>
#include <iostream>
using namespace std;

int main() {
	int N,P,Q,ans,cnt,i,j,r[5],p[100];
	
	cin >> N;
	for (int testcase=1;testcase<=N;testcase++) {
		ans = INT_MAX;
		
		cin >> P >> Q;
		for (i=0;i<Q;i++) {
			cin >> r[i];
			r[i]--;
		}
		
		sort(r,r+Q);
		do {
			for (i=0;i<P;i++) p[i] = 1;
			for (i=0,cnt=0;i<Q;i++) {
				p[r[i]] = 0;
				for (j=r[i]+1;j<P&&p[j];j++) cnt++;
				for (j=r[i]-1;j>=0&&p[j];j--) cnt++;
			}
			ans = min(ans,cnt);
		} while (next_permutation(r,r+Q));
		cout << "Case #" << testcase << ": " << ans << endl;
	}
	
	return 0;
}
