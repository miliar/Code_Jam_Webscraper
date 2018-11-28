#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
using namespace std;

ifstream cin("B-Large.in");
ofstream cout("B.out");
int main(){
	int T,C,D,N;
	cin >> T;
	for(int i=0;i<T;i++){
		map <pair <char,char>, char> mcomb;
		map < pair<char,char>, char > mopp;
		cin >> C;
		for(int j = 0;j<C;j++){
			string s;
			cin >> s;
			pair <char,char> pc;
			pc.first = s[0];
			pc.second = s[1];
			mcomb[pc] = char(s[2]);
			pc.first = s[1];
			pc.second = s[0];
			mcomb[pc] = char(s[2]);
		}
		cin >> D;
		for(int j=0;j<D;j++){
			string s;
			cin >> s;
			mopp[pair<char,char> (s[0],s[1])] = 'a';
			mopp[pair<char,char> (s[1],s[0])] = 'a';	
		}
		vector <char> vc;
		cin >> N;
		for(int j=0;j<N;j++){			
			char c;
			cin >> c;
			//check if combine
			if(vc.size()!=0){
				pair<char,char> pc = make_pair(vc.back(),c);
				if(mcomb.count(pc)!=0){
					vc.pop_back();
					vc.push_back(mcomb[pc]);
					continue;
				}				
			}
			bool bopp = false;
			for(int k=0;k<vc.size();k++){
				if(mopp.count(make_pair(c,vc[k]))==1){
					bopp = true;
				}
			}
			if(bopp){
				vc.clear();
				continue;
			}
			vc.push_back(c);			
		}
		cout << "Case #" << i+1 << ": [";
		for(int k=0;k<int(vc.size())-1;k++){
			cout << vc[k] << ", ";
		}
		if(vc.size()!=0){
			cout << vc.back();
		}
		cout << "]" << endl;

	}
	return 0;
}