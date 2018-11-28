#include <fstream>
#include <string>
#include <map>
#include <memory.h>
#include <iostream>
#include <cstdio>
using namespace std;


int main() {
	ifstream fin("a-small.in");
	ofstream fout("a-small.out");
	
	int n;
	char buffer[201];
	fin.getline(buffer, 200);
	sscanf(buffer,"%d", &n);
	
	for (int i = 0; i < n; ++i) {
		map <string, int> mp;
		int m; 
		fin.getline(buffer, 200);
		sscanf(buffer, "%d", &m);
		
		bool v[m]; 
		memset(v, 0, m);
		
		for (int j = 0; j < m; ++j) {			
			fin.getline(buffer, 200);
			string t(buffer);			
			mp[t] = j;
		}
		
		int switchCount = 0;
		
		int querysize; 
		fin.getline(buffer, 200);
		sscanf(buffer, "%d", &querysize);	
		
		map <string, int>::iterator it;
		
		int diffCount = 0;
		string q;
		
		char buffer[201];
		for (int j = 0; j < querysize; ++j) {			
			fin.getline(buffer, 200);
			string q(buffer);
			
			it = mp.find(q);
			if (it != mp.end()) {				
				int idx = it->second;				
				if (!v[idx]) {
					v[idx] = true;
					diffCount++;
				}
				if (diffCount == m) {
					switchCount++;
					memset(v, 0, m);						
					diffCount = 1;
					v[idx] = true;
				}								
			}
		}
		
		fout << "Case #" << i + 1 << ": " << switchCount << endl;
		
	}	
	
	fin.close();
	fout.close();
}
