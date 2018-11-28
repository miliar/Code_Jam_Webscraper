#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

int d[10010];
int l[10010];
int range[10010];

int n, D;

string solve(){
	memset(range, 0, sizeof(range));
	range[0] = d[0];
	
	for(int i = 0; i < n; i++){
		if(d[i] + range[i] >= D) return "YES";
		
		for(int j = i+1; j < n && d[j] <= d[i] + range[i]; j++){
			range[j] = max(range[j], min(l[j], d[j]-d[i]));
		}
	}
	return "NO";
}

int main(){
	int t;
	
	cin >> t;
	for(int tc = 1; tc <= t; tc++){
		cin >> n;
		for(int i = 0; i < n; i++){
			cin >> d[i] >> l[i];
		}
		cin >> D;
		
		cout << "Case #" << tc << ": " << solve() << "\n";
	}
}

