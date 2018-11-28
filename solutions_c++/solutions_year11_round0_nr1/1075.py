#include <iostream>
#include <vector>

using namespace std;

int main () {
	int t, a,T=0;
	cin >> t;
	while(t--) {T++;
		int n;
		cin >> n;
		vector<int> orange,blue,all;
		for(int i = 0; i < n; i++) {
			char c; int j;
			cin >> c >> j;
			if(c=='O') orange.push_back(j);
			else blue.push_back(-j),j=-j;
			all.push_back(j);
		}
		int p1=0,p2=0,no = 0,nb = 0,na = 0,tt=0;
		while(na<all.size()) {
			bool pushed = false;
			if(no<orange.size() and p1 == orange[no] and all[na] == orange[no]) {
				no++;
				na++;
				pushed=true;
			} else if(no<orange.size()) if(p1<orange[no]) p1++; else if(p1>orange[no]) p1--;

			if(nb<blue.size() and p2 == blue[nb] and all[na] == blue[nb] and !pushed) {
				nb++;
				na++;
			} else if(nb<blue.size()) if(p2<blue[nb]) p2++; else if(p2>blue[nb]) p2--;
			tt++;
		}
		cout << "Case #" << T << ": "<<tt-1 <<endl;
	}
	
	return 0;
}
