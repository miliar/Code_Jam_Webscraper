#include <cstdio>
#include <iostream>
#include <string>
#include <set>
using namespace std;

int N,S,Q;
string names[100];
string query[1000];

void pegalinha(string& s) {
	getline(cin,s);
}

int main(void) {
	cin >> N;
	for(int T=1;T<=N;T++) {
		printf("Case #%d: ",T);
		cin >> S;
		pegalinha(names[0]);
		set<string> can;
		for(int i=0;i<S;i++) {
			pegalinha(names[i]);
			can.insert(names[i]);
		}
		cin >> Q;
		pegalinha(query[0]);
		int ans=0;

		for(int i=0;i<Q;i++) {
			pegalinha(query[i]);
			if(can.size() == 1 and query[i]==*can.begin()) {
				for(int j=0;j<S;j++)
					can.insert(names[j]);
				can.erase(query[i]);
				ans++;
			} else {
				if(can.find(query[i]) != can.end())
					can.erase(query[i]);
			}
		}
		cout << ans << endl;
	}
	return 0;
}
