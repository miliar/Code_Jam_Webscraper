#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>

using namespace std;

string act[105];
string tod[105];

set<string> s;


int main() {
	int M,N,T,f,ct;
	cin >> T;
	string damn;
	for(int c=1;c<=T;c++) {		
		ct=0;
		cin >> N >> M;
		for(int i=0;i<N;i++) {
			cin >> act[i];
			f=act[i].find('/',1);
			while(f!=-1) {				
				s.insert(act[i].substr(1,f-1));
				f=act[i].find('/',f+1);
			}
			s.insert(act[i].substr(1,act[i].size()));
		}				
		for(int i=0;i<M;i++) {
			cin >> tod[i];
			f=tod[i].find('/',1);
			while(f!=-1) {
				damn = tod[i].substr(1,f-1);
				//cout << damn << '\n'; 
				if(s.find(damn) == s.end()) {
					//cout << damn << '\n';
					ct++;
					s.insert(damn);
				}
				f=tod[i].find('/',f+1);
			}
			damn = tod[i].substr(1,tod[i].size());
			if(s.find(damn) == s.end()) {
				//cout << damn << '\n';
				ct++;
				s.insert(damn);
			}
		}		
		cout << "Case #" << c << ": " << ct << '\n';
		s.erase(s.begin(),s.end());
	}
	return 0;
}
