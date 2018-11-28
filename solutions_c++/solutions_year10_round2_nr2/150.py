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
		vector <int> param = getv <int> (in);
		int N = param[0];
		int K = param[1];
		int B = param[2];
		int T = param[3];
		vector <int> x = getv <int> (in);
		vector <int> v = getv <int> (in);
		vector <bool> yes(N);
		vector <pair <int,int> > ch (N);
		for (int i=0;i<N;i++)
			ch[i] = make_pair(x[i], v[i]);
		sort(ch.begin(),ch.end());
		for (int i=0;i<N;i++)
			if (B-ch[i].first <= ch[i].second * T)
				yes[i] = true;
		int done = 0,ret = 0;
		for (int i=N-1;i>=0 && done < K;i--){
			if (yes[i]){

				for (int j=i+1;j<N;j++)
					if (!yes[j])
						ret++;
				done++;
			}

			
		}
		if (done == K)
			out << "Case #" << cas << ": " << ret << endl;
		else
			out << "Case #" << cas << ": IMPOSSIBLE" << endl;
	}


	if (in__!=&cin) delete in__;if (out__!=&cout) delete out__;
	return 0;
}