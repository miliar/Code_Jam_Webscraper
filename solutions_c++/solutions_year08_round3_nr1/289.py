#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;

int c;

int main() {
	
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	scanf("%d", &c);

	for(int test=1; test<=c; test++) {
		long long ans=0;
		int P,K,L;
		cin>>P>>K>>L;
		vi v(L);
		for(int i=0;i<L;i++) cin>>v[i];
		sort(v.rbegin(),v.rend());
		int times=1;
		int ii=0;
		bool s=true;
		for(int i=0;i<L;i++){
			if(ii==K) {ii=0; times++;}
			if(times>P) {s=false; break;}
			ans+=v[i]*times;
			//cout<< v[i]*times<<endl;
			ii++;
			
		}
		if(s) cout<<"Case #"<<test<<": "<<ans<<endl;
		else printf("Case #%d: Impossible\n", test);
	}

	return 0;
}
