#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <string>
#include <map>
//#include <pair>

using namespace std;

int main(int c, char* v[]) {
	int T;
	cin >> T;
	for (int i=0;i<T;++i) {		
		int C,D;
		cin >> C;
		string s,s1,s2;
		map<string,char> combine;
		vector<pair<char,char> > destroy;
		for (int j=0;j<C;++j) {
			cin >> s;
			s1 = s[0];
			s1 += s[1];
			s2 = s[1];
			s2 += s[0];
			combine[s1] = s[2]; 
			combine[s2] = s[2];
		}
		cin >> D;
		for (int j=0;j<D;++j) {
			cin >> s;
			destroy.push_back(pair<char,char>(s[0],s[1]));
		}
		int n;
		cin >> n;
		string input;
		cin >> input;
		string output;
		// find combination
		/*while (true) {
			size_t size=input.length();
			if (size >=2) {
				string last(input.substr(size-2,size-1));			
				if (combine.find(last) != combine.end()) {
					input.erase(size-2,size-1);
					input.append(1,combine[last]);
				}
				else
					break;
			}
			else
				break;
		}
		for (int k=0;k<destroy.size();++k) {
			if (input.find(destroy[k].first) != string::npos && input.find(destroy[k].second))
				input = string("");
		}*/
		for (int k=0;k<input.length();++k) {
			output.append(1,input[k]);
			size_t size=output.length();
			if (size >=2) {
				string last(output.substr(size-2,2));			
				if (combine.find(last) != combine.end()) {
					output.erase(size-2,2);
					output.append(1,combine[last]);
				}
			}
			for (int k=0;k<destroy.size();++k) {
				if (output.find(destroy[k].first) != string::npos && output.find(destroy[k].second) != string::npos)
					output = string("");
			}
		}
		cout << "Case #" << i+1 <<": [";
		for (int l=0;l<output.length();++l){
			cout<<output[l];
			if (l != output.length() -1)
				cout<<", ";
		}/*
		if (output.length() != 0)
			cout<<output[output.length()-1];*/
		cout << "]\n";
	}
}