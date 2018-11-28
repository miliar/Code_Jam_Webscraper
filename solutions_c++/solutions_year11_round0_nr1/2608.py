#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <iostream>
#include <fstream>


using namespace std;

int main() {
	
	int T, N;

	ifstream fin("A-large.in");	
	fin>>T;
	
	ofstream fout("out.txt");
	
	vector< pair<int, int> > v;
	char c;
	int val;
	int ret;

	int cur[2];
	int p[2];
	int idx;
	
	int Ti, i, stp;
	
	for (Ti=0; Ti<T; Ti++) {
		v.clear();
		fin>>N;
		for (int i=0; i<N; i++) {
			fin>>c>>val;
			v.push_back(pair<int,int>(c=='B',val));
		}
		ret = 0;
		cur[0] = cur[1] = 1;
		for (p[0]=0; p[0]<v.size(); p[0]++) if (v[p[0]].first==0) break;
		for (p[1]=0; p[1]<v.size(); p[1]++) if (v[p[1]].first==1) break;

		while (p[0]<v.size()||p[1]<v.size()) {

			idx = (p[0]<p[1])?0:1;
// 			fout<<cur[0]<<"|"<<cur[1]<<"|"<<p[0]<<"|"<<p[1]<<"|"<<idx<<"|"<<ret<<endl;
			stp = abs(v[p[idx]].second-cur[idx]);
			if (abs(v[p[1-idx]].second-cur[1-idx])<=stp) {
				cur[1-idx] = v[p[1-idx]].second;
			}
			else {
				cur[1-idx] += (v[p[1-idx]].second>cur[1-idx])?stp:(-stp);
			}
			cur[idx] = v[p[idx]].second;
			ret += stp;
			
			if (cur[1-idx]!=v[p[1-idx]].second) cur[1-idx] += (v[p[1-idx]].second>cur[1-idx])?1:-1;
			ret += 1;
			
			for (p[idx]++; p[idx]<v.size(); p[idx]++) if (v[p[idx]].first==idx) break;
// 			cin>>c;
		}
		
		fout<<"Case #"<<Ti+1<<": "<<ret<<endl;
	}
	
	fout.close();
	
	return 0;
}
