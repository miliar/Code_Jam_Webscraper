// Google Code Jam -- Online Round 1
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

class dir{
	map <string,dir*> children;
public:
	int add(string s){
		if (s == "") return 0;
		int index = s.find("/",1);
		string th,ne;
		if (index == string::npos){
			th = s;
			ne = "";
		} else {
			th = s.substr(0,index);
			ne = s.substr(index);
		}
		int ret;
		if (children.find(th) == children.end()){
			children[th] = new dir();
			ret = 1;
		} else {
			ret = 0;
		}
		return ret + children[th] -> add(ne);
	}


};


int main(int argc,const char * argv[]){

	// File stuff
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	fout.setf(ios::fixed,ios::floatfield);
	fout.precision(7);

	// Main stuff starts here
	for (int TC = get <int>(fin),cas = 1;cas <= TC;cas++){
		vector <int> NM = getv <int>(fin);
		int N = NM[0],M=NM[1];
		dir D;
		int ret = 0;
		for (int i=0;i<N;i++)
			D.add(get <string> (fin));
		for (int i=0;i<M;i++)
			ret += D.add(get <string> (fin));

		fout << "Case #" << cas << ": " << ret << endl;
		if (argc == 4) cout  << "Case #" << cas << ": " << ret << endl;
	}
	return 0;
}