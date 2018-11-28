#define _CRT_SECURE_NO_DEPRECATE
//
//
//
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

const double zero=1e-6;
const double limit=1e8;
#define SZ(x) (int(x.size()))
typedef long long int64;
typedef unsigned long long uint64;
template<class T> T sqr(T x) {return x*x;}
template<class T> T gcd(T a,T b){ if(a<0) return gcd(-a,b);if(b<0) return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(T a,T b){ return a*(b/gcd(a,b));}
int64 toInt64(string s){ istringstream sin(s); int64 t; sin>>t;return t;}
int toInt(string s){ istringstream sin(s); int t; sin>>t; return t;}
template<class T> string toString(T x){ ostringstream sout; sout<<x; return sout.str();}

ifstream inf("in.txt");
ofstream of("out.txt");
#define cin inf
#define cout of

int cb[200][200];
int op[100][100];
int main(int argc, char* argv[])
{
	int t;
	cin>>t;
	for(int i = 1;i <= t;i++) {
		memset(cb,0,sizeof(cb));
		memset(op,0,sizeof(op));
		string ret;
		ret.push_back('[');
		int c,d,n;
		cin>>c;
		for(int j = 0;j < c;j++) {
			char a,b,ct;
			cin>>a>>b>>ct;
			cb[b][a] = cb[a][b] = ct;
		}
		cin>>d;
		for(int j = 0;j < d;j++) {
			char a,b;
			cin>>a>>b;
			op[b][a] = op[a][b] = 1;
		}
		cin>>n;
		string s;
		for(int j = 0;j < n;j++) {
			char sc;
			cin>>sc;
			int sz = (int)s.size();
			if(sz > 0 && cb[s[sz-1]][sc] > 0) {
				s[sz-1] = (char)cb[s[sz-1]][sc];
			} else {
				int la = 0;
				for(int k = 0;k < sz;k++) {
					if(op[sc][s[k]] == 1){
						s.clear();
						la = 1;
						break;
					}
				}
				if(la == 0)
					s.push_back(sc);
			}
		}
		for(int j = 0;j < (int)s.size();j++){
			ret.push_back(s[j]);
			if(j < (int)s.size()-1)
				ret.append(", ");
		}
		ret.push_back(']');
		cout<<"Case #"<<i<<": "<<ret<<endl;
	}
	return 0;
}