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

vector<int> getCycles(vector<int> vec){

	vector<bool> visited(vec.size(), false);
	vector<int> cycles;

	while(true){
		int start = -1, i;
		for(i = 0 ; i < vec.size() ; i++)
			if(!visited[i]){
				start = i;
				break;
			}
		if(start == -1)
			break;
		i = start;
		vector<int> cycle;
		while(true){
			cycle.push_back(i);
			visited[i] = true;

			i = vec[i];
			if(i == start)
				break;
		}
		cycles.push_back(cycle.size());
	}
	return cycles;
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("D-small-attempt0.in", "rt", stdin);
	//freopen("D-small-attempt0.out", "wt", stdout);
	//freopen("D-small-attempt1.in", "rt", stdin);
	//freopen("D-small-attempt1.out", "wt", stdout);
	freopen("D-large.in", "rt", stdin);
	freopen("D-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		//cerr << "Solving testcase " << t+1 << endl;

		int N; cin >> N;
		vector<int> v;
		for(int i = 0 ; i < N ; i++){
			int x; cin >> x;
			x--;
			v.push_back(x);
		}
		//print(v);
		vector<int> cycles = getCycles(v);
		double d = 0;
		for(int i = 0 ; i < (int)cycles.size() ; i++){
			if(cycles[i] == 1)
				continue;
			d += cycles[i];
		}

		printf("Case #%d: %.9lf\n", t+1, d);
	}

	return 0;
}
