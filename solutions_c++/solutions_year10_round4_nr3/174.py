#include <set>
#include <iostream>
using namespace std;


int runTest() {
	int R;
	cin >> R;
	set<pair<int,int> > bs;
	set<pair<int,int> > newStates;
	set<pair<int,int> > changes;
	for (int i=0; i<R; i++) {
		int x1, x2, y1, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for (int y=y1; y<=y2; y++)
			for (int x=x1; x<=x2; x++) {
				bs.insert(make_pair(y,x));
				changes.insert(make_pair(y,x));
				changes.insert(make_pair(y+1,x));
				changes.insert(make_pair(y,x+1));
			}
	}
	int its = 0;
	while (!bs.empty()) {
		if (its%256==0)
			cerr << "\r" << bs.size(); cerr.flush();
		newStates.clear();
		for (set<pair<int,int> >::const_iterator it = changes.begin(); it!=changes.end(); it++) {
			if (bs.find(*it)==bs.end()) {
				if (bs.find(make_pair(it->first-1, it->second))!=bs.end()
					&& bs.find(make_pair(it->first, it->second-1))!=bs.end())
					newStates.insert(*it);
			} else {
				if (bs.find(make_pair(it->first-1, it->second))==bs.end()
					&& bs.find(make_pair(it->first, it->second-1))==bs.end())
					newStates.insert(*it);
			}
		}
		changes.clear();
		for (set<pair<int,int> >::const_iterator it = newStates.begin(); it!=newStates.end(); it++) {
			set<pair<int,int> >::iterator bs_it = bs.find(*it);
			if (bs_it==bs.end())
				bs.insert(*it);
			else
				bs.erase(bs_it);
			changes.insert(make_pair(it->first+1, it->second));
			changes.insert(make_pair(it->first, it->second+1));
		}
		its++;
	}
	cerr << endl;
	return its;
}

int main() {
//	freopen("in", "r", stdin);
	int T;
	cin >> T;
	for (int i=0; i<T; i++) {
		cerr << "test " << (i+1) << "/" << T << endl;
		cout << "Case #" << (i+1) << ": " << runTest() << endl;
	}
	return 0;
}
