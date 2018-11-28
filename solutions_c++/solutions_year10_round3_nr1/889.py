#include <iostream>
#include <vector>

using namespace std;

int nbInter(int nbWires, vector< pair<int, int> > wires) {
	int nb = 0;
	for(int i=0 ; i<nbWires ; i++) {
		for(int j=0 ; j<i ; j++) {
			if((wires[i].first - wires[j].first) * (wires[i].second - wires[j].second) < 0)
				nb++;
		}
	}
	return nb;
}

int main() {
	int nbTests;
	cin >> nbTests;

	for(int t=1 ; t<=nbTests ; t++) {
		int nbWires;
		cin >> nbWires;
		vector< pair<int,int> > wires(nbWires, pair<int,int>(-1,-1));
		for(int i=0 ; i<nbWires ; i++) {
			cin >> wires[i].first >> wires[i].second;
		}

		cout << "Case #" << t << ": " << nbInter(nbWires, wires) << endl;
	}
}
