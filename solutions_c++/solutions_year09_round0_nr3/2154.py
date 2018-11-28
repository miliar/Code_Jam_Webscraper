#include <iostream>

using namespace std;

int main(){		
	int N;
	cin >> N;
	string w = "welcome to code jam";
	string s;
	getline(cin,s);
	int a[20];
	for (int i = 1 ; i <= N ; i++){
		a[0] = 1;	
		for (int j = 1 ; j < 20; j++) a[j] = 0;
		s = "";
		getline(cin,s);
		//cout << s << endl;
		int ans = 0;				
		for (int j = 0 ; j < s.size() ; j++){
			for (int k = 19 ; k > 0 ; k--){
				if (s[j] == w[k-1]) a[k] = (a[k-1] + a[k]) % 10000;					
			}				
		} 		
		ans = a[19];		
		//cout << ans << endl;		
		if (ans >= 1000) cout << "Case #" << i << ": " << ans << endl;	
		else if (ans >= 100) cout << "Case #" << i << ": " << "0" << ans << endl; 
		else if (ans >= 10) cout << "Case #" << i << ": " << "00" << ans << endl; 
		else cout << "Case #" << i << ": " << "000" << ans << endl; 
	}
	return 0;
}