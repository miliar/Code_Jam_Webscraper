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

int main() {

	ifstream fin("A-small-attempt1.in");	

	ofstream fout("out.txt");
	
	int T;
	fin>>T;
	
	for (int Ti=1; Ti<=T; Ti++) {
		bool ret = false;
		int d, pd, pg, g, n;
		fin>>n>>pd>>pg;
		
		if (pd+pg==0 || pd+pg==200) ret = 1;
		else if (pg==0 || pg==100) ret = 0;
		else {
			for (d=1; d<=n; d++) {
				if (d*pd%100!=0 || d*(100-pd)%100!=0) continue;
				
				if (pg!=0 && pg!=100) {
					ret = 1;
					break;
				}
			}
		}
		
		fout<<"Case #"<<Ti<<": ";
		if (ret) fout<<"Possible"<<endl;
		else fout<<"Broken"<<endl;
	}
	
	
	
	
	fout.close();
	
	return 0;
}
