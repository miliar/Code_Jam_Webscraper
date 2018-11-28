// Google Code Jam 2009 -- Round 1B
// 12th October 2008
//
// Problem A -  

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <fstream>
#include <cmath>
#include <queue>
#include <set>
#include <algorithm>
#include <list>
#include <cstdio>
using namespace std;


// A few utility I/O functions
vector <string> split(const string &s,const char &separator=' '){vector <string> ret;int p1=0,p2;for (p2 = 0;p2 < s.size();p2++)if (s[p2]==separator){if (p2-p1>0) ret.push_back(s.substr(p1,p2-p1));p1=p2+1;}if (p2-p1 > 0) ret.push_back(s.substr(p1,p2-p1));return ret;}
template <class T> T get(istream &fin){string s;getline(fin,s);stringstream ss(s);T ret;ss >> ret;return ret;}
template <class T> vector <T> getv(istream &fin,const char &separator = ' '){string s;getline(fin,s);vector <string> convert = split(s,separator);vector <T> ret(convert.size());for (int i=0;i<convert.size();i++){stringstream ss(convert[i]);ss>>ret[i];}return ret;}
template <> vector <string> getv <string> (istream &fin,const char &separator){string s;getline(fin,s);return split(s,separator);}

int fin(const string &s,int i){
	int count = 0;
	do {
		if (s[i] == '(') count++;
		if (s[i] == ')') count--;
		i++;
	} while(count > 0);
	return i;
}

class TreeNode{
public:
	string name;
	double weight;
	TreeNode *c1,*c2;
	TreeNode(){c1 = 0;c2 = 0;}
	void add(const string &s,int st,int en){
		while (s[st] == ' ') st++;
		while (s[en] == ' ') en--;
		if (s[st] == '(' && s[en] == ')') {st++;en--;}
		while (s[st] == ' ') st++;
		while (s[en] == ' ') en--;
		//cout << s.substr(st,en-st+1) << endl;
		name = "";
		string val;
		while (s[st] != ' ' && s[st] != ')') val += s[st++];
		stringstream ss(val);
		ss >> weight;
		while (s[st] == ' ' && s[st] != ')') st++;
		if (s[st] == ')') return;
		while (s[st] != ' ') name += s[st++];
		while (s[st] == ' ') st++;
		int e1 = fin(s,st);
		c1 = new TreeNode();
		c1 -> add(s,st,e1-1);
		c2 = new TreeNode();
		c2 -> add(s,e1,en);
	}
	double get(const set <string> &an){
		if (name == "") return weight;
		if (an.find(name) != an.end()) return weight * (c1 -> get(an));
		else return weight * (c2 -> get(an));
	}
};

int main(int argc,const char * argv[]){

	// File stuff
	istream *in__;ostream *out__;
	if (argc > 1) in__ = new ifstream(argv[1]);else in__ = &cin;
	if (argc > 2) out__ = new ofstream(argv[2]);else out__ = &cout;
	istream & in = *in__;ostream & out = *out__;

	out.setf(ios::fixed,ios::floatfield);cout.setf(ios::fixed,ios::floatfield);
	out.precision(7);cout.precision(7);

	// Main stuff starts here
	for (int TC = get <int>(in),cas = 1;cas <= TC;cas++){
		string s;
		int L = get <int> (in);
		for (int i=0;i<L;i++){
			string line;
			getline(in,line);
			s+= line + " ";
		}
		TreeNode tree;
		tree.add(s,0,s.size()-1);
		int A = get <int> (in);
		out << "Case #" << cas << ":"<< endl;
		for (int i=0;i<A;i++){
			vector <string> an = getv <string>(in);
			set <string> p;
			for (int i=2;i<an.size();i++)
				p.insert(an[i]);
			out << tree.get(p) << endl;
		}
			
	}

	if (in__!=&cin) delete in__;if (out__!=&cout) delete out__;
	return 0;
}