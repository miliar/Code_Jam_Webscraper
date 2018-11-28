#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <sstream>

using namespace std;

int NA, NB, turn;

int readTime() {
	int H,M;
	char garb;
	cin >> H >> garb >> M;
	return H*60+M;
}

vector<pair<int,int> > go[2];
int done[2][220];

int main() {
	int cases;
	cin >> cases;

	string line;
	getline(cin,line);
	for(int t=0; t<cases; t++) {
		cin >> turn >> NA >> NB;
		//cout << "NA="<<NA<< " NB="<<NB<<endl;

		go[0].clear(); go[1].clear();
		for(int i=0; i<NA+NB; i++) {
			int t1 = readTime();
			int t2 = readTime();
			pair<int,int> p = make_pair(t1, t2);
			//cout << t1 << "->"<<t2<<endl;

			if (i < NA) go[0].push_back(p);
			else go[1].push_back(p);
		}

		for(int i=0; i<2; i++) sort(go[i].begin(), go[i].end());

		int ans[2] = {0,0};
		int pos[2] = {0,0};
		memset(done,0,sizeof(done));

		while(true) {
			for(int i=0; i<2; i++) {
				while(pos[i] < go[i].size() && done[i][pos[i]]) pos[i]++;
			}

			//cout << "POS: " << pos[0] << ","<<pos[1]<<endl;

			int id;
			if (pos[0] < go[0].size()) {
				if (pos[1] < go[1].size()) {
					id = go[0][pos[0]].first < go[1][pos[1]].first ? 0 : 1;
				}
				else id = 0;
			}
			else {
				if (pos[1] < go[1].size()) id = 1;
				else break;
			}

			//cout << "Train leaving from " << id << ", time " << pos[id]<<endl;
			ans[id]++;

			int tpos[2];
			tpos[0] = pos[0], tpos[1] = pos[1];

			while(tpos[id] < go[id].size()) {
				done[id][tpos[id]] = 1;

				int tm = go[id][tpos[id]].second + turn;
				id = 1-id;
				while(tpos[id] < go[id].size() && (done[id][tpos[id]] || go[id][tpos[id]].first < tm)) tpos[id]++;
			}
		}

		//cout << "Done1:"; for(int i=0; i<NA; i++) cout << done[0][i] << " "; cout<<endl;
		//cout << "Done2:"; for(int i=0; i<NB; i++) cout << done[1][i] << " "; cout<<endl;

		cout << "Case #" << (t+1) << ": " << ans[0] << " "<< ans[1]<<endl;

	}

}
