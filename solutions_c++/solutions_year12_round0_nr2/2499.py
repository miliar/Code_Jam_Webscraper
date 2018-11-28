#include <iostream>

using namespace std;

int sur[12][31]; //is it possible to make a surprinsing triple with best score >= p?

void pre(){
	for(int i = 10; i >= 2; i--){
		for(int j = 2; j <= 4 && 3*i-j >= 0; j++){
			sur[i][3*i-j] = true;
		}
		for(int j = 0; j <= 30; j++){
			sur[i][j] |= sur[i+1][j];
		}
	}	
}

int main(){
	ios::sync_with_stdio(false);
	pre();
	
	int t, n, s, p, ni, ans;
	
	cin >> t;
	for(int tc = 1; tc <= t; tc++){
		cin >> n >> s >> p; 
		
		cout << "Case #" << tc << ": ";
		
		ans = 0;
		for(int i = 0; i < n; i++){
			cin >> ni;
			
			if((ni+2)/3 >= p){
				ans++;
			}
			else if(sur[p][ni] && s){
				ans++;
				s--;
			}
		}
		
		cout << ans << "\n";
	}
	return 0;
}
