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

int main(int argc, char* argv[])
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int mx = 200;  
	char line[200];
	fin.getline(line, mx);
	int noc = to<int>(string(line));
	for(int i = 1; i <= noc; i ++) {
		fin.getline(line, mx);
		int nos = to<int>(string(line));
		map<string, int> m;
		for(int j = 0; j < nos; j ++) {
			fin.getline(line, mx);
			string ss(line);
			m[ss] = 1;
		}
		fin.getline(line, mx);
		int noq = to<int>(string(line));
		set<string> km;
		int r = 0;
		for(int j = 0; j < noq; j ++) {
			fin.getline(line, mx);
			string tt(line);
			if(m[tt] == 1) {
				km.insert(tt);
				if(km.size() == nos) {
					r ++;
					km.clear();
					km.insert(tt);
				}
			}
		}
		fout<<"Case #"<<i<<": "<<r<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

