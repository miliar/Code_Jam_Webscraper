#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <boost/algorithm/string.hpp>
#include <algorithm>


using namespace std;
using namespace boost;

bool comp(string a, string b){
	return a.compare(b);
}

int main (int argc, char * const argv[]) {
	ifstream fin(argv[1]);
	unsigned long T;
	fin >> T;
//cout << T << endl;
	
	for(unsigned long i = 0; i != T; ++i) {
		unsigned long N,M;
		fin >> N >> M;
		vector<string> cdir;
		vector<string> mkdir;
		for (unsigned long j = 0; j != N; j++) {
			string line;
			fin >> line;
			cdir.push_back(line);
		}
		for (unsigned long j = 0; j != M; j++) {
			string line;
			fin >> line;
			mkdir.push_back(line);	
		}
		
		cdir.push_back("/");
		
//cout << N << " " << cdir.size() << " " << M << " " << mkdir.size() << endl;
	/*************/
		vector<string> cdirlist;
		vector<string> dirlist;
		
		for (unsigned long j = 0; j != cdir.size(); j++) {
			vector<string> strs;
			split(strs, cdir[j], is_any_of("/"));
			for (unsigned k = 0; k != strs.size(); k++) {
				ostringstream ss (ostringstream::out);
				for (unsigned l = 0; l != k+1; l++) {
					ss << strs[l] << "/";					
				}
				cdirlist.push_back(ss.str());
				dirlist.push_back(ss.str());
			}			
		}
		
		for (unsigned long j = 0; j != mkdir.size(); j++) {
			vector<string> strs;
			split(strs, mkdir[j], is_any_of("/"));
			
			for (unsigned k = 0; k != strs.size(); k++) {
				ostringstream ss (ostringstream::out);
				for (unsigned l = 0; l != k+1; l++) {
					ss << strs[l] << "/";					
				}
				dirlist.push_back(ss.str());
			}			
		}
		
		std::sort(dirlist.begin(), dirlist.end());
		dirlist.erase(unique (dirlist.begin(), dirlist.end()), dirlist.end());
		
		std::sort(cdirlist.begin(), cdirlist.end());
		cdirlist.erase(unique (cdirlist.begin(), cdirlist.end()), cdirlist.end());
		
		
//		unique (cdirlist.begin(), cdirlist.end(), comp);
//		unique (dirlist.begin(), dirlist.end(),comp);
//		
//		unsigned long unlistsize = 0  
//		for (int counter = 0; unlist != NULL; unlist++) {
//			unlistsize = counter;
//		}
//		
//		unsigned long cunlistsize = 0  
//		for (int counter = 0; cunlist != NULL; cunlist++) {
//			cunlistsize = counter;
//		}
		


			cout <<"Case #"<< i+1 <<": " << dirlist.size() - cdirlist.size()  << "\n";

		
	}

    return 0;
}
