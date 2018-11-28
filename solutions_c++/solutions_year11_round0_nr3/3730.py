#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {

	int test;
	cin>>test;
	for(int k=1;k<=test;k++){
	int n;
	cin >> n;

	int ar[n+9];
	
	for(int i = 0; i < n; i++) {
		cin >> ar[i];
	}

	sort(ar, ar+n);
	int ret = 0;
	for(int i = 0; i < n; i++) {
		ret += ar[i];
	}
	bool r = false;
	for(int i = 0; i < n; i++) {
		//bool r = false
		int a = 0;
		for(int j = 0; j < n; j++) {
			if(i != j) {
			
				a = a^ar[j];
				
			}
		}

			if(a == ar[i]){ ret -= ar[i]; r = true;break;}
	}
	if(r == true)cout << "Case "<<"#"<<k<<": "<< ret << endl;
	if(r == false) cout << "Case "<<"#"<<k<<": "<< "NO" << endl;
	}
	return 0;
}

			 
			

		
