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
	int n,N,S,p;
	
	cin>>n;
	
	for (int i = 0; i < n; i++) {
		cin>>N>>S>>p;
		
		int ans=0,a;
		for (int j=0;j<N;j++) {
			cin>>a;
			
			if ((a+2)/3>=p) ans++;
			else {
				if (S>0 && p+2*max(0,p-2)<=a) {
					S--;
					ans++;
				}
			}
		}
		
		cout << "Case #" << (i+1) << ": " << ans << endl; 
	}
	return 0;
}
