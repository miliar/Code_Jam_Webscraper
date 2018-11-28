// Google Code Jam -- Online Round 2
// 5th June 2010
//
// Problem A

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
		int k= get <int> (in);
		vector <string> D(2*k-1);
		for (int i=0;i<2*k-1;i++)
			getline(in,D[i]);
		for (int i=0;i<D.size();i++)
			if (D[i].size() < 2*k-1)
				D[i] += string(2*k-1-D[i].size(),' ');

		int res = 1000000000;
		vector <vector <bool> > sym1(2*k-1,vector <bool>(2*k-1));
		vector <vector <bool> > sym2(2*k-1,vector <bool>(2*k-1));
		for (int i=0;i<D.size();i++)
			for (int j=0;j<D[i].size();j++){
				bool sym = true;
				for (int j1=j-1,j2=j+1;j1 >= 0 && j2 < D[i].size();j1--,j2++)
					if (D[i][j1] != ' ' && D[i][j2] != ' ' && D[i][j1] != D[i][j2])
						sym = false;
				sym1[i][j] = sym;
			}
		for (int i=0;i<D[0].size();i++)
			for (int j=0;j<D.size();j++){
				bool sym = true;
				for (int j1=j-1,j2=j+1;j1 >= 0 && j2 < D.size();j1--,j2++)
					if (D[j1][i] != ' ' && D[j2][i] != ' ' && D[j1][i] != D[j2][i])
						sym = false;
				sym2[i][j] = sym;
			}

		for (int i=0;i<D.size();i++)
			for (int j=0;j<D[i].size();j++){
				bool sym = true;
				for (int K=0;K<sym1.size();K++)
					if (!sym1[K][j])
						sym = false;
				for (int K=0;K<sym1.size();K++)
					if (!sym2[K][i])
						sym = false;
				if (sym){
					int i1 = max(i-k+1,k-i-1);
					int j1 = max(j-k+1,k-j-1);
					int m = i1 + j1 + k;
					res = min(res,m*m-k*k);
				}
			}



		out << "Case #" << cas << ": " << res << endl;
		if (argc == 4) cout  << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}