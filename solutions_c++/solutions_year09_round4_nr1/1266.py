#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

int graph[100][100];

struct State {
	vector<int> v;
	int cost;
};

bool check(vector<int> &v){
	for(int i = 0; i < v.size(); i++){
		if(v[i] > i + 1){
			return false;
		}
	}
	return true;
}

int solve(vector<int> &v){
	set<vector<int> > memo;
	queue<State> q;
	{
		State s;
		s.v = v;
		s.cost = 0;
		q.push(s);
	}

	while(!q.empty()){
		State s = q.front();q.pop();
		if(memo.find(s.v) == memo.end()){
			memo.insert(s.v);
		} else {
			continue;
		}
		if(check(s.v)){
			return s.cost;
		}
		for(int i = 0; i < s.v.size() - 1; i++){
			if(s.v[i] > s.v[i + 1]){
			State ns(s);
			swap(ns.v[i], ns.v[i+1]);
			ns.cost++;
			q.push(ns);
				}
		}
	}
	return -1;
}

int main(){
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int n;
		vector<int> v;
		cin >> n;
		for(int j = 0; j < n; j++){
			int max = 0;
			for(int k = 0; k < n; k++){
				char t;
				cin >> t;
				if(t == '1'){
					max = k + 1;
				}
			};
			v.push_back(max);
		}
		cout << "Case #" << (i + 1) << ": " << solve(v) << endl;
	}
}
