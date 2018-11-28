#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

class Trie{
	Trie * children[26];
	int terminal;
public:
	Trie(){memset(children,0,sizeof(children));terminal = 0;}
	void Add(const string &s,int i){
		if (i==s.size()){
			terminal++;
			return;
		}
		char c = s[i]-'a';
		if (!children[c])
			children[c] = new Trie();
		children[c]->Add(s,i+1);
	}
	int count(const string & patt,int i){
		if (i==patt.size()) return terminal;
		if (patt[i] == '('){
			i++;
			int j;
			for (j=i;patt[j]!=')';j++);
			int ret = 0;
			for (int k=i;k<j;k++)
				if (children[patt[k]-'a'])
					ret += children[patt[k]-'a'] -> count(patt,j+1);
			return ret;
		}
		if (children[patt[i]-'a'])
			return children[patt[i]-'a'] -> count(patt,i+1);
		return 0;
	}
};

int main(int argc,const char* argv[]){
	istream * _in = 0;
	ostream * _out = 0;
	if (argc > 1) _in = new ifstream(argv[1]); else _in = & cin;
	if (argc > 2) _out = new ofstream(argv[2]); else _out = & cout;
	istream & in = *_in;
	ostream & out = *_out;
	string line;
	getline(in,line);
	stringstream ss(line);
	int L,D,N;
	ss >> L >> D >> N;
	Trie solver;
	for (int i=0;i<D;i++){
		getline(in,line);
		if (line.size() != L) continue;
		solver.Add(line,0);
	}
	for (int i=0;i<N;i++){
		getline (in,line);
		out << "Case #" << (i+1) << ": " << solver.count(line,0) << endl;
	}

	if (_in != &cin) delete _in;
	if (_out != &cout) delete _out;
};
