#include <iostream>
#include <queue>
#include <vector>
#include <map>
using namespace std;

struct node{int i;int k;};

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T;
	int n,r,k;
	int index = 0;
	scanf("%d",&T);
	while (T--){
		long long res = 0,cnt = 0;

		scanf("%d %d %d",&r,&k,&n);
		queue<node> q;
		vector<long long> anstemp;
		map<int,int> hash;
		for (int i=0 ;i<n; ++i){
			node t;
			scanf("%d",&t.k);
			t.i = i;
			q.push(t);
		}
		anstemp.push_back(0);
		int start = 0;
		
		for (int i=1 ;i<=r; ++i){
			int t = 0;
			int tmp = q.size();
			if (hash[q.front().i]) {
				start = hash[q.front().i]-1;
				cnt = i-start-1;
				break;
			}
			hash[q.front().i] = i;
			while (t + q.front().k <= k && tmp--){
				t += q.front().k;
				q.push(q.front());
				q.pop();
			}
			cnt++;
			anstemp.push_back(t);
			anstemp[anstemp.size()-1] += anstemp[anstemp.size()-2];
			res += t;
		}

		res -= anstemp[start];
		r -= start;

		long long ans = (r/cnt)*res + anstemp[start+r%cnt];
		printf("Case #%d: %I64d\n",++index,ans);
	}
	return 0;
}
