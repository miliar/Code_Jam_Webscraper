#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<fstream>
using namespace std;

class firstGroup{
public:
	int cost;
	int nextGroup;
	firstGroup(){
		cost = 0;
		nextGroup = 0;
	}
};


int main(){

	ifstream ifs("C-small-attempt0.in");
	ofstream ofs("C-small.out");

	int TOTAL_CASE;
	ifs>>TOTAL_CASE;

	for(int CASE = 1 ; CASE <= TOTAL_CASE ; CASE++){

		int euros = 0;
		int R,k,N;
		ifs>>R>>k>>N;
		vector<int> g;
		g.resize(N);
		for(int i = 0 ; i < N ; i++) ifs>>g[i];

		vector<firstGroup> fg;
		fg.resize(N);

		for(int i = 0 ; i < N ; i++){
			int cost = 0;
			int cntGroup = 0;
			int idx = i;
			while(cost + g[idx] <= k){
				cntGroup++;
				cost += g[idx];
				if(++idx >= (int)g.size()) idx = 0;
				if(idx == i) break;
			}
			fg[i].cost = cost;
			fg[i].nextGroup = idx;
		}

		int i = 0;
		while(R--){
			euros += fg[i].cost;
			i = fg[i].nextGroup;
		}

		ofs<<"Case #"<<CASE<<": "<<euros<<endl;
	}
	ifs.close();
	ofs.close();
	return 0;
}