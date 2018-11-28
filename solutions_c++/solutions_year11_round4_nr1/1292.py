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
FILE *o = fopen("out.txt", "w");
typedef struct{
	int b;
	int e;
	int w;
}MY;

bool mysort(const MY &a,const MY &b)
{
	return a.w < b.w;
}
int main(int argc, char* argv[])
{
	int T;
	cin>>T;
	for(int x = 1;x <= T;x++) {
		int X,S,R,t,N;
		cin>>X>>S>>R>>t>>N;
		vector<MY> v(N);
		int len = X;
		for(int i = 0;i < N;i++){
			cin>>v[i].b>>v[i].e>>v[i].w;
			len -= v[i].e-v[i].b;
		}
		double ret = 0.0;
		if(t*R <= len){
			ret += t+double(len-t*R)/S;
			for(int i = 0;i < N;i++)
				ret += double(v[i].e-v[i].b)/(S+v[i].w);
		} else {
			double tt = t - double(len)/R;
			ret += double(len)/R;
			stable_sort(v.begin(),v.end(),mysort);
			int la = 0;
			for(int i = 0;i < N;i++){
				if(la == 0){
					if(v[i].e-v[i].b >= (R+v[i].w)*tt){
						ret += tt + double(v[i].e-v[i].b-(R+v[i].w)*tt)/(S+v[i].w);
						la = 1;
					}else
						ret += double(v[i].e-v[i].b)/(R+v[i].w);
					tt -= double(v[i].e-v[i].b)/(R+v[i].w);
				}else{
					ret += double(v[i].e-v[i].b)/(S+v[i].w);
				}
			}
		}
		//cout<<"Case #"<<x<<": "<<ret<<endl;
		fprintf(o,"Case #%d: %lf\n",x,ret);
	}
	return 0;
}
