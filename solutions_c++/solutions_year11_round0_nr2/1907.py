#include <iostream>
#include <string>
#include <map>
using namespace std;

typedef pair<char, char> CP;
int main() {
	int T, C, D, N;
	cin >> T;
	for(int t=1; t<=T; t++) {
		map<CP, char> Cs;
		cin >> C;
		for(int i=0; i<C; i++) {
			char a, b, c;
			cin >> a >> b >> c;
			if (a > b) swap(a, b);
			Cs[make_pair(a, b)] = c;
		}

		int Ds[91][91] = {};
		cin >> D;
		for(int i=0; i<D; i++) {
			char a, b;
			cin >> a >> b;
			Ds[int(a)][int(b)] = Ds[int(b)][int(a)] = 1;
		}

		string buf;
		cin >> N;
		while(N-- > 0) {
			char c;
			cin >> c;
			if (buf.empty()) {
				buf += c;
				continue;
			}
			CP a = make_pair(c, buf[buf.length() - 1]);
			if (a.first > a.second) swap(a.first, a.second);
			if (Cs.find(a) != Cs.end())
				buf[buf.length() - 1] = Cs[a];
			else
				buf += c;
			for(int i=0; i+1<buf.length(); i++)
				if (Ds[int(buf[i])][int(buf[buf.length()-1])])
					buf.clear();
		}
		cout << "Case #" << t << ": [";
		for(int i=0; i+1<buf.length(); i++)
			cout << buf[i] << ", ";
		if (!buf.empty()) cout << buf[buf.length()-1];
		cout << "]" << endl;
	}
	return 0;
}

