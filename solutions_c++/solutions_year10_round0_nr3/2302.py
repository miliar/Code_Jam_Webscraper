#include <iostream>
#include <list>
using namespace std;

int money(int nbRides, int capacite, int nbGroups, list<int>& groups) {
	int euros = 0;
	list<int>::iterator pt = groups.begin();

	for(int i=0 ; i<nbRides ; i++) {
		pt = groups.begin();
		int placesRes = capacite;
		int groupsin = 0;
		while((*pt) <= placesRes && groupsin < nbGroups) {
			int nbPers = (*pt);
			placesRes -= nbPers;
			euros += nbPers;
			groupsin++;

			pt++;
			groups.pop_front();
			groups.push_back(nbPers);
		}
	}

	return euros;
}

int main() {
	int nbTests;
	cin >> nbTests;

	for(int i=1 ; i<=nbTests ; i++) {
		int r, k, n;
		cin >> r >> k >> n;
		list<int> g;
		for(int j=0 ; j<n ; j++) {
			int gi;
			cin >> gi;
			g.push_back(gi);
		}
		cout << "Case #" << i << ": " << money(r, k, n, g) << endl;
	}
}
