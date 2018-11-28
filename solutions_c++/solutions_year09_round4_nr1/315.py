#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

set<vector<int> > vis;
int last[1000], N;

bool check(vector<int>& v){

	for(int i = 1 ; i <= N ; i++){
		int x = v[i-1];
		if(last[x] > i)
			return false;
	}
	return true;
}

void print(vector<int>& v){
	for(int i = 0 ; i < v.size() ; i++)
		cout << v[i] << " " ;
	cout << endl << endl;
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small-attempt0.out", "wt", stdout);
	//freopen("A-large.in", "rt", stdin);
	//freopen("A-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){

		memset(last, 0, sizeof last);
		vis.clear();

		cin >> N;
		for(int i = 0 ; i < N ; i++){
			string str; cin >> str;
			for(int j = 0 ; j < N ; j++)
				if(str[j] == '1')
					last[i] = j+1;
		}

		vector<int> v;
		for(int i = 0 ; i < N ; i++)
			v.push_back(i);

		queue<vector<int> > q;
		q.push(v);
		vis.insert(v);

		int level = 0, best = -1;
		while(!q.empty()){

			int s = q.size();
			for(int i = 0 ; i < s ; i++){
				vector<int> v = q.front(); q.pop();
				//print(v);
				if(check(v)){
					best = level;
					goto done;
				}

				for(int j = 0 ; j < v.size()-1 ; j++){
					vector<int> vv = v;
					swap(vv[j], vv[j+1]);
					if((vis.insert(vv)).second)
						q.push(vv);
				}
			}

			level++;
		}

done:
		printf("Case #%d: %d\n", t+1, best);

	}

	return 0;
}
