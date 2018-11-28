#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <map>

using namespace std;
int main(int argc, char ** argv){
	ifstream fin(argv[1]);
	int T;
	fin >> T;
	
	for (int t=0; t!= T; t++){
		int C;
		fin >> C;

		map<pair <char,char>,char> combine;
		for (int c=0; c!=C; c++) {
			string str;
			fin >> str;
			
			combine[pair <char,char>(str[0],str[1])] = str[2];
			combine[pair <char,char>(str[1],str[0])] = str[2];
		}

		int D;
		fin >> D;
		vector<pair <char,char> > oppose(D);
		for (int d=0; d!=D; d++) {
			string str;
			fin >> str;
			oppose[d] = pair <char,char>(str[0],str[1]);
//			cout << D<<"(" <<oppose[d].first <<"," << oppose[d].second << ")" << endl;
		}
		
		int N;
		fin >> N;
		char c;
		fin >> c;
		vector <char> elements;
		elements.push_back(c);
		for (int n=1; n!=N; n++) {
			char c;
			fin >> c;
			elements.push_back(c);
			
			for (bool change = true; change; change = false){
				unsigned int last = elements.size()-1;
				if (last ==0) break;
				
				map<pair <char,char>,char>::iterator elfind;
				if ((elfind = combine.find(
										 pair <char,char>(elements[last-1],elements[last])
										)) != combine.end()) {
					elements.pop_back();
					elements.pop_back();
					elements.push_back((char)elfind->second);
					continue;
				}
				
				for (unsigned int i = 0; i != oppose.size(); ++i) {
					bool a = find(elements.begin(),elements.end(),oppose[i].first ) != elements.end();
					bool b = find(elements.begin(),elements.end(),oppose[i].second) != elements.end();
					
					if (a && b) {
						elements.clear();
						break;
					}
					
				}
			}
		}
		
		
		
		cout << "Case #" << t+1 << ": " << "[";
		for (unsigned int i = 0; i != elements.size(); i++) {
			cout << elements[i];
			if (i != elements.size()-1) {
				cout <<", ";
			}
		}
		cout<< "]"<< endl;
	}
}