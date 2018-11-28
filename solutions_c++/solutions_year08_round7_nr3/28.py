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
/*vector<string> tokens(const string &str, const string &delims){
	char *buf = strdup(str.c_str()), *token;
	const char *dels = delims.c_str();
	vector<string> v;
	token = strtok( buf, dels );
	while (token) {	v.push_back(token);	token = strtok(NULL, dels);	}
	free(buf);
	return v;
}*/
#define erase_unique(v)     (v).erase(unique(all(v)),v.end())  
#define erase_remove(v,val) (v).erase(remove(all(v),(val)),v.end()) 

template<class T> ostream &operator<<(ostream &s, vector<T> v){char c='[';for(typename vector<T >::iterator i=v.begin();i!=v.end();i++){s<<c<<*i;c=',';}s<<']';return s;}
// END CUT HERE 

vector<vector<int> > recipes;
vector<int> MM;

int f(int mix) {
	if (MM[mix]>=0) return MM[mix];
	vector<int> sub;
	FN(i,SZ(recipes[mix])) {
		sub.push_back(f(recipes[mix][i]));
	}
	if (!SZ(sub)) { 
//		cout<<"prepare "<<mix<<": trivial, =1"<<endl;
		return MM[mix]=1; 
	}
	sort(sub.rbegin(),sub.rend());
	int K=SZ(sub);
	int need=sub[0],have=sub[0]-1;
	for (int i=1; i<K; i++) {
		if (sub[i]>have) {
			int d=sub[i]-have;
			need+=d;
			have+=d;
			
		}
		have--;
	}
	if (!have) need++;
//	cout<<"to prepare "<<mix<<" I need (including)"<<need<<endl;
	return MM[mix]=need;
}

vector<vector<double> > qs;
vector<double> probs;
int Q;
void gen(int from, double acc) {
	if (from==Q) {
		probs.push_back(acc);
	} else {
		FN(i,4) {
			gen(from+1, qs[from][i]*acc);
		}
	}
}
int main(int argc, char* argv[])
{
	int CA;
	cin >> CA;
	for (int ca=0; ca<CA; ca++) {
		int M;
		cin>>M>>Q;
		qs.clear(); probs.clear();
		FN(q,Q) {
			qs.push_back(vector<double>());
			FN(i,4) {
				double p; cin>>p;
				qs[q].push_back(p);
//cout<<"("<<p<<")";
			}
		}
//cout<<endl;
		gen(0,1.0);
		//cout<<" there are "<<SZ(probs)<<endl;
		double sum=0;
		FN(i,SZ(probs)) {
			sum+=probs[i];
		//	cout<<probs[i]<<" ";
		}
//		cout<<"["<<sum<<"]";
		sort(probs.rbegin(),probs.rend());
		double pp=0;
		int QQ=SZ(probs)<M ? SZ(probs) : M;
		FN(i,QQ) {
			pp+=probs[i];
		}
		cout<<"Case #"<<ca+1<<": "<<pp<<endl;
	}
	return 0;
}
// END CUT HERE 
