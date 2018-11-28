#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <iostream>
#include <fstream>


using namespace std;

int main() {
	
	int T, N;

	ifstream fin("B-large.in");	
	fin>>T;
	
	ofstream fout("out.txt");
	
	map<string, char> C;
	set<string> D;
	vector<char> v;
	
	string s;
	char c, c1, c2, c3;
	bool op;
	
	for (int Ti=0; Ti<T; Ti++) {
		C.clear();
		D.clear();
		v.clear();
		
		fin>>N;
		for (int i=0; i<N; i++) {
			fin>>c1>>c2>>c3;
			s = c1;
			s += c2;
			C[s] = c3;
			s = c2;
			s += c1;
			C[s] = c3;
		}
		
		fin>>N;
		for (int i=0; i<N; i++) {
			fin>>c1>>c2;
			s = c1;
			s += c2;
			D.insert(s);
			s = c2;
			s += c1;
			D.insert(s);
		}
		
		fin>>N;
		fin>>c1;
		v.push_back(c1);
		for (int i=1; i<N; i++) {
			fin>>c;
			v.push_back(c);
			
			// combine
			while (v.size()>1) {
				s = v[v.size()-2];
				s += v[v.size()-1];
				if ( C.count(s)==0 ) break;
				else {
					v.pop_back();
					v[v.size()-1] = C[s];
				}
			}
			
			// oppose
			if (v.size()<2) continue;
			op = 0;
			c = v[v.size()-1];
			for (int j=0; j<v.size()-1; j++) {
				s = v[j];
				s += c;
				if (D.count(s)>0) {
					op = 1;
					break;
				}
			}
			if (op) v.clear();
		}
		
		fout<<"Case #"<<Ti+1<<": [";
		if (v.size()==0) fout<<"]"<<endl;
		else {
			for (int i=0; i<v.size()-1; i++) {
				fout<<v[i]<<", ";
			}
			fout<<v[v.size()-1]<<"]"<<endl;
		}
	}
	
	fout.close();
	
	return 0;
}
