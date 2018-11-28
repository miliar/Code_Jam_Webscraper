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


using namespace std;


bool works (vector<int>&v, double m, int d) {
	double now = v[0]-m;
	int i;
// 	cout<<now<<" ";
	for (i=1; i<v.size(); i++) {
		if (v[i]-m>now+d) now = v[i]-m;
		else if (v[i]+m>now+d) now += d;
		else break;
// 		cout<<now<<" ";
	}
// 	cout<<endl;
	return i==v.size();
}


int main() {

	ifstream fin("B-small-attempt0.in");	
// 	ifstream fin("in.txt");	
	ofstream fout("out.txt");
	int T;
	fin>>T;
	
	for (int Ti=1; Ti<=T; Ti++) {
		int c, d;
		fin>>c>>d;
		
		vector<int> v;
		for (int i=0; i<c; i++) {
			int tp, tv;
			fin>>tp>>tv;
			for (int j=0; j<tv; j++) v.push_back(tp);
		}
		sort(v.begin(), v.end());
// 		for (int i=0; i<v.size(); i++) cout<<v[i]<<" ";
// 		cout<<"| "<<v.size()<<endl;

		double e=1e-8, m=-1, l=0, r=-1, n=1.0;
		
		while (abs(n-m)>e) {
			m = n;
// 			cout<<m<<endl;
			if (!works (v, m, d)) {
				if (r>0) {
					n = (m+r)/2;
					l = m;
				}
				else {
					n = 2*m;
					l = m;
				}
			}
			else {
				n = (l+m)/2;
				r = m;
			}
			
		}
// 		cout<<endl<<endl;
		
		fout<<"Case #"<<Ti<<": "<<m<<endl;
	}
	
	fout.close();
	return 0;
}
