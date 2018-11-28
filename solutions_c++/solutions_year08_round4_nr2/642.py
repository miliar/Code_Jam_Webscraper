#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <stdlib.h>
#include <iostream>
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
#define EPS (1e-7)
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

int valid(int x, int X) {
if (x<0||x>X) return false;
return true;
}
int main(int argc, char* argv[])
{
int CA;
cin >> CA;
for (int ca=0; ca<CA; ca++) {
int ans = -1;
	int X,Y,A;
	cin>>X>>Y>>A;
	int rx1,rx2,ry1,ry2;
	bool found=false;
	for(int x1=0; x1<=X && !found; x1++) {
		for(int y2=0; y2<=Y && !found; y2++) { 
			for(int x2=0; x2<=X && !found; x2++) {
				for(int y1=0; y1<=Y && !found; y1++) { 
/*			int K=x1*y2-A;
	
			if (K!=0) {
				for(int x2=1; x2*x2<=abs(K) && x2<=X && !found; x2++) {
					ry1=abs(K)/x2;
					if (ry1<=Y && ry1*x2==K) {
						found=1;
						rx1=x1; rx2=x2; ry2=y2;
					}
				}
			} else {
				rx1=x1; ry2=y2; rx2=ry1=0;
			}*/
if (abs(x1*y2-x2*y1)==A) {found=1; rx1=x1;rx2=x2;ry2=y2;ry1=y1; }

}}
		}
	}
if (found && (abs(rx1*ry2-rx2*ry1) != A || !valid(rx1,X) || !valid(rx2,X) || !valid(ry1,Y) || !valid(ry2,Y))) {
cout<<"ERROR!!!";
}
	cout<<"Case #"<<ca+1<<": ";
	if (found) {
		cout<<"0 0 "<<rx1<<" "<<ry1<<" "<<rx2<<" "<<ry2<<endl;
//cout<<(A==(abs(rx1*ry2-rx2*ry1)))<<valid(rx1,X) <<valid(rx2,X) <<valid(ry1,Y) <<valid(ry2,Y);
	} else {
		cout<<"IMPOSSIBLE"<<endl;
	}
}
return 0;
}
// END CUT HERE 
