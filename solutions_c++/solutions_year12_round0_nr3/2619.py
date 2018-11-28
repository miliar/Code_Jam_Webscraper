#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>

using namespace std;

#define all(x) x.begin(),x.end()
#define bits(x) __builtin_popcount(x)
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)

int main() {
	int n,a,b;
	int pot;
	
	cin>>n;
	for (int i = 0; i < n; i++) {
		pot=1;
		cin>>a>>b;
		int tmp=a;
		
		while (tmp>=10) {
			tmp/=10;
			pot*=10;
		}
		
		int ans=0;
		for (int j=a;j<=b;j++) {
			int next = j;
			while ((next=(next/10+(next%10)*pot)) != j) {
				if (j<next && next<=b) ans++;
			}
		}
		
		cout << "Case #" << (i+1) << ": " << ans << endl; 
	}
	return 0;
}
