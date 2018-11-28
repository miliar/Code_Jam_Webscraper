#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;

vector <string> dic;
int L;

bool count(const string &sub, const vector <vector <char> > &tries) {
	bool rv=true;
	for(int l=0; l<L; l++){
		if (find(tries[l].begin(), tries[l].end(), sub[l]) ==
			tries[l].end()) {
			rv=false;
			break;
		}
	}
	return rv;
}

main(){
	int D,N;
	cin >> L >> D >> N;
	vector < map<char, bool> > pos;
	for(int l=0; l<L; l++) {
		map<char, bool> m;
		for(char c='a'; c<='z'; c++) {
			m[c] = false;
		}
		pos.push_back(m);
	}
	for(int d=0; d<D; d++) {
		string x;
		cin >> x;
		dic.push_back(x);
		for(int l=0; l<L; l++){
			pos[l][x[l]]=true;
		}
	}
	for(int n=0; n<N; n++) {
		vector <vector <char> > tries;
		string s;
		cin >> s;
		int p=0;
		int sum=0;
		for(int l=0; l<L; l++){
			vector <char> t;
			if (s[p]!='(') {
				t.push_back(s[p]);
				tries.push_back(t);
				p++;
				continue;
			}
			p++;
			while(s[p]!=')') {
				if (pos[l][s[p]]) {
					t.push_back(s[p]);
				}
				p++;
			}
			p++;
			if (t.size() == 0) sum=-1;
			tries.push_back(t);
		}
		if (sum == -1){ 
			cout << "Case #" << n+1 <<": 0" << endl;
			continue;
		}
		sum = 0;
		for(int d=0; d< D; d++){
			if(count(dic[d], tries)) sum++;
		}
		cout << "Case #" << n+1 << ": " << sum << endl;
	}
}
		
