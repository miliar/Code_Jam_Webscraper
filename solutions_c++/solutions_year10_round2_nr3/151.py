// Google Code Jam -- Europe Middle-East Africa Regional
// 6nd October 2008
//
// Problem  - 

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

string comp = "welcome to code jam";

long long mem[501][501];
long long nck[501][501];

int mod = 100003;

int main(int argc,const char * argv[]){

	// File stuff
	istream *in__;ostream *out__;
	if (argc > 1) in__ = new ifstream(argv[1]);else in__ = &cin;
	if (argc > 2) out__ = new ofstream(argv[2]);else out__ = &cout;
	istream & in = *in__;ostream & out = *out__;

	out.setf(ios::fixed,ios::floatfield);cout.setf(ios::fixed,ios::floatfield);
	out.precision(7);cout.precision(7);

	memset(nck,0,sizeof(nck));
	nck[0][0] = 1;
	for (int i=1;i<=500;i++)
		for (int j=0;j<i;j++){
			nck[i][j] += nck[i-1][j];
			nck[i][j+1] += nck[i-1][j];
			nck[i][j] %= mod;
			nck[i][j+1] %= mod;
		}

	

	// Main stuff starts here
	for (int TC = get <int>(in),cas = 1;cas <= TC;cas++){
		memset(mem,0,sizeof(mem));
		int N = get <int> (in);
		for (int i=2;i<=N;i++){
			mem[i][0] = 1;
			for (int j=1;j<i-1;j++)
				for (int k=0;k<j;k++)
					if (i-j-2 >= j-k-1)
						mem[i][j] = (mem[i][j] + mem[j+1][k]*nck[i-j-2][j-k-1]) % mod;
		}
		long long ret = 0;
		for (int i=0;i<N;i++)

			ret = (ret + mem[N][i]) % mod;

		out << "Case #" << cas << ": " << ret << endl;
	}


	if (in__!=&cin) delete in__;if (out__!=&cout) delete out__;
	return 0;
}