#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	int T,t;
	long long m,X,Y,Z;
	long long a[1002];
	int i,j,n,cnt;

	cin >> t;
	for(T=1;t--;T++) {
		vector<long long> v;

		cin >> n >> m >> X >> Y >> Z;
		for(i=0;i<m;i++) cin >> a[i];
		for(i=0;i<=n-1;i++) {
			v.push_back(a[i%m]);
			a[i%m]=(X*a[i%m]+Y*(i+1))%Z;
		}

		long long res[1002]={0,};
		long long ret;
		for(i=0;i<n;i++) res[i]=1;
		for(i=n-1;i>=0;i--) {
			for(j=i+1;j<n;j++) {
				if(v[i]<v[j]) res[i]= (res[i]+res[j])%1000000007LL;
			}
		}

		ret=0;
		for(i=0;i<n;i++) ret=(ret+res[i])%1000000007LL;
		cout << "Case #" << T << ": " << ret << endl;
		//printf("Case #%d: %lld\n", T,ret);
	}

	return 0;
}