#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
map<int,bool> win[1000001];
map<int,bool>::iterator it;
bool go(int a,int b) {
	if(a > b) return go(b,a);
	if(b >= a+a) return 1;
	it = win[a].find(b);
	if(it != win[a].end()) return it->second;
	bool ret = !go(b-a,a);
	return (win[a][b] = ret);
}
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int a1,a2,b1,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		for(int a=1;a<=min(b2,a2);++a) win[a].clear();
		long long ans = 0;
		for(int a=a1;a<=a2;++a)
			for(int b=b1;b<=b2;++b)
				if(go(a,b)) ++ans;
		printf("Case #%d: ",cn);
		cout << ans << endl;
	}
}
