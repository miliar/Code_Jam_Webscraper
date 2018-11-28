#include <vector>
#include <list>
#include <cstring>
#include <cstdio>
#include <stdlib.h>
#include <iostream>
#include <queue>
#include <sstream>
#include <map>
#include <cmath>
#include <algorithm>
using namespace std;
#define FN(i,n) for (int i=0; i<(int)(n); i++)
#define SZ(c) ((int)(c).size())

#define FBE(i,v,T) for (vector<T >::iterator i=(v).begin(); i!=(v).end(); i++)
#define FEB(i,v,T) for (vector<T >::reverse_iterator i=(v).rbegin(); i!=(v).rend(); i++)
#define ABS(a) ((a)<0?-(a):(a))
#define PI     3.14159265358979323846
#define MIN (a,b)  ((a)<(b) ? (a) : (b))
#define MAX (a,b)  ((a)<(b) ? (b) : (a))
#define MAXINT (1<<30)
#define MININT (-MAXINT)
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
template<class X,class Y> ostream &operator<<(ostream &s, pair<X,Y> p){s<<p.first<<'@'<<p.second;return s;}
template<class V> ostream &operator<<(ostream &s, list<V> v){char c='{';for (typename list<V >::iterator i=v.begin(); i!=v.end();i++){s<<c<<*i; c=','; }s<<'}';return s;}
template<class A> string printString(A o ) { ostringstream s; (s << o); return s.str(); }
template<class C> void kill(C&c){for(typename C::iterator i=c.begin(); i!=c.end(); i++)kill:for(typename C::iterator j=i+1;j!=c.end();j++)if(*i==*j){*j=c.back();c.pop_back();goto kill;}}
template<class TA, class TV> void feed(vector<TV> &v, TA a[], int n) {  v.clear(); FN(i,n) v.push_back(TV(a[i])); }
#define FEED(vec,arr) feed((vec),(arr),sizeof((arr))/sizeof((arr)[0]))
#define all(a) (a).begin(), (a).end()
vector<string> tokens(const string &str, const string &delims){
	char *buf = strdup(str.c_str()), *token;
	const char *dels = delims.c_str();
	vector<string> v;
	token = strtok( buf, dels );
	while (token) {	v.push_back(token);	token = strtok(NULL, dels);	}
	free(buf);
	return v;
}
#define erase_unique(v)     (v).erase(unique(all(v)),v.end())  
#define erase_remove(v,val) (v).erase(remove(all(v),(val)),v.end()) 

template<class T> ostream &operator<<(ostream &s, vector<T> v){char c='[';for(typename vector<T >::iterator i=v.begin();i!=v.end();i++){s<<c<<*i;c=',';}s<<']';return s;}
// END CUT HERE 

double dist(double x0,double y0,double x1,double y1) {
	return sqrt((x0-x1)*(x0-x1) + (y0-y1)*(y0-y1));
}
vector<int> xs, ys, rs;

double DS[40][40][40];
#include "stdio.h"
int main(int argc, char* argv[])
{
	int CASES, N;
	cin >> CASES;
	for (int test=0; test<CASES; test++) {
		cin>>N;
		xs=vector<int>(N);
		ys=vector<int>(N);
		rs=vector<int>(N);
		FN(i,N) cin>>xs[i]>>ys[i]>>rs[i];
		
		FN(i,N)FN(j,N) {
			double x0 = (double)(xs[i]+xs[j])/2.0;
			double y0 = (double)(ys[i]+ys[j])/2.0;
			FN(k,N) {
				DS[i][j][k] = dist(x0,y0,xs[k],ys[k]) + rs[k];
// 				cout<<"dist "<<x0<<","<<y0<<"->"<<xs[k]<<","<<ys[k]<<" (+"<<rs[k]<<")="<<DS[i][j][k]<<endl;;
			}
		}
		
		
		double ret = -1;
		if (N==1) {
			ret=rs[0];
		} else if (N==2) {
			ret = max(rs[0],rs[1]);
		} else if (N==3) {
			ret = 1<<30;
			FN(single,N) {
				vector<int> xx, yy, rr;
				FN(no,N) if (no!=single) {
					xx.push_back(xs[no]);
					yy.push_back(ys[no]);
					rr.push_back(rs[no]);
				}
								
				double dd=dist(xx[0],yy[0], xx[1],yy[1])+rr[0]+rr[1];
				ret = min(ret, max(dd/2.0, (double)rs[single]));
			}
		} else {
			cout<<"Error"<<endl;
		}
			
		printf("Case #%d: %0.9f\n", test+1, ret);
		continue;
//		cout<<xs<<endl;
//		cout<<ys<<endl;
//		cout<<rs<<endl;
		double best = 1<<30;
		FN(i0,N)FN(j0,N) {
			// riega i0 e i1	
			double x0 = (double)(xs[i0]+xs[j0])/2.0;
			double y0 = (double)(ys[i0]+ys[j0])/2.0;
//			for(int i1=i0; i1<N; i1++)FN(j1,N) {
			FN(i1,N)FN(j1,N) {
				
				
				
				
				double x1 = (double)(xs[i1]+xs[j1])/2.0;
				double y1 = (double)(ys[i1]+ys[j1])/2.0;
// 				cout<<"regador 0 en "<<i0<<"/"<<j0<<" ("<<x0<<", "<<y0<<") ";
// 				cout<<"regador 1 en "<<i1<<"/"<<j1<<" ("<<x1<<", "<<y1<<") ";
				double minr = 0;
				FN(k,N) {
					minr = max(minr, min(DS[i0][j0][k], DS[i1][j1][k]));
//					cout<<"("<<DS[i0][j0][k]<<" & "<<DS[i1][j1][k]<<")";
				}
//  				cout<<"radio min "<<minr<<endl;
				best=min(best,minr);
			}
		}
		
//		cout.precision(7);
//		cout<<"Case #"<<(test+1)<<": "<<((double)(int)(best*1000000))/1000000<<endl;
		//best=((double)(int)(best*1000000))/1000000;
		printf("Case #%d: %0.9f\n", test+1, best);
//		cout<<"exiting!"<<endl;break;
	}
	return 0;
}
// END CUT HERE 
