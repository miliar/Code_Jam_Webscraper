#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <iterator>
using namespace std;

map<int, int> M;

void solve(){
	int len, walk, run, n;
	double runt;
	scanf("%d%d%d%lf%d", &len, &walk, &run, &runt, &n);
	M.clear();
	M[0] = len;
	int st, ed, v;
	for (int i = 0; i < n; i++){
		scanf("%d%d%d", &st, &ed, &v);
		if (M.find(v) == M.end())
			M[v] = ed - st;
		else
			M[v] += ed - st;
		M[0] -= ed - st;
	}

	double cost = 0;
	for (map<int, int>::iterator i = M.begin(); i != M.end(); i ++){
		if (runt * (i->first + run) > i->second){
			cost += (double)i->second / (i->first + run);
			runt -= (double)i->second / (i->first + run);
		}
		else{
			cost += runt + (i->second - runt * (i->first + run)) / (i->first + walk);
			runt = 0;
		}
	}
	printf("%.8lf\n", cost);
}

int main(){
	freopen("Airport.in", "r", stdin);
	freopen("Airport.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
