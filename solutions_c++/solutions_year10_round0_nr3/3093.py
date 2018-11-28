#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main() {
	int t;
	cin >> t;
	for(int o=1;o<=t;o++) {
		int r, k, n;
		cin >> r >> k >> n;
		vector<int> v;
		for(int i=0;i<n;i++) {
			int yyyy;
			cin >> yyyy;
			v.push_back(yyyy);

		}
		int i = 0;
		int ans = 0;
		int len = 0;
		for(int j=1;j<=r;j++) {
			len = 0;
			int sum = 0;
			while(1 ) {
				if(sum+v[i]>k) break;
				sum = sum + v[i];
				i++;
				len++;
				if(i==n) i = 0;
				if(len==n) break;
			}
			ans += sum;
		}
		printf("Case #%d: %d\n", o, ans);	
			
	}
}
