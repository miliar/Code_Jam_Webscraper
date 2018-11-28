#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
typedef long long ll;
int c[1001];
int main(){
	int t,n;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++){
		int xsum = 0;
		scanf("%d", &n);
		for(int j = 0; j < n; j++){
			scanf("%d", &c[j]);
			xsum ^= c[j];
		}
		if(xsum != 0){
			cout << "Case #" << i << ": " << "NO";
			if(i < t)
				cout << endl;
		}
		else{
			sort(c,c+n);
			ll ans = 0;
			for(int j = 1; j < n; j++)
				ans += c[j];
			cout << "Case #" << i << ": " << ans;
			if(i < t)
				cout << endl;
		}

	}
	return 0;
}
