// Google Code Jam -- Online Round 2
// 5th June 2010
//
// Problem C - Large Solution

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
		set <pair <int,int> > B;
		int N;
		in >> N;
		for (int i=0;i<N;i++){
			int X1,X2,Y1,Y2;
			in >> X1 >> Y1 >> X2 >> Y2;
			for (int x = X1;x <= X2;x++)
				for (int y = Y1;y <= Y2;y++)
					B.insert(make_pair(x,y));
		}
		int ans;
		vector <pair <int,int> > check;
		for (set <pair <int,int> >::iterator it = B.begin();it != B.end();it++){
			check.push_back(make_pair((*it).first,(*it).second));
			check.push_back(make_pair((*it).first+1,(*it).second));
			check.push_back(make_pair((*it).first,(*it).second+1));
		}

		for (ans = 0;!B.empty();ans++){
			sort(check.begin(),check.end(),greater <pair <int,int> >());
			vector <pair <int,int> > cnew;
			for (int i=0;i<check.size();i++){
				int x = check[i].first;
				int y = check[i].second;
				if (B.find(check[i]) != B.end()){
					if (B.find(make_pair(x-1,y)) == B.end() && B.find(make_pair(x,y-1)) == B.end()){
						B.erase(check[i]);
						cnew.push_back(make_pair(x+1,y));
						cnew.push_back(make_pair(x,y+1));
					}
				} else {
					if (B.find(make_pair(x-1,y)) != B.end() && B.find(make_pair(x,y-1)) != B.end()){
						B.insert(check[i]);
						cnew.push_back(make_pair(x+1,y));
						cnew.push_back(make_pair(x,y+1));
					}
				}
			}
			check = cnew;
		}


		out << "Case #" << cas << ": " << ans << endl;
		if (argc == 4) cout  << "Case #" << cas << ": " << ans << endl;
	}
	return 0;
}