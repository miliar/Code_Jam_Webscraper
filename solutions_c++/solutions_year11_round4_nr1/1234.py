#include <map>
#include <set>
#include <queue>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

typedef pair<int, int> pii;
typedef vector<pii> vp;

bool mysort (pii p1, pii p2) {
	return p1.second<p2.second;
}

int main() {

	ifstream fin("A-large.in");	
// 	ifstream fin("in.txt");	
	ofstream fout("out.txt");
	int T;
	fin>>T;
	
	for (int Ti=1; Ti<=T; Ti++) {
		
		double t;
		int X, S, R, N;
		fin>>X>>S>>R>>t>>N;
		
		int len = X;
		int b, e, w;
		
		vp v (N);
		
		for (int i=0; i<N; i++) {
			fin>>b>>e>>w;
			len -= (e-b);
			v[i].first = e-b;
			v[i].second = w+S;
		}
		if (len>0) v.push_back (pii(len, S));
		sort (v.begin(), v.end(), mysort);
// 
// 		for (int i=0; i<v.size(); i++) {
// 			cout<<v[i].first<<" "<<v[i].second<<endl;
// 		}
// 		cout<<"---"<<endl;
		
		double ret = 0;
		bool flag = 0;
		for (int i=0; i<v.size(); i++) {
			if (flag) {
				ret += v[i].first*1.0/v[i].second;
			}
			else {
				double tmp = v[i].first*1.0/(v[i].second-S+R);
				if (tmp>t) {
					flag = 1;
					ret += (t+(v[i].first-t*(v[i].second-S+R))*1.0/v[i].second);
				}
				else {
					t -= tmp;
					ret += tmp;
				}
// 				cout<<tmp<<" ";
			}
// 			cout<<ret<<" "<<t<<" "<<flag<<endl;
		}
// 		cout<<endl;
	
		fout<<setprecision(8);
		fout<<"Case #"<<Ti<<": "<<ret<<endl;
	}
	
	fout.close();
	return 0;
}
