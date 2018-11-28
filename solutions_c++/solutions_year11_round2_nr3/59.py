#define _CRT_SECURE_NO_DEPRECATE
#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
vector<vector<int> > help(const vector<int>& v, const vector<pair<int,int> >& w){
	vector<vector<int> > ans;
	if (v.size() <= 2){
		return ans;
	}
	int n = (int)v.size();
	int m = (int)w.size();
	for (int i=0;i<m && (int)ans.size() == 0;++i){
		bool found = false;
		for (int j=0;j<n&&!found;++j){
			if (w[i].first != v[j]){
				continue;
			}
			for (int k=0;k<n;++k){
				if (k == j){
					continue;
				}
				if (w[i].second != v[k]){
					continue;
				}
				vector<int> temp1, temp2;
				for (int u=j;u!=k; u = (u+1)%n){
					temp1.push_back(v[u]);
				}
				temp1.push_back(v[k]);
				for (int u=k;u!=j; u = (u+1)%n){
					temp2.push_back(v[u]);
				}
				temp2.push_back(v[j]);
				if (temp1.size() <= 2 || temp2.size() <= 2){
					continue;
				}
				vector<vector<int> > tt = help(temp1, w);
				for (int y =0;y<tt.size();++y){
					ans.push_back(tt[y]);
				}
				tt = help(temp2, w);
				for (int y =0;y<tt.size();++y){
					ans.push_back(tt[y]);
				}
				found = true;
				break;
			}
		}
	}
	if (ans.size() == 0){
		ans.push_back(v);
	}
	return ans;
}
vector<vector<int> > get_rooms(const vector<pair<int,int> >&w, int n){
	vector<vector<int> > ans;
	vector<int> v(n);
	for (int i=0;i<n;++i){
		v[i] = i;
	}
	return help(v,w);
}

int valid(const vector<vector<int> >& rs,const vector<int>& c){
	set<int> tmp;
	for (int i=0;i<c.size();++i){
		tmp.insert(c[i]);
	}
	int u = tmp.size();
	for (int i=0;i<rs.size();++i){
		set<int> met;
		for (int j=0;j<rs[i].size();++j){
			met.insert(c[rs[i][j]]);
		}
		if (met.size() != u){
			return 0;
		}
	}
	return u;
}

int main()
{
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		int  n,m;
		cin >> n >> m;
		vector<pair<int,int> > w(m);
		for (int j=0;j<m;++j){
			cin >> w[j].first;
			w[j].first--;
		}
		for (int j=0;j<m;++j){
			cin >> w[j].second;
			w[j].second--;
		}
		vector<vector<int> > rs = get_rooms(w,n);
		int mn = rs[0].size();
		for (int i=1;i<rs.size();++i){
			mn = min(mn, (int)rs[i].size());
		}
		int lim =1;
		for (int i=0;i<n;++i){
			lim *= mn;
		}
		vector<int> ans;
		int best = 0;
		for (int t=0;t<lim;++t){
			vector<int> cs(n);
			int tt = t;
			for (int j=0;j<n;++j){
				cs[j] = tt%mn;
				tt/=mn;
			}
			int val = valid(rs,cs);
			if (val > best){
				ans = cs;
				best = val;
			}
		}
		cout<<"Case #"<<it<<": " << best<<endl;
		for (int i=0;i<ans.size();++i){
			printf("%d%c",ans[i]+1, (((i+1)==ans.size())?'\n':' '));
		}
	}
	return 0;
}
