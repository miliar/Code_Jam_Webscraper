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
		int ret = 0;
		vector<int> v(n,0);
		vector<int> vo;
		vector<int> vb;
		for(int j = 0;j < n;j++) {
			char c;
			int k;
			cin>>c>>k;
			if(c == 'O'){
				v[j] = k;
				vo.push_back(k);
			}else{
				v[j] = k+100;
				vb.push_back(k);
			}
		}
		int x = 1,y = 1;
		int o = 0,b = 0;
		for(int j = 0;j < n;j++) {
			int tt = 0;
			if(v[j] > 100) {
				tt = abs(vb[b]-y)+1;
				y = vb[b];
				b++;
				if(o < (int)vo.size()){
					if(abs(vo[o]-x) <= tt)
						x = vo[o];
					else {
						int k = abs(vo[o]-x)/(vo[o]-x);
						x += k*tt;
					}
				}
			} else {
				tt = abs(vo[o]-x)+1;
				x = vo[o];
				o++;
				if(b < (int)vb.size()){
					if(abs(vb[b]-y) <= tt)
						y = vb[b];
					else{
						int k = abs(vb[b]-y)/(vb[b]-y);
						y += k*tt;
					}
				}
			}
			ret += tt;
		}
		cout<<"Case #"<<i<<": "<<ret<<endl;
	}
	return 0;
}
