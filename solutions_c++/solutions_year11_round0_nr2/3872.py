#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int main(int n, char**p) {
	int T;
	cin>>T;
	for(int i=0; i<T; ++i) {
		int C;
		cin >>C;
		map<pair<char,char>, char> comb;
		for(int j=0; j<C; ++j) {
			string c;
			cin >> c;
			comb[make_pair(min(c[0],c[1]),
							max(c[0],c[1]))]=c[2];
		}
		vector<pair<char,char> > opp;
		int D;
		cin >>D;
		for(int j=0; j<D; ++j) {
			string c;
			cin >>c;
			opp.push_back(make_pair(c[0], c[1]));
		}
		int N;
		cin>>N;
		string s;
		cin >>s;
		string t;
		t += s[0];
		map<char, int> flg;
		flg[s[0]]++;
		for(int j=1; j<N;++j) {
			map<pair<char,char>, char>::iterator it
			 = comb.find(make_pair(min(*t.rbegin(),s[j]),max(*t.rbegin(),s[j])));
			if(it==comb.end()) {
				t += s[j];
				flg[s[j]]++;
			} else {
				flg[*t.rbegin()]--;
				*t.rbegin()=it->second;
			}
			for(int k=0; k<opp.size(); ++k) {
				if(flg[opp[k].first]>0&&flg[opp[k].second]>0) flg.clear(),t="";
			}
		}
		cout << "Case #" <<i+1 <<": [";
		if(t.length()>0) {
			cout << t[0];
			for(int j=1; j<t.length(); ++j) {
				cout <<", "<<t[j];
			}
		}
		cout <<"]"<<endl;
	}
}

				
