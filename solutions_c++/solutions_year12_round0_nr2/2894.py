#include <iostream>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		int n, s, p, v[100], ans=0, cnt_s=0;
		cin >> n >> s >> p;
		for(int i=0;i<n;i++){
			cin >> v[i];
			if(v[i] / 3 >= p || v[i] >= 1 && ((v[i] - 1) / 3) + 1 >= p) ans++;
			else if(cnt_s < s && v[i] >= 2 && ((v[i] - 2) / 3) + 2 >= p){
				ans++;
				cnt_s++;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}