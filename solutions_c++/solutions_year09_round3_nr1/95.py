#include <iostream>
#include <string>
#include <map>
using namespace std;

typedef map<char,int> M;

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;++t) {
		string s;
		cin>>s;
		M m;
		int next=1;
		for (int i=0;i<s.size();++i) {
			M::iterator it = m.find(s[i]);
			if (it==m.end()) {
				m[s[i]]=next;
				if (next==1) next=0;
				else if (next==0) next=2;
				else next++;
			}
		}
		long long ret=0;
		int base=next;
		if (next==0) base=2;	
		for (int i=0;i<s.size();++i) {
			ret*=base;
			ret+=m[s[i]];
		}
		cout << "Case #" << t << ": " << ret << endl;
	}
}
