#include<iostream>
#include <string.h>
using namespace std; 

int main(){
	freopen("C:\\Documents and Settings\\mqiao\\My Documents\\Downloads\\B-large.in", "r", stdin); 
	freopen("C:\\Documents and Settings\\mqiao\\My Documents\\Downloads\\aout.txt","w",stdout); 
	int t;
	int n, s, targetS, p; 
	int ans, a;
	cin >> t; 
	int cret1, cret2; 
	for (int i = 0; i < t; i++) {
		cout <<"Case #"<<i+1<<": ";
		cin >> n >> targetS >> p; 
		cret1 = p * 3 - 2; 
		cret2 = p * 3 - 4; 
		if (cret1 < 0) cret1 = 0;
		if (cret2 < 0) cret2 = 2; 
		ans = s = 0; 
		for (int j = 0; j < n; j++) {
			cin >> a; 
			if (a >= cret1) ans ++;
			else if (a >= cret2) s ++;
		}
		if (s > targetS) s = targetS;
		ans += s; 
		cout << ans << endl; 
	}
	fclose(stdin); 
	//fclose(stdout); 
}