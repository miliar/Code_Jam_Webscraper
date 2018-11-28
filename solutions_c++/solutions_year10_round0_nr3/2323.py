#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<stack>
using namespace std;

int t,k,i,j,R,K,N;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin >> t;
	for (k=0;k<t;k++) {
		cin >> R >> K >> N;
		queue<int> q1,q2;
		long long res=0;
		for (i=0;i<N;i++) {
			int num;
			cin >> num;
			q1.push(num);
		}
		for (i=0;i<R;i++) {
			while (!q2.empty()) {q1.push(q2.front()); q2.pop(); }
			int col=0;
			while (!q1.empty() && (col+q1.front())<=K) {col+=q1.front(); q2.push(q1.front()); q1.pop(); }
			res+=col;
		}
		cout << "Case #" << k+1 << ": " << res << endl;
	}
	return 0;
}
