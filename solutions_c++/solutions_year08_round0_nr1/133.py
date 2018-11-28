#include <iostream>
#include <set>
using namespace std;

int main() {
	string x;
	int N;
	cin >> N;
	for (int z=1;z<=N;++z) {
		int S;
		cin >> S; getline(cin,x);
		for (int i=0;i<S;++i) getline(cin,x);
		int Q;
		cin >> Q; getline(cin,x);
		int ans=0;
		set<string> s;
		while (Q-- > 0) {
			getline(cin,x);
			s.insert(x);
			if (s.size()==S) ++ans, s.clear(), s.insert(x);
		}
		if (s.size()>0) ++ans;
		if (ans>0) --ans;
		cout << "Case #" << z << ": " << ans << endl;
	}
}
