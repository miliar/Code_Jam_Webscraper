// Google Code Jam -- Online Round 2
// 2nd August 2008
//
// Problem C - Advanced Solution

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

double Abs(const double &x){
	return x < 0.0 ? -x : x;
}

double evaluate(const vector <vector <int> > &p,const vector <double> &s){
	double res = 0.0;
	for (int i=0;i<p.size();i++)
		res = max(res,(Abs(s[0]-p[i][0]) + Abs(s[1]-p[i][1]) + Abs(s[2] - p[i][2])) / p[i][3]);
	return res;
}
double tsearch(vector <double> &mx,vector <double> &mn,int dim,const vector <vector <int> > &p){
		if (dim == 3) return evaluate(p,mn);
		for (int i=0;i<45;i++){
			double m1 = mn[dim];
			double x1 = mn[dim] + (mx[dim] - mn[dim]) * 0.501;
			double x2 = mn[dim] + (mx[dim] - mn[dim]) * 0.499;
			mn[dim] = x1;mx[dim+1]=1e6;mn[dim+1]=0.0;
			double d1 = tsearch(mx,mn,dim+1,p);
			mn[dim] = x2;mx[dim+1]=1e6;mn[dim+1]=0.0;
			double d2 = tsearch(mx,mn,dim+1,p);
			if (d1 < d2) mn[dim] = x2;
			else mn[dim]=m1,mx[dim] = x1;
		}
		return evaluate(p,mn);
}

int main(int argc,const char * argv[]){

	// File stuff
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	fout.setf(ios::fixed,ios::floatfield);
	fout.precision(7);

	// Main stuff starts here
	for (int TC = get <int>(fin),cas = 1;cas <= TC;cas++){
		int N = get <int> (fin);
		vector <vector <int> > points(N);
		for (int i=0;i<N;i++)
			points[i] = getv <int> (fin);

		vector <double> mx(4,1e6),mn(4,0);
		double res = tsearch(mx,mn,0,points);
		cout << mn[0] << " " << mn[1] << " " << mn[2] << " "<<evaluate(points,mn) << endl;
		fout << "Case #" << cas << ": " << res << endl;
		if (argc == 4) cout  << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}