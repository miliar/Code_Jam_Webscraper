#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int cost[2005], ret, p;
int req[1050];
bool was[8000];

void DFS(int round, int &need){
	if (round == 1){
		if (need){
			if (!was[round]){
				ret++;
				was[round] = true;
			}
			need--;
		}
		return;
	}
	DFS(round >> 1, need);
	if (need){
		if (!was[round]){
			ret++;
			was[round] = true;
		}
		need--;
		return;
	}
}

int main(){
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int t;
	cin >> t;
	for (int I=0; I<t; I++){
		cout << "Case #" << I+1 << ": ";
		ret = 0;
		cin >> p;
		memset(was, 0, sizeof was);
		for (int i=0; i<1<<p; i++){
			cin >> req[i];
			req[i] = p - req[i];
		}
		int left;
		for (int i=1; i<1<<p; i++){
			cin >> cost[i];
		}
		for (int i=0; i<1<<p; i++){
			DFS((1<<p) + i, req[i]);
		}
		cout << ret << endl;
	}
	return 0;
}