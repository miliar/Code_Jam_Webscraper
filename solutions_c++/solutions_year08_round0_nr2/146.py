#include <iostream>
#include <set>
#include <map>
#include <utility>
using namespace std;

int main() {
	int N;
	cin >> N;
	
	for(int i = 1; i <= N; ++i) {
		cout << "Case #" << i << ": ";
				
		int T;
		cin >> T;
		
		int NA, NB;
		cin >> NA >> NB;
		
		multimap<int, int> nas;
		for(int na = 0; na != NA; ++na) {
			int h, m;
			char ch;
			cin >> h >> ch >> m;
			int d = h*60+m;
			cin >> h >> ch >> m;
			int a = h*60+m;
			nas.insert(make_pair(d, a));
		}
		multimap<int, int> nbs;
		for(int nb = 0; nb != NB; ++nb) {
			int h, m;
			char ch;
			cin >> h >> ch >> m;
			int d = h*60+m;
			cin >> h >> ch >> m;
			int a = h*60+m;
			nbs.insert(make_pair(d, a));
		}
		multiset<int, greater<int> > ava, avb;
		int A = 0, B = 0;
		while(!(nas.empty() && nbs.empty())) {
			if(!nas.empty() && (nbs.empty() || nas.begin()->first <= nbs.begin()->first)) {
				int d = nas.begin()->first, a = nas.begin()->second;
				nas.erase(nas.begin());
				if(ava.lower_bound(d) != ava.end()) {
					ava.erase(ava.lower_bound(d));
					avb.insert(a + T);
				}
				else {
					avb.insert(a + T);
					++A;
				}
			}
			else {
				int d = nbs.begin()->first, a = nbs.begin()->second;
				nbs.erase(nbs.begin());
				if(avb.lower_bound(d) != avb.end()) {
					avb.erase(avb.lower_bound(d));
					ava.insert(a + T);
				}
				else {
					ava.insert(a + T);
					++B;
				}
			}
		}
		cout << A << " " << B << endl;
	}
}
