#include <sstream>
#include <set>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
#include <map>
using namespace std;

int main(){
	int T; cin >> T;
	for(int tt = 1; tt <= T; tt++){
		int n, k, b, t;
		cin >> n >> k >> b >> t;
		
		int dentro = 0;
		vector<int> x(n), xf(n);
		vector<int> v(n);
		for(int i = 0; i < n; i++) 
			cin >> x[i];
		for(int i = 0; i < n; i++)
			cin >> v[i];
		
		for(int i = 0; i < n; i++)
			xf[i] = x[i] + v[i] * t;
		
		vector<int> cost(n);
		for(int i = 0; i < n; i++)
			if(xf[i] >= b){
				int index = i;
				for(int j = 0; j < n; j++) if(x[j] >= x[index] && xf[j] < b)
					cost[index]++;
			}
			else cost[i] = 1 << 30;
		//for(inti = 0; i  < n; i++) cost
		sort(cost.begin(), cost.end());
		
		int res = 0;
		bool sirve = true;
		for(int i = 0; i < k; i++)
			if(cost[i] == (1 << 30)) sirve = false;
			else res +=cost[i];
		
		if(sirve)
			cout << "Case #"<<tt<<": "<<res<<endl;
		else 
			cout << "Case #"<<tt<<": "<<"IMPOSSIBLE"<<endl;
	}
}
