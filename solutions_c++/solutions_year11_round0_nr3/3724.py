#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <map>

using namespace std;

int main() {

	int t;
	cin>>t;
	for(int k=1;k<=t;k++){
	int n, ret = 0;;
	cin >> n;

	int ar[n+2];
	
	for(int i = 0; i < n; i++) {
		cin >> ar[i];
		ret += ar[i];
	}

	sort(ar, ar+n);
	
	bool r = true;
	for(int i = 0; i < n; i++) {
		
		int a = 0;
		for(int j = 0; j < n; j++) {
			if(i != j) {
			
				a = a^ar[j];
				
			}
		}

			if(a == ar[i]){ ret -= ar[i]; r = false;break;}
	}
	if(r == false)cout << "Case "<<"#"<<k<<": "<< ret << endl;
		else { cout << "Case "<<"#"<<k<<": "<< "NO" << endl; }
	}
	return 0;
}

			 
			

		
