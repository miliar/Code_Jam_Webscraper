#include<iostream>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<vector>
#include<string>
#include<math.h>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; cin>>T;
	for (int t=1; t<=T; t++) {
		int N,L,H; cin>>N>>L>>H;
		vector<int> v;
		for (int i=0; i<N; i++) {
			int curr; cin>>curr; v.push_back(curr);
		}


		int ans=-1;
		for (int i=L; i<=H; i++) {
			bool flag=true;
			for (int j=0; j<N; j++) {
				int curr=v[j];
				if(!(i%curr==0 || curr%i==0)) { flag=false; break; }
			}
			if(flag) { ans=i; break; }
		}

		cout << "Case #" << t << ": ";
		if(ans==-1) cout << "NO";
		else cout << ans;
		cout << endl;
	}

	return 0;
}
