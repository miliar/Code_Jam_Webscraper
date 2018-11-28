#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> recycle[2000010];

void pre(){
	int pot = 10, mult = 1, step = 0, pairs = 0;
	
	for(int i = 10; i <= 2000000; i++){
		if(i == pot){
			pot *= 10;
			mult *= 10;
			step++;
		}
		
		
		int n = i;
		for(int j = 0; j < step; j++){
			n = n/10 + mult*(n%10); //rotate
			
			if(n <= 2000000 && n > i){
				recycle[i].push_back(n);
			}
		}
		
		sort(recycle[i].begin(), recycle[i].end());
		
		recycle[i].resize( unique(recycle[i].begin(), recycle[i].end()) - recycle[i].begin() );
		
		pairs += recycle[i].size();
	}
}

int main(){
	ios::sync_with_stdio(false);
	pre();
	
	int t, a, b, ans;
	
	cin >> t;
	for(int tc = 1; tc <= t; tc++){
		cin >> a >> b;
		
		ans = 0;
		for(int i = a; i <= b; i++){
			ans += upper_bound(recycle[i].begin(), recycle[i].end(), b) - 
				   		lower_bound(recycle[i].begin(), recycle[i].end(), a);
		}
		
		cout << "Case #" << tc << ": " << ans << "\n";
	}
	
	return 0;
}
