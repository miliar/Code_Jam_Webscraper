#include <iostream>
#include <string>
#include <fstream>

#include <vector>
#include <map>

#include <algorithm>

using namespace std;

template<typename T>
void mySwap(T& t1, T& t2) {
	T tmp = t2;
	t2 = t1;
	t1 = tmp;
}

struct wire {
	float y1, y2;
	
	wire() : y1(0), y2(0) {}
};


vector<wire> wires;

int doIntersect(wire w) {
	if(wires.size() == 0) return 0;
	
	int inter = 0;
	for(int i=0; i<wires.size(); ++i) {
		if((w.y1 > wires[i].y1 && w.y2 < wires[i].y2) || (w.y1 < wires[i].y1 && w.y2 > wires[i].y2)) {
			++inter;
		}
	}
	return inter;
}

int main() {
	ifstream in("A-large.in");
	ofstream out("large.out");
	
	int c;
	in>>c;
	
	for(int i=0; i<c; ++i) {
		int n;
		in>>n;
		
		int count = 0;
		wires.clear();
		for(int j=0; j<n; ++j) {
			wire tmp;
			in>>tmp.y1>>tmp.y2;
			
			count += doIntersect(tmp);
		
			wires.push_back(tmp);
		}
		
		out<<"Case #"<<i+1<<": "<<count<<endl;
	}
}