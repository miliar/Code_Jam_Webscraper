#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

class Wire{
public:
	int spt;
	int ept;
	Wire(int s,int e){
		spt = s;
		ept = e;
	}
};

int main(){
	ifstream ifs;
	ofstream ofs;

	ifs.open("A-large.in");
	ofs.open("A-large.out");


	int T;
	ifs>>T;

	for(int caseN = 1 ; caseN <= T ; caseN++){

		int N;
		ifs>>N;

		vector<Wire> wires;

		for(int i = 0 ; i < N ; i++){
			int spt,ept;
			ifs>>spt>>ept;
			wires.push_back(Wire(spt,ept));
		}
		int result = 0;
		for(int i = 0 ; i < N-1 ; i++){
			for(int j = i+1 ; j < N ; j++){
				if((wires[i].spt > wires[j].spt && wires[i].ept < wires[j].ept)
					||(wires[i].spt < wires[j].spt && wires[i].ept > wires[j].ept))
					result++;
			}
		}
		ofs<<"Case #"<<caseN<<": "<<result<<endl;
	}

	ifs.close();
	ofs.close();

	return 0;
}