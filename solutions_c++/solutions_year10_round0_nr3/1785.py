#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct node{
	int i;
	int k;
};

int main(){
	freopen("C-large-2.in","r",stdin);
	freopen("C-large-2.out","w",stdout);
	int T;
	int n,r,k;
	int index = 0;
	cin>>T;
	while (T--){
		long long res = 0;
		int cnt = 0;
		cin>>r>>k>>n;
		queue<node> q;
		vector<long long> ans;
	//	map<int,int> mm;
		for (int i=0 ;i<n; ++i){
			node t;
			cin>>t.k;
			t.i = i;
			q.push(t);
		}
		ans.push_back(0);
		for (int i=0 ;i<r; ++i){
			int t = 0;
			int tmp = q.size();
			if (i > 0 && q.front().i == 0) break;
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
		//cout<<st << " "<< cnt<<" "<<res <<" "<<endl;
		long long tot =(r/cnt)*res + ans[r%cnt];
		printf("Case #%d: %I64d\n",++index,tot);
	}
	return 0;
}
