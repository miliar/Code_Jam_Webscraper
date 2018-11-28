#include <iostream>
#include <vector>
#include <string>

using namespace std;

string L;
string vs[10000];
int mask[26][10000];
int first;

pair<int, int> dfs(vector<int> vi, int idx){
	if(vi.size() == 1) return make_pair(0, vi[0]);
	vector< pair<int,int> > vp(vi.size());
	for(int i=0;i<vi.size();i++)
		vp[i] = make_pair(mask[L[idx]-'a'][vi[i]], vi[i]);
	sort(vp.begin(), vp.end());
	pair<int,int> res = make_pair(0, 10000000);
	for(int i=0;i<vi.size(); ){
		vector<int> vii;
		int j=i;
		while(j<vi.size()&&vp[j].first == vp[i].first) vii.push_back(vp[j++].second);
		pair<int,int> cur = dfs(vii, idx+1);
		if(vii.size()!=vi.size() && vp[i].first == 0) cur.first--;
		res = min(cur, res);
		i=j;
	}
	return res;
}

int main(){
	int TEST; cin >> TEST;
	for(int test=1;test<=TEST;test++){
		int N, M; cin >> N >> M;
		for(int i=0;i<N;i++) cin >> vs[i];
		memset(mask, 0, sizeof(mask));
		for(int i=0;i<N;i++){
			for(int j=0;j<vs[i].size();j++)
				mask[vs[i][j]-'a'][i] |= (1<<j);
		}
		printf("Case #%d:", test);
		for(int i=0;i<M;i++){
			cin >> L;
			vector<int> vi[10];
			for(int j=0;j<N;j++)
				vi[vs[j].size()-1].push_back(j);
			pair<int,int> res = make_pair(0,0);
			for(int j=0;j<10;j++){
				if(vi[j].empty()) continue;
				res = min(res, dfs(vi[j], 0));
			}
			printf(" %s", vs[res.second].c_str());
		}
		printf("\n");
	}
}