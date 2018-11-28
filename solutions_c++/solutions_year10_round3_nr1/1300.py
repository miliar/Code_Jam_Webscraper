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
#include <cassert>
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
#define IFF_GUYING
#ifdef IFF_GUYING
	ifstream inf("A-large.in");
	ofstream outf("A-large.out");
	#define cin inf
	#define cout outf
#endif

typedef struct{
	int x;
	int y;
}MY;
int main(int argc, char* argv[])
{
	int t;
	cin>>t;
	for(int i = 0;i < t;i++){
		int n;
		cin>>n;
		vector<MY> set;
		for(int j = 0;j < n;j++){
			int x,y;
			cin>>x>>y;
			MY p = {x,y};
			set.push_back(p);
		}
		int ret = 0;
		if(set.size() > 1){
			for(int j = 0;j < set.size();j++){
				vector<double> v;
				for(int k = j+1;k < set.size();k++){
					int x1 = set[j].x;
					int y1 = set[j].y;
					int x2 = set[k].x;
					int y2 = set[k].y;
					if((x1-x2)*(y1-y2)<0){
						double d = (double)(y1-y2)/(double)(x1-x2);
						int suc = 0;
						for(int l = 0;l < v.size();l++)
							if(v[l] == d){
								suc = 1;
								break;
							}
						if(suc == 0)
							v.push_back(d);
					}
				}
				ret+=v.size();
			}
		}
		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
	return 0;
}