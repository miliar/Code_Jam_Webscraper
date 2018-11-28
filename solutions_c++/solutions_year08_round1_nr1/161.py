#include<iostream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cmath>

using namespace std;

typedef long long LL;

int main(){
	int T;
	cin >> T;
	for(int t=1; t<=T; t++){
		int n; 
		cin >> n;
		LL v1[1024], v2[1024];
		for(int i=0; i<n; i++)cin >> v1[i];
		for(int i=0; i<n; i++)cin >> v2[i];
		sort(v1,v1+n);
		sort(v2,v2+n);
		LL res=0;
		for(int i=0; i<n; i++)res+=v1[i]*v2[n-1-i];
		cout << "Case #" << t << ": " << res << "\n";
	}
}
