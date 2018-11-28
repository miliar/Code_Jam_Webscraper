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

int main(int argc, char* argv[])
{
	int t;
	cin>>t;
	for(int i = 1;i <= t;i++) {
		int n;
		cin>>n;
		vector<int> v(n);
		int sum = 0;
		int s = 0;
		long long ret = 1000*1000000+1;
		for(int j = 0;j < n;j++){
			cin>>v[j];
			sum ^= v[j];
			s += v[j];
			if(ret > v[j])
				ret = v[j];
		}
		if(sum != 0)
			cout<<"Case #"<<i<<": NO"<<endl;
		else
			cout<<"Case #"<<i<<": "<<s-ret<<endl;
	}
	return 0;
}