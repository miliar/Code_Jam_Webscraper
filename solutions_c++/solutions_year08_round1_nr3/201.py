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


/* output generated with: 
#!/bin/bash
for I in `seq 1 30`; do
#echo -n "$I="
echo "scale=1000; print "x"; (3+sqrt(5))^$I" | bc | grep "\\." | sed s/\\..*
//g | sed "s/\\(.*\\)/\"\\1\",/g"
done;

*/

char * data[] =
{
"001",
"005",
"027",
"0143",
"0751",
"03935",
"020607",
"0107903",
"0564991",
"02958335",
"015490047",
"081106943",
"0424681471",
"02223661055",
"011643240447",
"060964798463",
"0319215828991",
"01671435780095",
"08751751364607",
"045824765067263",
"0239941584945151",
"01256350449401855",
"06578336356630527",
"034444616342175743",
"0180354352626532351",
"0944347650390491135",
"04944668491836817407",
"025890620349458939903",
"0135565048129406369791",
"0709827807378602459135",
"03716706651753989275647"
};

int main(int argc, char* argv[])
{
	int T;
	cin >> T;
	for (int ca=0; ca<T; ca++) {
		int p;	cin>>p;
		string s= data[p];
		s=s.substr(s.size()-3,3);
		cout<<"Case #"<<ca+1<<": "<<s<<endl;
	}
	return 0;
}
// END CUT HERE 
