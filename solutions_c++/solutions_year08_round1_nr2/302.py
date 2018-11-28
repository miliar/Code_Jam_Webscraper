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


int main(int argc, char* argv[])
{
	int T;
	cin >> T;
	for (int ca=0; ca<T; ca++) {
		int FL,CLI;
		cin >> FL >> CLI;
		vector<vector<int> > likes(CLI);
		vector<vector<int> > likesM(CLI);
		FN(c,CLI) {
			int t; cin>>t;
			likes[c] = vector<int>(t);
			likesM[c] = vector<int>(t);
			FN(f,t) { cin >> likes[c][f] >> likesM[c][f];
				likes[c][f]--;
//cout<<"customer "<<c<<" likes "<<likes[c][f]<< "+"<<likesM[c][f]<<endl;
			}
		}

		int best=12345;
		int bestM=-1;
		FN(mask,1<<10) {
			bool error = false;
			FN(c,CLI) {
				bool sat=false;	
				int t = SZ(likes[c]);
				int i=0; 
				while (i<t && !sat) {
					int fl = likes[c][i];	
					int malted = (mask&(1<<fl));
					sat = likesM[c][i] ? malted!=0 : malted==0;
					i++;
				}
				if (!sat) {
					error = true;
					break;
				}
			}
			if (!error) {
				int bi=0,k=mask;
				while(k) { bi+=k&1; k>>=1; }
				if (bi<best)  { bestM = mask; best=bi; }
			}
		}

		if (best==12345) 
		cout<<"Case #"<<ca+1<<": IMPOSSIBLE"<<endl;
		else {
			cout<<"Case #"<<ca+1<<":";
			FN(i,FL) {
				cout<<" "<<(bestM&1);
				bestM>>=1;
			}
			cout<<endl;
		}
	}
	return 0;
}
// END CUT HERE 
