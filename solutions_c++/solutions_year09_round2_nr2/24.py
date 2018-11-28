// Google Code Jam 2009 -- Round 1B
// 12th October 2008
//
// Problem B -  

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
		string s,ans;
		getline(in,s);
		string t = s;
		sort(&t[0],&t[t.size()],greater <char>());
		if (s == t){
			sort(&s[0],&s[s.size()]);
			s = string(1,'0') + s;
			int p = 0;
			while(s[p] == '0') p++;
			swap(s[p],s[0]);
			ans = s;
		} else {
			for (int i=s.size()-2;i>=0;i--){
				int best = -1;
				for (int j=i+1;j<s.size();j++)
					if (s[j] > s[i] && (best == -1 || s[best] > s[j]))
						best = j;
				if (best != -1){

					swap(s[best],s[i]);
					sort(&s[i+1],&s[s.size()]);
					ans = s;
					break;
				}
			}
		}
		out << "Case #" << cas << ": " << ans << endl;
	}

	if (in__!=&cin) delete in__;if (out__!=&cout) delete out__;
	return 0;
}