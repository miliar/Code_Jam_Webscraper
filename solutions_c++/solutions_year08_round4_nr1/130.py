// Google Code Jam -- Online Round 2
// 2nd August 2008
//
// Problem A - Advanced Solution

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

#define INF 100000

using namespace std;


// A few utility I/O functions
vector <string> split(const string &s,const char &separator=' '){vector <string> ret;int p1=0,p2;for (p2 = 0;p2 < s.size();p2++)if (s[p2]==separator){if (p2-p1>0) ret.push_back(s.substr(p1,p2-p1));p1=p2+1;}if (p2-p1 > 0) ret.push_back(s.substr(p1,p2-p1));return ret;}
template <class T> T get(istream &fin){string s;getline(fin,s);stringstream ss(s);T ret;ss >> ret;return ret;}
template <class T> vector <T> getv(istream &fin,const char &separator = ' '){string s;getline(fin,s);vector <string> convert = split(s,separator);vector <T> ret(convert.size());for (int i=0;i<convert.size();i++){stringstream ss(convert[i]);ss>>ret[i];}return ret;}
template <> vector <string> getv <string> (istream &fin,const char &separator){string s;getline(fin,s);return split(s,separator);}
template <class T > string toStr(T x){stringstream ss;ss << x;return ss.str();}

int mem[10001][2];

int rec(int i,int val,const vector <pair <int,int> > &nodes){
	if (nodes[i].second == -1) return nodes[i].first == val ? 0 : INF;
	if (mem[i][val] >-1) return mem[i][val];
	int ret = INF;
	if (nodes[i].first == 0){ // AND gate
		if (val == 1) ret = rec(2*i+1,1,nodes) + rec(2*i+2,1,nodes);
		else ret = min(rec(2*i+1,0,nodes),rec(2*i+2,0,nodes));
	} else {
		if (val == 0) ret = rec(2*i+1,0,nodes) + rec(2*i+2,0,nodes);
		else ret = min(rec(2*i+1,1,nodes),rec(2*i+2,1,nodes));		
	}
	if (nodes[i].second == 1){
		if (nodes[i].first == 1){ // AND gate
			if (val == 1) ret = min(ret,1+rec(2*i+1,1,nodes) + rec(2*i+2,1,nodes));
			else ret =  min(ret,1+min(rec(2*i+1,0,nodes),rec(2*i+2,0,nodes)));
		} else {
			if (val == 0) ret =  min(ret,1+rec(2*i+1,0,nodes) + rec(2*i+2,0,nodes));
			else ret =  min(ret,1+min(rec(2*i+1,1,nodes),rec(2*i+2,1,nodes)));		
		}		

	}
	return (mem[i][val] = ret);
}

int main(int argc,const char * argv[]){

	// File stuff
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	fout.setf(ios::fixed,ios::floatfield);
	fout.precision(7);

	// Main stuff starts here
	for (int TC = get <int>(fin),cas = 1;cas <= TC;cas++){
		vector <int> v = getv <int> (fin);
		int N = v[0],M = v[1];
		vector <pair <int,int> > nodes(N);
		memset(mem,-1,sizeof(mem));
		for (int i=0;i<N;i++){
			vector <int> x = getv <int> (fin);
			if (x.size() == 2){
				nodes[i].first = 1-x[0];nodes[i].second = x[1];
			} else {
				nodes[i].first = x[0];nodes[i].second = -1;
			}
		}
		int r = rec(0,M,nodes);
		int x = rec(1,1,nodes);
		int y = rec(2,1,nodes);
		string res;
		if (r >= INF) res = "IMPOSSIBLE";
		else res = toStr(r);

		fout << "Case #" << cas << ": " << res << endl;
		if (argc == 4) cout  << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}