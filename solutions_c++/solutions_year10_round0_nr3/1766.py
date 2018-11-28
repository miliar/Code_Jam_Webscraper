#include <iostream>
#include <queue>
#include <vector>
#include <map>
using namespace std;

struct node{
	int i;
	int k;
};

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T;
	int n,r,k;
	int index = 0;
	cin>>T;
	while (T--){
		long long res = 0;
		long long cnt = 0;
		cin>>r>>k>>n;
		queue<node> q;
		vector<long long> ans;
		map<int,int> mm;
		for (int i=0 ;i<n; ++i){
			node t;
			cin>>t.k;
			t.i = i;
			q.push(t);
		}
		ans.push_back(0);
		int st = 0;
		
		for (int i=1 ;i<=r; ++i){
			int t = 0;
			int tmp = q.size();
			if (mm[q.front().i]) {
				st = mm[q.front().i]-1;
				cnt = i-st-1;
				break;
			}
			mm[q.front().i] = i;
			while (tmp--){
				if (t + q.front().k > k) break;
				t += q.front().k;
				q.push(q.front());
				q.pop();
			}
			++cnt;
			ans.push_back(t);
			ans[ans.size()-1] += ans[ans.size()-2];
			res += t;
		}
		//for (int i=0 ;i<cnt; ++i) cout<<ans[i]<<" "; cout<<endl;
		res -= ans[st];
		r -= st;
		//cout<<st << " "<< cnt<<" "<<res <<" "<<endl;
		long long tot = ans[st]+(r/cnt)*res + ans[st+r%cnt]-ans[st];
		printf("Case #%d: %I64d\n",++index,tot);
	}
	return 0;
}
