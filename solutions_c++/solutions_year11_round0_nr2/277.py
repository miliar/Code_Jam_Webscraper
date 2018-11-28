#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	for(int tc=1; tc<=T; tc++) {
		int C;
		char combine[256][256];
		bzero(combine,sizeof(combine));
		char oppose[256][256];
		bzero(oppose,sizeof(oppose));
		cin >> C;
		for(int i=0; i<C; i++) {
			char a,b,c;
			cin >> a >> b >> c;
			combine[a][b]=combine[b][a]=c;
		}
		int D;
		cin >> D;
		for(int i=0; i<D; i++) {
			char a,b;
			cin >> a >> b;
			oppose[a][b]=oppose[b][a]=1;
		}
		int N;
		cin >> N;
		string ret;
		for(int i=0; i<N; i++) {
			char c;
			cin >> c;
			if(ret.size() && combine[ret[ret.size()-1]][c]) {
				ret[ret.size()-1] = combine[ret[ret.size()-1]][c];
			} else {
				ret += c;
			}
			for(int i=0; i<ret.size()-1; i++) {
				if(oppose[ret[i]][ret[ret.size()-1]]) {
					ret="";
					break;
				}
			}
			//cout << ret << endl;
		}
		cout << "Case #" << tc << ": [";
		for(int i=0; i<ret.size(); i++) {
			cout << (i?", ":"") << ret[i];
		}
		cout << "]" << endl;
	}
}
