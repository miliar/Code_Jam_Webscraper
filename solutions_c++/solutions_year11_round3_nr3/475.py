#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;

void solve(ll tc){
	int n, l, h;
	cin >> n >> l >> h;
	vector<int> f;
	for(int i = 0; i < n; i++){
		int fi;
		cin >> fi;
		f.push_back(fi);
	}
	for(int i = l; i <= h; i++){
		bool harmony = true;
		for(int j = 0; j < n && harmony; j++){
			if(i != f[j] && f[j] % i && i % f[j]){
				harmony = false;
			}
		}
		if(harmony){
			cout << "Case #" << tc << ": " << i << endl;
			return;
		}
	}
	cout << "Case #" << tc << ": " << "NO" << endl;
}

int main(){
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		solve(i+1);
	}
	return 0;
}
