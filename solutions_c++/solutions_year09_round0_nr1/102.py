#include <iostream>
#include <string>
#include <vector>
#include <tr1/unordered_set>
#include <cassert>

using namespace std;

int L,D,N;

typedef tr1::unordered_set<char> CSet;

int main()
{
	cin>>L>>D>>N;
	vector<string> words;
	string s;
	for(int i=0; i<D; ++i) {
		cin>>s;
		words.push_back(s);
	}
	for(int i=0; i<N; ++i) {
		cin>>s;
		vector<CSet> sets;
		for(int j=0; j<s.size(); ++j) {
			CSet set;
			if (s[j]=='(') {
				while(s[++j]!=')') set.insert(s[j]);
			} else set.insert(s[j]);
			sets.push_back(set);
		}

		int r=0;
		for(unsigned j=0; j<words.size(); ++j) {
			bool ok=1;
			for(int k=0; k<L; ++k) {
				if (!sets[k].count(words[j][k])) {
					ok=0;
					break;
				}
			}
			if (ok) ++r;
		}
		cout<<"Case #"<<i+1<<": "<<r<<'\n';
	}
}
