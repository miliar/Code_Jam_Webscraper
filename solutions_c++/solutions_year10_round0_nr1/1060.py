#define _CRT_SECURE_NO_DEPRECATE
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


#define IFF_GUYING
#ifdef IFF_GUYING
	ifstream inf("in.txt");
#define cin inf
#endif

ofstream outf("out.txt");
#define cout outf

int main(int argc, char* argv[])
{
	int t,n,k;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";

		cin>>n>>k;

		int m;
		for(m=0;m<n;m++)
		{
			if( (1<<m & k) == 0)
			{
				cout<<"OFF"<<endl;
				break;
			}
		}
		if (m == n)
			cout<<"ON"<<endl;
	}
	return 0;
}
