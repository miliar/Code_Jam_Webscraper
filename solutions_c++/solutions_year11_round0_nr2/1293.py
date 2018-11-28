#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MAX = 256;

int main(void) {
	int T; cin >> T;

	for(int t = 0; t < T; ++t) {
		char conv[MAX][MAX];
		for(int i=0;i<MAX;++i){
			for(int j=0;j<MAX;++j){
				conv[i][j]=0;
			}
		}
		char kwang[MAX][MAX];
		for(int i=0;i<MAX;++i){
			for(int j=0;j<MAX;++j){
				kwang[i][j]=0;
			}
		}

		int C; cin >> C;
		for(int i = 0; i < C; ++i) {
			string tmp; cin >> tmp;
			conv[tmp[0]][tmp[1]] = conv[tmp[1]][tmp[0]] = tmp[2];
		}

		int D; cin >> D;
		for(int i = 0; i < D; ++i) { 
			string tmp; cin >> tmp;
			kwang[tmp[0]][tmp[1]] = kwang[tmp[1]][tmp[0]] = 1;
		}

		int N; cin >> N;
		vector<char> soln;
		if(N) {
			string data; cin >> data;
			int n = (int)data.size();
			for(int i = 0; i < n; ++i) {
				char c = data[i];
				int z = soln.size();
				if(z >= 1) {
					if(conv[soln[z-1]][c]) { soln[z-1] = conv[soln[z-1]][c]; continue; }
					int clear = 0;
					for(int j = 0; j < z; ++j) {
						if(kwang[soln[j]][c]) { clear=1; break; }
					}
					if(clear) {
						soln.clear(); continue;
					}
				}
				soln.push_back(c);
			}
		}

		cout << "Case #" << (t+1) << ": [";
		for(vector<char>::iterator i=soln.begin(); i != soln.end(); ++i) {
			if(i != soln.begin()) { cout << ", "; }
			cout << *i;
		}
		cout << "]" << endl;
	}
}
