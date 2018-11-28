// Google Code Jam -- Online Round 2
// 5th June 2010
//
// Problem B - Large Solution

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
#define INF 100000000000000LL;

using namespace std;


// A few utility I/O functions
vector <string> split(const string &s,const char &separator=' '){vector <string> ret;int p1=0,p2;for (p2 = 0;p2 < s.size();p2++)if (s[p2]==separator){if (p2-p1>0) ret.push_back(s.substr(p1,p2-p1));p1=p2+1;}if (p2-p1 > 0) ret.push_back(s.substr(p1,p2-p1));return ret;}
template <class T> T get(istream &fin){string s;getline(fin,s);stringstream ss(s);T ret;ss >> ret;return ret;}
template <class T> vector <T> getv(istream &fin,const char &separator = ' '){string s;getline(fin,s);vector <string> convert = split(s,separator);vector <T> ret(convert.size());for (int i=0;i<convert.size();i++){stringstream ss(convert[i]);ss>>ret[i];}return ret;}
template <> vector <string> getv <string> (istream &fin,const char &separator){string s;getline(fin,s);return split(s,separator);}


long long mem[2048][11];
vector <int> costs;
vector <int> teams;

long long rec(int match,int missed){
	if (match >= costs.size()){
		int i = match - costs.size();
		if (teams[i] >= missed) return 0;
		else return INF;
	}
	if (mem[match][missed] != -1) return mem[match][missed];
	long long ret = costs[match] + rec(match*2+1,missed) + rec(match*2+2,missed);
	ret = min(ret,rec(match*2+1,missed+1) + rec(match*2+2,missed+1));
	return mem[match][missed] = ret;
}

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
		memset(mem,-1,sizeof(mem));
		int N;
		in >> N;
		costs = vector <int> ((1 << N) - 1);
		teams = vector <int> (1 << N);

		for (int i=0;i<(1<<N);i++)
			in >> teams[i];

		vector <vector <int> > g(N);

		for (int i=0;i<N;i++)
			for (int j=0;j<(1 << (N-i-1));j++){
				int temp;
				in >> temp;
				g[i].push_back(temp);
			}
		int p = 0;
		for (int i=N-1;i>=0;i--)
			for (int j=0;j<g[i].size();j++)
				costs[p++] = g[i][j];

		long long ans = rec(0,0);

		out << "Case #" << cas << ": " << ans << endl;
		if (argc == 4) cout  << "Case #" << cas << ": " << ans << endl;

	}
	return 0;
}