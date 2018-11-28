#include <sstream>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <fstream>
using namespace std;

template<class Ty,class Tx> Ty to(Tx x){Ty y;stringstream ss("");ss<<x;ss.seekg(0);ss>>y;return y;};

int ttoi(string time) {
	return (time[0] - '0') * 600 + (time[1] - '0') * 60 + (time[3] - '0') * 10 + time[4] - '0';
};

int main(int argc, char* argv[])
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int mx = 200;  
	char line[200];
	fin.getline(line, mx);
	int noc = to<int>(string(line));
	for(int i = 1; i <= noc; i ++) {
		int ta;
		fin>>ta;
		int na, nb;
		fin>>na>>nb;
		vector<pair<int, int> > nas;
		vector<pair<int, int> > nbs;
		int numa = 0;
		int numb = 0;
		for(int k = 0; k < na + nb; k ++) {
			string st, at;
			fin>>st>>at;
			if(k < na) {
				nas.push_back(make_pair(ttoi(st), ttoi(at)));
			} else {
				nbs.push_back(make_pair(ttoi(st), ttoi(at)));
			}
		}
		sort(nas.begin(), nas.end());
		sort(nbs.begin(), nbs.end());
		while((nas.size() > 0) && (nbs.size() > 0)) {
			if(nas[0].first < nbs[0].first) {
				numa ++;
				int newt = nas[0].first;
				int pos = 0;
				bool bl = false;
				while(!bl) {
					if(pos == 0) {
						for(int j = 0; j < nas.size(); j ++) {
							if(nas[j].first >= newt) {
								newt = nas[j].second + ta;
								nas.erase(nas.begin() + j);
								pos = 1;
								break;
							}
						}
						if(pos == 0) {bl = true;}
					} else {
						for(int j = 0; j < nbs.size(); j ++) {
							if(nbs[j].first >= newt) {
								newt = nbs[j].second + ta;
								nbs.erase(nbs.begin() + j);
								pos = 0;
								break;
							}
						}
						if(pos == 1) {bl = true;}
					}
				}
			} else {
				numb ++;
				int newt = nbs[0].first;
				int pos = 1;
				bool bl = false;
				while(!bl) {
					if(pos == 0) {
						for(int j = 0; j < nas.size(); j ++) {
							if(nas[j].first >= newt) {
								newt = nas[j].second + ta;
								nas.erase(nas.begin() + j);
								pos = 1;
								break;
							}
						}
						if(pos == 0) {bl = true;}
					} else {
						for(int j = 0; j < nbs.size(); j ++) {
							if(nbs[j].first >= newt) {
								newt = nbs[j].second + ta;
								nbs.erase(nbs.begin() + j);
								pos = 0;
								break;
							}
						}
						if(pos == 1) {bl = true;}
					}
				}
			}
		}
		numa += nas.size();
		numb += nbs.size();
		fout<<"Case #"<<i<<": "<<numa<<' '<<numb<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

