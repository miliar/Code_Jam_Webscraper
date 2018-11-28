//#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <fstream>
#include <map>
using namespace std;
ifstream cin("A-large.in",ifstream::in);
ofstream cout("A-large-2.out",ifstream::out);
struct wire {
	int Ai;
	int Bi;
};
int main() {
	int T;
	cin >> T;
	for (int i=1; i<=T; i++) {
		int N;
		cin >> N;
		vector<wire> wires;
		for (int j=0; j<N; j++) {
			int Ai,Bi;
			cin >> Ai >> Bi;
			wire x;
			x.Ai = Ai; x.Bi = Bi;
			wires.push_back(x);
		}
		int incount =0;
		for (int j=0; j<wires.size(); j++) {
			for (int k=0; k<wires.size(); k++) {
				if (j!=k) {
					if (((wires[j].Ai < wires[k].Ai) && (wires[j].Bi > wires[k].Bi))||((wires[j].Ai > wires[k].Ai) && (wires[j].Bi < wires[k].Bi)))
						incount++;
				}
			}
		}
		cout << "Case #"<<i<<": " << incount/2 << endl;
	}
}