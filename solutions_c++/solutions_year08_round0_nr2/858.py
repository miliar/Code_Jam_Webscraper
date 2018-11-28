#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N[2];
int strains[2];
vector<int> trains[2];
vector<pair<int,pair<int,int> > > trips;

int toMinutes(string s) {
	return (10*(s[0]-'0')+s[1]-'0')*60+10*(s[3]-'0')+s[4]-'0';
}

int main() {
	int n;
	cin >> n;
	for(int t = 1; t <= n; ++t) {
		trips.clear();
		trains[0].clear();
		trains[1].clear();
		
		int T;
		cin >> T >> N[0] >> N[1];
		strains[0] = 0;
		strains[1] = 0;
		for(int i = 0; i < 2; ++i)
			for(int j = 0; j < N[i]; ++j) {
				string from,to;
				cin >> from >> to;
				int mfrom = toMinutes(from);
				int mto = toMinutes(to)+T;
				trips.push_back(pair<int,pair<int,int> >(mfrom,pair<int,int>(mto,i)));
			}

		sort(trips.begin(), trips.end());

		for(int i = 0; i < (int)trips.size(); ++i) {
			int d = trips[i].second.second;
			int from = trips[i].first;
			int to = trips[i].second.first;
			vector<int>::iterator j;
			for(j = trains[d].begin(); j != trains[d].end(); ++j)
				if(*j <= from)
					break;
			if(j == trains[d].end()) {
				strains[d]++;
			}
			else {
				trains[d].erase(j);
			}
			trains[(d+1)%2].push_back(to);
			sort(trains[(d+1)%2].begin(), trains[(d+1)%2].end());
		}

		cout << "Case #" << t << ": " << strains[0] << " " << strains[1] << endl;
	}
	return 0;
}
