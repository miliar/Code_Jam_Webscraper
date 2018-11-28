#include <iostream>1
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main(){
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	
	int T;
	cin>>T;
	for (int t = 0; t < T; ++t){
		long long n, k;
		cin>>n>>k;
		bool flag = true;
		for (int j = 0; j < n; ++j)
			if(!(k & (1LL<<j))){
				flag = false;
				break;
			}
		printf("Case #%d: %s\n", t+1, (flag ? "ON" : "OFF"));
	}
	
	return 0;
}