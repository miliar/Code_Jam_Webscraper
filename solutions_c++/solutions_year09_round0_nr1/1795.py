#include <iostream>
#include <vector>
#include <string>
using namespace std;

int doit( int L, string line, const vector<string> &dict ) {
	int i = 0;
	int len = 0;
	vector< vector<bool> > check( L, vector<bool>( 128, false ) );
	while(i<line.size()) {
		if( line[i] == '(' ) {
			++i;
			while(line[i]!=')') {
				check[len][ line[i++] ] = true;
			}
			++i;
			++len;
		}
		else {
			check[len++][line[i++]] = true;
		}
	}
	int ret = 0;
	for(int i=0;i<dict.size();++i) {
		bool ok = true;
		for(int j=0;j<dict[i].size();++j) {
			if( !check[j][dict[i][j]] ) { ok = false; break; }
		}
		if(ok) ret++;
	}
	return ret;
}

int main() {
	freopen("A-large.in","r",stdin);
	int L, D, N;
	cin >> L >> D >> N;
	vector<string> dict(D);
	for(int i=0;i<D;++i) cin >> dict[i];

	string line;
	for(int cc=1;cc<=N;++cc) {
		cin >> line;
		printf("Case #%d: %d\n", cc, doit( L, line, dict ));
	}
	fclose(stdin);
}
