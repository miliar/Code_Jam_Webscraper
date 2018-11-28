#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <fstream>
#include <set>
#include <vector>
using namespace std;
map<pair<char,char>, char> two_base;
set<pair<char,char> > opposed;

int T;

void solve(vector<char> &elements){
	int sz = elements.size();
	if(sz>1 && two_base.count(make_pair(elements[sz-1], elements[sz-2]))){
		elements[sz-2] = two_base[make_pair(elements[sz-1], elements[sz-2])];
		elements.pop_back();
		solve(elements);
	}
	sz = elements.size();
	for(int j = sz-2; j>=0; j--){
		if(opposed.count( make_pair(elements[sz-1], elements[j])) > 0){
			elements.clear();
			return;
		}
	}
}

int main(){
	ifstream in("Input.in");
	ofstream out("Output.out");
	in >> T;
	string str;
	for(int i = 0; i<T; i++){
		two_base.clear(); opposed.clear(); str.clear();
		int C,D,N;
		in >> C;
		for(int j = 0; j<C; j++){
			in >> str;
			two_base[make_pair(str[0],str[1])] = str[2];
			two_base[make_pair(str[1],str[0])] = str[2];
		}
		in >> D;
		for(int j = 0; j<D; j++){
			in >> str;
			opposed.insert(make_pair(str[0],str[1]));
			opposed.insert(make_pair(str[1],str[0]));
		}
		in >> N >> str;
		vector<char> elements;
		for(int i = 0; i<N; i++){
			elements.push_back(str[i]);
			solve(elements);
		}
		out << "Case #" << i+1 << ": ";
		out << "[";
		if(elements.size()>0) out << elements[0];
		for(int i = 1; i<elements.size(); i++)
			out << ", " << elements[i];
		out << "]" << endl;
	}
} 

