#include <iostream>

using namespace std;

int main(){	
	
	int L,D,N;
	cin >> L >> D >> N;
	string s[D];
	string t[L];
	for (int i = 0 ; i < D; i++) cin >> s[i];
	string a;
	for (int i = 1 ; i <= N ; i++){	
		for (int j = 0 ; j < L ; j++) t[j] = "";
		int ans = 0;
		int l = 0;
		cin >> a;
		//cout << a << endl;
		for (int j = 0 ; j < a.size() ; j++){
			if (a[j] == '('){
				j++;
				//int c = 0;
				for ( ; a[j] != ')' ; j++){
					t[l] += a[j];
					//c++; 				
				}	
				//j++;								
			}
			else t[l] = a[j];
			l++;
		}	
		for (int j = 0 ; j < D ; j++){				
			int x = 0;
			for (int k = 0 ; k < L ; k++){
				for (int l = 0 ; l < t[k].size() ; l++){
					if (s[j][k] == t[k][l]) x++;
				}												
			}
			if (x == L) ans++;			
		}
		//for (int j = 0 ; j < L ; j++) cout << t[L] << endl;	
		//cout << t[0] << endl;				
		cout << "Case #" << i << ": " << ans << endl;		
	}
	return 0;
}