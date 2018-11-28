#include<iostream>
#include<string>
#include<cstring>
using namespace std;

int L, D, N;
string dict[6000];
char exist[32][256];

int main() {
    cin >> L >> D >> N;
    for(int d = 0; d < D; ++d) {
	cin >> dict[d];
    }
    for(int i = 0; i < N; ++i) {
	string line;
	cin >> line;
	memset(exist, 0, sizeof(exist));
	int at = 0;
	for(int s = 0; s < line.size(); ++s) {
	    if(line[s] == '(') {
		++s;
		while(line[s] != ')') {
		    exist[at][line[s]] = 1;
		    ++s;
		}
	    } else {
		exist[at][line[s]] = 1;
	    }
	    ++at;
	}
	int ans = 0;
	for(int d = 0; d < D; ++d) {
	    bool okay = true;
	    for(int l = 0; l < L; ++l) {
		if(!exist[l][dict[d][l]]) {
		    okay = false;
		    break;
		}
	    }
	    if(okay) ans++;
	}
	cout << "Case #" << (i+1) << ": " << ans << endl;
    }
    return 0;
}
