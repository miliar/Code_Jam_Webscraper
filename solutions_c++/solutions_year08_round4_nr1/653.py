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

int mm[10001][2]; // [nodeix][toVal]

int fminor(int node, int val) {
	int l=((node+1)*2)-1, r=((node+1)*2)+1-1;
	int chl,chr;
	if (!val) { // must be 0
		chl=mm[l][0], chr=mm[r][0];
		if (chl<0 || chr<0) return -1;
		return chl+chr;
	} else {
		int chl1=mm[l][1], chr1=mm[r][1];
		int chl0=mm[l][0], chr0=mm[r][0];
		int best = -1;
		if (chl1>=0 && chr0>=0 && (best<0 || chl1+chr0<best)) best = chl1+chr0;
		if (chl0>=0 && chr1>=0 && (best<0 || chl0+chr1<best)) best = chl0+chr1;
		if (chl1>=0 && chr1>=0 && (best<0 || chl1+chr1<best)) best = chl1+chr1;
		return best;
	}
}
int fminand(int node, int val) {
	int l=((node+1)*2)-1, r=((node+1)*2)+1-1;
	if (val) { // must be 1
		int chl=mm[l][1], chr=mm[r][1];
		if (chl<0 || chr<0) return -1;
		return chl+chr;
	} else {
		int chl1=mm[l][1], chr1=mm[r][1];
		int chl0=mm[l][0], chr0=mm[r][0];
		int best = -1;
		if (chl1>=0 && chr0>=0 && (best<0 || chl1+chr0<best)) best = chl1+chr0;
		if (chl0>=0 && chr1>=0 && (best<0 || chl0+chr1<best)) best = chl0+chr1;
		if (chl0>=0 && chr0>=0 && (best<0 || chl0+chr0<best)) best = chl0+chr0;
		return best;
	}
}

int main(int argc, char* argv[])
{
int CA;
cin >> CA;
for (int ca=0; ca<CA; ca++) {
int ans = -1;
	int M,V;
	cin>>M>>V;
	int nodes=(M-1)/2, leaves=(M+1)/2;
	vector<int> OPS(nodes); // 1: and, 0=or
	vector<int> CHG(nodes); // 1: can change
	vector<int> VALS(M);
	FN(i,nodes) cin>>OPS[i]>>CHG[i];
	FN(i, leaves) cin>>VALS[nodes+i];

	for(int node=M-1; node>=0; node--) {
		if (node>=nodes) { // leaf
			mm[node][VALS[node]] = 0;
			mm[node][1-VALS[node]] = -1;
//cout<<"Leaf #"<<node<<"  {"<<VALS[node]<<"} [0]="<<mm[node][0]<<"  [1]="<<mm[node][1]<<endl;
		} else { // op
			FN(v,2) {
				int best;
				if (OPS[node]) { // and
					best = fminand(node, v);
					if (CHG[node]) {
						int b2=fminor(node, v);
						if (b2>=0 && (best<0 || best>1+b2)) best=1+b2;
					}
				} else {
					best = fminor(node, v);
					if (CHG[node]) {
						int b2=fminand(node, v);
						if (b2>=0 && (best<0 || best>1+b2)) best=1+b2;
					}
				}
				mm[node][v] = best;
			}
//cout<<"Node "<<node<<" op="<<OPS[node]<<" chg="<<CHG[node]<<"  [0]="<<mm[node][0]<<"  [1]="<<mm[node][1]<<endl;
		}
	}
	cout<<"Case #"<<ca+1<<": ";
	if (mm[0][V]>=0) {
		cout<<mm[0][V]<<endl;
	} else {
		cout<<"IMPOSSIBLE"<<endl;
	}
}
return 0;
}
// END CUT HERE 
