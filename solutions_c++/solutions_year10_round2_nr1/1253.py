#include <iostream>
#include <string>

#include <vector>

#include <fstream>

using namespace std;

vector<string> existingPaths;

bool stringEqual(const string& s1, const string& s2) {	

	for(int i=0; i<s2.size(); ++i) {
		if(s1[i] != s2[i]) return false;
	}
	if(s1.size() == s2.size()) return true;
	if(s1.size() > s2.size()) {
		if(s1[s2.size()] == '/') return true;
	}
	return false;
}


int createPath(string& path, int cost) {
	if(existingPaths.size() != 0) {
		for(int i=existingPaths.size()-1; i>=0; --i) {
			if(path.size() <= existingPaths[i].size()) {
				if(stringEqual(existingPaths[i], path)) {
					return cost;
				}
			}
		}
	} else {
		int i = 0;
		int t = 0;
		while(i<path.size()) {
			if(path[i] == '/') ++t;
			++i;
		}
		return t;
	}
	
	if(path.find('/') != string::npos) {
		path.erase(path.rfind('/'), path.size());
		return createPath(path, cost+1);
	} 
	return cost;
}

int main() {
	ifstream in("A-small-attempt6.in");
	ofstream out("large2.out");
	
	int t;
	in>>t;
	
	for(int i=0; i<t; ++i)  {
		int n, m;
		in>>n>>m;
		
		existingPaths.clear();
		for(int j=0; j<n; ++j) {
			string tmp;
			in>>tmp;
			existingPaths.push_back(tmp);
		}
		
		for(int m=0; m<existingPaths.size(); ++m) {
			for(int n=m; n<existingPaths.size(); ++n) {
				if(existingPaths[n].size() < existingPaths[m].size())
					swap(existingPaths[n], existingPaths[m]);
			}
		}
		
		int tcost = 0;
		for(int j=0; j<m; ++j) {
			string tmp;
			in>>tmp;
			string t2 = tmp;
			tcost += createPath(t2, 0);
			
			int k=0;
			existingPaths.push_back(tmp);
			
			for(int m=0; m<existingPaths.size(); ++m) {
				for(int n=m; n<existingPaths.size(); ++n) {
					if(existingPaths[n].size() < existingPaths[m].size())
						swap(existingPaths[n], existingPaths[m]);
				}
			}
		}
		out<<"Case #"<<i+1<<": "<<tcost<<endl;
			
	
	}
	in.close();
	out.close();
}