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

int j,k,n,t,i,r=0;
long long res=0;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin >> t;
	for (j=0;j<t;j++) {
		cin >> n >> k;
		res=1; long long bin=1;
		for (i=1;i<=n-1;i++) {
			bin*=2;
			res+=bin;
		}
		cout << "Case #" << j+1 << ": ";
		if ((k+1)%(res+1)==0) cout << "ON" << endl; else cout << "OFF" << endl;
	}
	return 0;
}
