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

int main(int argc, char* argv[])
{
	int CA;
	cin >> CA;
	for (int ca=0; ca<CA; ca++) {
		vector<string> names;
		int N; cin>>N;
		vector<vector<string> > sings;
		FN(i,N) {
			string s; cin>>s;names.push_back(s);
			sings.push_back(vector<string>());
			int M; cin>>M;
//	cout<<" prepare "<<s<<" with "<<M<<":";
			FN(j,M) {
				cin>>s;
				if (s[0]>='A' && s[0]<='Z') {
					sings[i].push_back(s);
//	cout<<" [+"<<s<<"]";
				} else {
//	cout<<" [["<<s<<"]]";
				}
			}
		}

		recipes.clear();recipes.resize(N);
		MM.clear();MM.resize(N,-1);
		FN(i,N) {
			FN(j,SZ(sings[i])) {
				recipes[i].push_back(find(names.begin(),names.end(),sings[i][j])-names.begin());
			}
	//		cout<<"[ "<<i<<" NEEDS: "<<recipes[i]<<endl;
		}
		
		int cnt = f(0);
		cout<<"Case #"<<ca+1<<": "<<cnt<<endl;
	}
	return 0;
}
// END CUT HERE 
