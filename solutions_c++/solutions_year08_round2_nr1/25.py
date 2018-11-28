// Google Code Jam -- Online Round 1
// 26th July 2008
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


int main(int argc,const char * argv[]){

	// File stuff
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	fout.setf(ios::fixed,ios::floatfield);
	fout.precision(7);

	// Main stuff starts here
	for (int TC = get <int>(fin),cas = 1;cas <= TC;cas++){
		long long N,A,B,C,D,x0,y0,M,res = 0;
		vector <int> v = getv <int> (fin);
		N = v[0], A = v[1], B = v[2], C = v[3], D = v[4], x0 = v[5], y0 = v[6], M = v[7];

		long long count[3][3];
		memset(count,0,sizeof(count));
		for (int i=0;i<N;i++){
			count[x0 % 3][y0 % 3]++;
			x0 = (A * x0 + B) % M;
			y0 = (C * y0 + D) % M;
		}
		vector <pair <int,int> > p;
		for (int i=0;i<3;i++)
			for (int j=0;j<3;j++)
				p.push_back(make_pair(i,j));
		for (int i=0;i<p.size();i++)
			for (int j=i;j<p.size();j++)
				for (int k=j;k<p.size();k++)
					if (((p[i].first + p[j].first + p[k].first) % 3) == 0 && ((p[i].second + p[j].second + p[k].second) % 3) == 0)
						res += count[p[i].first][p[i].second] * (count[p[j].first][p[j].second] - (j==i)) * (count[p[k].first][p[k].second] - (k==i) - (k==j)) / ((k==i && k==j) ? 6 : (k==i || k==j || i==j) ? 2 : 1);


		fout << "Case #" << cas << ": " << res << endl;
		if (argc == 4) cout  << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}