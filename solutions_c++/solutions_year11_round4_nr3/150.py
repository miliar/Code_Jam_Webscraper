#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <vector>

using namespace std;

int primechk[1000003];
vector<int> plist;
int main(){
	int T;
	int testcase = 0;
	scanf("%d",&T);
	for(int i = 2;i <= 1000000;i ++) {
		if(primechk[i])continue;
		plist.push_back(i);
		for(int j = i *2 ;j <= 1000000;j += i ){
			primechk[j] = 2;
		}
	}
	while(T--> 0 ){
		++testcase;
		long long n;
		scanf("%lld",&n);
		long long ans = 0;
		long long cnt1 = 0, cnt2 = 0;

		for(int i = 0; i <plist.size();i ++){
			long long tmp = n;
			if(tmp < plist[i]) break;
			while(tmp /= plist[i]) ans ++;
			ans --;
		}
		if(n != 1) {
			ans ++;
		}

		printf("Case #%d: %lld\n",testcase,ans);
	}
	return 0;
}
