#include <iostream>
#include <cmath>
#include <cstdlib>
#include <functional>
#include <algorithm>
#include <string>
#include <vector>


using namespace std;

vector<string> M;

int main() {
	// INIT, IN
	ios_base::sync_with_stdio(0);
	int L,D,N;
	cin>>L>>D>>N;

	int d=D; 
	string s;
	while(d-->0) { cin>>s; M.push_back(s); }

	// CASES
	for(int icase=1; icase<=N; ++icase) {
		cin>>s;
		int len=s.length();
		char c=0;
		vector<int> czy(D,1);
		int odp = D;
		int tok = 0;

		for(int i=0; i<len; ++i) {
			c = s[i];
			char ok[256]={0};
			ok[c] = 1;
			if(c=='(') {
				while(i<len && s[i]!=')') {
					++i;
					c=s[i];
					ok[c]=1;
				}
			}
			for(d=D; d-->0;) {
				if(czy[d]) {
					if( !ok[ M[d][tok] ] ) {
						czy[d] = 0;
						--odp;
					}
				}
			}
			++tok;
		}
		cout<<"Case #"<<icase<<": "<<odp<<endl;

	}

	cin.get();
	return 0;
}

/*
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc

*/



