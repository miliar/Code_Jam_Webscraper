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
#define cin inf
ofstream outf("out.txt");
#define cout outf

set<string> dir;
string str[100];
int main(int argc, char* argv[])
{

	int T;
	cin>>T;
	for(int t=1; t<= T;t++)
	{
		
		dir.clear();
		int n,m;
		cin>>n>>m;
		for(int i=0;i<n;i++)
		{
			string s;
			cin>>s;
			dir.insert(s);
		}

		int ret=0;
		for(int i=0;i<m;i++)
		{
			cin>>str[i];
			string& s = str[i];
			s += "/";
			int np = 1;
			for(;;)
			{
				int idx = s.find_first_of("/",np);
				if(idx == string::npos)
					break;
				string pr = s.substr(0,idx);
				if(dir.find(pr) == dir.end())
				{
					ret++;
					dir.insert(pr);
				}
				np = idx+1;
			}
		}
		cout<<"Case #"<<t<<": "<<ret<<endl;
	}
}
