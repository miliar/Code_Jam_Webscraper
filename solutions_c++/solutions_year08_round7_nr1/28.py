#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <map>
#include <set>

using namespace std;

int N, M;
string names[1001];
map<string, int> name_id;
int best[1001];
set<int> children[1001];
vector<string> c_s[1001];
int remaining[1001];

int calculate() {
	int j;
	for(int i=0; i<N; i++) {
		for(j=0; j<N; j++)
			if(remaining[j] == 0)
				break;
		best[j] = children[j].size() + 1;
		int mc = 99999;
		if(children[j].size() > 0) {
			for(set<int>::iterator iter = children[j].begin(); iter != children[j].end(); iter ++) {
				if(best[*iter] > best[j])
					best[j] = best[*iter];
				if(best[*iter] < mc)
					mc = best[*iter];
			}
			if(mc + children[j].size() - 1 > best[j])
				best[j] = mc + children[j].size() - 1;
		}
		for(int k=0; k<N; k++)
			if(children[k].find(j) != children[k].end())
				remaining[k] --;
		remaining[j] = -1;
	}
	cerr <<j <<endl;
	return best[j];
}

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >> N;
		memset(best, 0, sizeof(best));
		name_id.clear();
		for(int j=0; j<N; j++) {
			cin >>names[j];
			name_id.insert(make_pair(names[j], j));
			cin >>M;
			children[j].clear();
			remaining[j] = 0;
			c_s[j].clear();
			for(int k=0; k<M; k++) {
				string c;
				cin >>c;
				c_s[j].push_back(c);
			}
		}
		for(int j=0; j<N; j++) {
			for(int k=0; k<c_s[j].size(); k++) {
				map<string,int>::iterator iter = name_id.find(c_s[j].at(k));
				if(iter != name_id.end()) {
					children[j].insert(iter->second);
					remaining[j] ++;
				}
			}
		}
		cout <<"Case #" <<i+1 <<": " <<calculate() <<endl;
	}
	return 0;
}