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
// END CUT HERE 



#include "stdio.h"
int main(int argc, char* argv[])
{
int L,D,N;
cin >> L >> D>> N;
vector<string> words(D);
vector<vector<vector<int> > > letters(L, vector<vector<int> >(26));//[step][char]
FN(i,D)  {
	cin>>words[i];
	FN(j,L) letters[j][words[i][j]-'a'].push_back(i);
}
FN(i,N) {
	string pat;
	cin>>pat;
//	cout<<"pat:"<<pat<<endl;
	vector<int> B(D,0);
	int p=0;
	vector<string> pattern(L);
	for (int j=0; j<L; j++) {
		string ls;
		if (pat[p]=='(') {
			ls = pat.substr(p+1, pat.find(')',p)-p-1);
			p=pat.find(')',p)+1;
		} else {
		 	ls=pat[p];
			p++;
		}
		pattern[j]=ls;
	}
	int K=0;
	for (int w=0; w<D; w++) {
		int l;
		for (l=0; l<L && pattern[l].find(words[w][l])!=string::npos; l++) ;
		if (l==L) {
			//cout<<"can be "<<words[w]<<endl; 
			K++;
		}
	}
 	cout<<"Case #"<<(i+1)<<": "<<K<<endl;
}

/*	ib=din.size(); ob=dout.size();
	FN(i,ib) {
		iv[din[i]] = i;
	}
	int x=0;
	FN(i,alien.size()) {
		x=x*ib+iv[alien[i]];
	}
	int X=x;
	char buf[1000];
	buf[999]=0;
	char *k=buf+999;
	do {
		*--k = dout[x%ob];
		x/=ob;
	} while (x);*/
//cout<<"in:"<<alien<<" (din="<<din<<", dout="<<dout<<"), x="<<X<<", out="<<k<<endl;

	return 0;
}
// END CUT HERE 
