#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

typedef pair<char, char> pchar;

int main() {
	int N; cin >> N;
	for (int I=0; I<N; ++I) {
		map<pchar, char> spell;
		map<char, int> contains;
		vector<pchar> opposed;
		vector<char> list;
		
		int n; cin >> n;
		char a,b,c;
		for(int i=0; i<n; ++i) {
			cin >> a >> b >> c;
			spell[make_pair(a,b)]=c;
			spell[make_pair(b,a)]=c;
		}
		
		cin >> n;
		for(int i=0; i<n; ++i) {
			cin >> a >> b;
			opposed.push_back(make_pair(a,b));
			opposed.push_back(make_pair(b,a));
		}
		
		cin >> n;
		for(int i=0; i<n; ++i) {
			cin >> a;
			list.push_back(a);
			contains[a]++;
			
			if (list.size()>=2) {
				pchar last=make_pair(*(list.end()-2), *(list.end()-1));
				if (spell.find(last)!=spell.end()) {
					contains[list.back()]--;
					list.pop_back();
					contains[list.back()]--;
					list.pop_back();
					list.push_back(spell[last]);
					contains[list.back()]++;
				}
				for(int j=0; j<opposed.size(); ++j) {
					if (contains[opposed[j].first] and contains[opposed[j].second]) {
						list.clear();
						contains.clear();
					}
				}
			} 
		}
		
		cout << "Case #" << I+1 << ": [";
		for (int i=0; i<list.size(); ++i) {
			cout << list[i] << ((i+1==list.size())?"":", ");
		}
		cout  << "]" << endl;
	}
}
