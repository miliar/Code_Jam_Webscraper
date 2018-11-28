#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;


int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t; cin >> t;
	for (int k=0;k<t;k++) {
		int n; cin >> n;
		vector<int> a (n);
		int res=0;
		for (int i=0;i<n;i++) {
			cin >> a[i]; res^=a[i];
		}
		if (res!=0) {
			printf("Case #%d: NO\n",k+1);
		} else {
			sort(a.begin(),a.end());
			int cur=0; int chk=0;
			for (int i=1;i<a.size();i++) {
				cur+=a[i];
				chk^=a[i];
			}
			printf("Case #%d: %d\n",k+1,cur);

		}
	}

	return 0;
}
