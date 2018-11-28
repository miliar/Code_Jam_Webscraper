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
	freopen("B-small.in","rt",stdin);
	freopen("B-small.out", "wt", stdout);
	int C;
	cin>>C;
	int N,M,T;
	for(int i = 1; i <= C; i++) {
		cin>>N>>M;
		vector<int> ret(N,-1);
		int malted = N + 1;
		vector<vector<int> > dem(M);
		for(int j = 0; j < M; j++) {
			dem[j].resize(N);
			for(int k = 0; k < N; k++) dem[j][k] = -1;
			cin>>T;
			for(int k = 0; k < T; k++) {
				int a,b;
				cin>>a>>b;
				dem[j][a-1] = b;
			}
		}
		vector<int> rtemp(N);
		for(int j = 0; j < 2<<N; j++) {
			int cnt = 0;
			for(int k = 0; k < N; k++) {
				if((2<<k) & j) {
					rtemp[k] = 1;
					cnt++;
				}
				else rtemp[k] = 0;
			}
			bool mark = true;
			for(int k = 0; k < M; k++) {
				bool over = false;
				for(int p = 0 ; p < N; p++) if(dem[k][p] == rtemp[p]) {
					over = true;
					break;
				}
				if(over == false) {
					mark = false;
					break;
				}
			}
			if(mark && cnt < malted) {
				malted = cnt;
				ret = rtemp;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(malted > N) cout<<"IMPOSSIBLE"<<endl;
		else {
			for(int j = 0; j < N; j++) cout<<ret[j]<<" ";
			cout<<endl;
		}
	}
	return 0;
}