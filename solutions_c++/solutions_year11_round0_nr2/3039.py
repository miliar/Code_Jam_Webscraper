#include <cstdio>
#include <map>
#include <string>
using namespace std;


int t, n, C, D, N;
int main() {
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		char s[4];
		scanf("%d", &C);
		map<string, char> combine;
		map<char, char> oppose;
		for(int j = 0; j < C; ++j) {
			scanf("%s", s);
			combine[string(s, s + 2)] = s[2];
		}
		scanf("%d", &D);
		for(int j = 0; j < D; ++j) {
			scanf("%s", s);
			oppose[s[0]] = s[1];
			oppose[s[1]] = s[0];
		}
		scanf("%d", &N);
		char ss[N+1];
		scanf("%s", ss);
		string seq = ss;
		string out; out = seq[0];
		for(int j = 1; j < N; ++j) {
			string pc, rpc;
			if(out.size() >= 1) {
				pc += out[out.size() - 1];
				pc += seq[j];
				rpc += seq[j];
				rpc += out[out.size() - 1];
			}
			if(combine.find(pc) != combine.end()) {
				out[out.size() - 1] = combine[pc];
			} else if(combine.find(rpc) != combine.end()) {
				out[out.size() - 1] = combine[rpc];
			} else if(oppose.find(seq[j]) != oppose.end() 
			  && out.find(oppose[seq[j]]) != string::npos) {
				out.clear();
			} else {
				out += seq[j];
			}
		}
		
		string sOut = string("[");
		for(int j = 0; j < (int)out.size(); ++j) {
			sOut += out[j];
			if(j < (int)out.size() - 1)
				sOut += ", ";
		}
		sOut += "]";
		printf("Case #%d: %s\n", i, sOut.c_str());
	}

	return 0;
}
