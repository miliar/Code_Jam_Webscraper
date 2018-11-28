#include <iostream>

#include <stdio.h>
#include <stdlib.h>

#include <string>
#include <vector>

using namespace std;

vector<string> vs;
vector<int> vi;

int main(void) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int L, D, N;
	cin >> L >> D >> N;

	vs.clear();
	for(int i=0;i<D;i++) {
		string s;
		cin >> s;
		vs.push_back(s);
	}

	
	int t=1;
	while(N--) {
		vi.clear();
		vi.resize(vs.size());

		string p; cin >> p;

		int len = p.length();
		int i=0;
		int k=0;
		while(i<len){
			string t;
			if(p[i]=='(') {
				i++;
				while(p[i]!=')') t.push_back(p[i++]);
				i++;
			}
			else {
				t.push_back(p[i++]);
			}

			for(int i=0;i<vs.size();i++) 
				for(int j=0;j<t.length();j++) if(vs[i][k] == t[j]) { vi[i]++; break; }
			k++;
		}

		int res=0;
		for(int i=0;i<vs.size();i++) if(vi[i]==k) res++;

		printf("Case #%d: %d\n", t++, res);
	}

	return 0;
}