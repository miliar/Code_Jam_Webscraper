#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

int p;
int mis[1100];
int mk[2200];

void dfs(int c) {
	if(c >= (1<<p)) {
		mis[c - (1<<p)]--;
		mis[c - (1<<p)] = max(mis[c - (1<<p)],0);
		return ;
	}
	dfs(c * 2);
	dfs(c * 2 + 1);
}
	
int solve() {
	memset(mk,0,sizeof(mk));
	int ans = 0;
	while(true) {
		int flag = 0;
		for(int i = 0;i < (1<<p);++i) {
			if(mis[i] > 0) {
				flag = 1;
				break;
			}
		}
		if(!flag) return ans;
		int ret = 0, ind = 0;
		for(int i = 0;i < (1<<p);++i) {
			if(mis[i] > ret) {
				ret = mis[i];
				ind = i;
			}
		}
		ind += (1<<p);
		vector<int>ok;
		while(ind) {
			ok.push_back(ind/2);
			ind /= 2;
		}
		for(int i = ok.size() - 1;i >= 0;--i) {
			if(ok[i] == 0)continue;
			if(!mk[ok[i]]) {
				mk[ok[i]] = 1;
				dfs(ok[i]);
				break;
			}
		}
		ans++;
	}
	
	return 0;
}
				
int main() {
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	
	int T,cas = 1;
	scanf("%d",&T);
	while(T--) {
		scanf("%d",&p);
		for(int i = 0;i < (1<<p);++i) {
			scanf("%d",&mis[i]);
			mis[i] = p - mis[i];
			mis[i] = max(mis[i],0);
		}
		int price;
		for(int i = 0;i < p;++i) {
			for(int j = 0;j < (1<<(p-i-1));++j) {
				scanf("%d",&price);
			}
		}
		printf("Case #%d: %d\n",cas++, solve() * price);
	}
//	while(1);
	return 0;
}
