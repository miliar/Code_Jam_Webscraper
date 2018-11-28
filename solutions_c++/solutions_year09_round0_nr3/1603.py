#include <vector>
#include <list>
#include <cstring>
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
PII operator+(PII a, PII b) { return make_pair(a.first+b.first, a.second+b.second); }
// END CUT HERE 

int dp[20][501]; // 
// f(it,ip) = if (text[it]==ip[ip]) then f(it+1,ip+1)   ++ f(it+1,ip+1)

#include "stdio.h"
int main(int argc, char* argv[])
{
char s[510];
cin.getline(s,510);
int T;
sscanf(s, "%d", &T);
string pattern="welcome to code jam";
//   "elcomew elcome to code jam..."
//m: [    3       2            1   ]
//am:[                        1    ]

//           "wweellccoommee to$"
//           [111111111111111110]
//          e[33332222222221...0]
//         me[444444444442     0]
//        ome[8888888884       0]
//       come[     168         0]
//      lcome[                 0]
//     elcome[                 0]
//    welcome[                 0]

int M=pattern.size();
FN(ca,T) {
	char text[510];
	cin.getline(text,510);

	int prev[510],cur[510];
	int N=strlen(text);
	FN(i,N)prev[i]=1;

	for (int j=M-1; j>=0; j--) {
		char c = pattern[j];
		cur[N]=0;
		for (int i=N-1; i>=0; i--) {
			cur[i]=cur[i+1];
			if (c==text[i]) {
//				cout<<"text["<<i<<"]==pattern["<<j<<"]=="<<c<<endl;
				cur[i]=(cur[i]+prev[i])%1000; //MODULO
			}
		}

//		FN(j,M+1)cout<<cur[j]<<" ";cout<<endl;
		memcpy(prev,cur,sizeof(cur));
	}
	char s[100];
	sprintf(s, "Case #%d: %04d\n", ca+1, cur[0]);
	cout<<s;
}
	return 0;
}
// END CUT HERE 
