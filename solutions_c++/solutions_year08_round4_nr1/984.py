#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int main() {
	freopen("A-small.in","rt",stdin);
	freopen("A-small.out", "wt", stdout);
	int N,M,V;
	cin>>N;
	for(int i = 1; i <= N; i++) {
		cin>>M>>V;
		vector<bool> val(M+1);
		int m = (M-1) / 2;
		vector<bool> isand(m+1);
		vector<bool> changable(m+1);
		for(int j = 1; j <= m; j++) {
			bool t;
			cin>>t;
			isand[j] = t;
			cin>>t;
			changable[j] = t;
		}
		for(int j = m + 1; j <= M; j ++) {
			bool t;
			cin>>t;
			val[j] = t;
		}
		int res = 10000;
		for(int j = 0; j < 1<<m; j++) {
			vector<bool> temp = val;
			int cnt = 0;
			for(int k = m; k >= 1; k--) {
				if((bool)(1<<(k-1) & j) != isand[k] && changable[k] == false) goto mark;
				if((bool)(1<<(k-1) & j) != isand[k]) cnt ++;
				if( (1<<(k-1) & j) ) temp[k] = temp[k * 2] & temp[k * 2 + 1];
				else	temp[k] = temp[k * 2] | temp[k * 2 + 1];
			}
			if(temp[1] == (bool)V && cnt < res) res = cnt;
mark:;
		}
		cout<<"Case #"<<i<<": ";
		if(res < 10000) cout<<res<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}