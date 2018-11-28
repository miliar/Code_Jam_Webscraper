#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef long long int int64;


/*
int solve(int r, int k, queue<int> q){
	int sum = 0;
	while(r--){
		int n = 0;
		queue<int> used;
		while(n + q.front() <= k and !q.empty()){
			int f = q.front();
			n += f;
			q.pop();
			used.push(f);
		}
		while(!used.empty()){
			q.push(used.front());
			used.pop();
		}
		sum += n;
	}
	return sum;
}
*/

void buildElement(int64 k, vector<int64> &v, vector<int64> &va, vector<int64> &vn, int64 index){
	int64 amount = 0;
	for(int64 l = index; l < v.size() + index; l++){
		int64 i = l % v.size();
		amount += v[i];
		va[index] = amount;
		vn[index] = i;
		if(amount > k){
			va[index] = amount - v[i];
			return;
		}
	}
}

void buildTable(int64 k, vector<int64> &v, vector<int64> &va, vector<int64> &vn){
	for(int64 i = 0; i < v.size(); i++){
		buildElement(k, v, va, vn, i);
		//		cout << va[i] << "\t" << vn[i] << "\t" << endl;
	}
}

int64 solve(int64 r, int64 k, vector<int64> v){
	vector<int64> amounts(v.size());
	vector<int64> nexts(v.size());
	buildTable(k, v, amounts, nexts);
	int64 current = 0;
	int64 sum = 0;
	while(r--){
		sum += amounts[current];
		current = nexts[current];
	}
	return sum;
}

int main(){
	int64 t;
	cin >> t;
	for(int64 i = 0; i < t; i++){
		int64 r, k, n;
		cin >> r >> k >> n;
		vector<int64> p;
		for(int64 i = 0; i < n; i++){
			int64 t;
			cin >> t;
			p.push_back(t);
		}
		cout << "Case #" << (i+1) << ": " << solve(r, k, p) << endl;
	}
}
