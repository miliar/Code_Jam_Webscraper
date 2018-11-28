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

int main(int argc, char* argv[])
{

	int T;
	cin>>T;
	for(int tt=1; tt<= T;tt++)
	{
		int n,k,b,t;
		cin>>n>>k>>b>>t;
		int l[50];
		int v[50];

		for(int i=0;i<n;i++)
			cin>>l[i];
		for(int i=0;i<n;i++)
			cin>>v[i];
		int m[50] = {0};
		int nk = 0;
		int id;
		for(id = n-1;id>=0;id--)
		{
			if(l[id]+v[id]*t<b)
			{
				m[id] = 1;
			}
			else
				nk++;
			if(nk==k)
				break;
		}
		cout<<"Case #"<<tt<<": ";
		if(nk < k)
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		int ret = 0;
		for(int i=0;i<n;i++)
		{
			if(m[i])
			{
				for(int it=id;it<i;it++)
					if(m[it] == 0)
						ret++;
			}
		}
		cout<<ret<<endl;
	}
}
