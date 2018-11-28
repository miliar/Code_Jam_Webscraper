#include <iostream>
#include <vector>
using namespace std;
typedef vector<int> vi;

int main() {
	int nTest; cin>>nTest;
	int r,k,n;
	vi a;
	for (int test=1;test<=nTest;test++) {
		cin>>r>>k>>n;
		a.resize(n);
		for (int i=0;i<n;i++) cin>>a[i];
		vi visited(n,0);
		vi collected(n,0);
		int turn = 1, ptr = 0;
		int res = 0;
		while (turn<=r) {
			int sum = 0;
      int ptr0 = ptr;
      do {sum+=a[ptr];ptr = (ptr+1)%n;}
      while (sum+a[ptr]<=k && ptr!=ptr0);
			res += sum;
			if (visited[ptr]!=0) {
				int dturn = turn-visited[ptr];
				int dres = res-collected[ptr];
				int nturn = (r-turn)/dturn;
				turn+=dturn*nturn;
				res+=dres*nturn;
			} else {
				visited[ptr] = turn;
				collected[ptr] = res;
			}
			turn++;
		}
		cout<<"Case #"<<test<<": "<<res<<endl;
	}
}
