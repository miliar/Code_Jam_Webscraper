#include <iostream>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++){
		int n,s,p,t,ans;
		cin >> n >> s >> p;
		ans = 0;
		for(int j = 0; j < n; j++){
			cin >> t;
			if(t >= 3*p-2) ans++;
			else if(p-2 > 0 && s && t >= 3*p-4){
				ans++;
				s--;
			}
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
}
