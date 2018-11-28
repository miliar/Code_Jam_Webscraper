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
#define READ(t,c) t c; cin>>c;

template<class T> ostream &operator<<(ostream &s, vector<T> v){char c='[';for(typename vector<T >::iterator i=v.begin();i!=v.end();i++){s<<c<<*i;c=',';}s<<']';return s;}
// END CUT HERE 

vector<string>board;
map<pair<int,pair<int,int> >,int > mm;

int BRD[101][101];
int MM[101][101];
int ROWS,COLS;
int f(int row, int col) {
	if (row==ROWS&&col==COLS) return 1;
	if (MM[row][col]>=0) return MM[row][col];
	int ans1=0,  ans2=0;
	if (row+1<=ROWS && col+2<=COLS && !BRD[row+1][col+2]) ans1 = f(row+1, col+2);
	if (row+2<=ROWS && col+1<=COLS && !BRD[row+2][col+1]) ans2 = f(row+2, col+1);
//cout<<"["<<row<<"]["<<col<<"] = "<<ans1+ans2<<endl;
	return MM[row][col]=(ans1+ans2)%10007;
}

int main(int argc, char* argv[])
{
READ(int,CA);
for (int ca=0; ca<CA; ca++) {
	READ(int,H);ROWS=H;
	READ(int,W);COLS=W;
	READ(int,R);
	memset(BRD,0,sizeof(BRD));
	memset(MM,-1,sizeof(BRD));
	FN(i,R) {
		READ(int,r);READ(int,c);
		BRD[r][c]=1;
	}
	int ans = f(1,1);
	cout<<"Case #"<<ca+1<<": "<<ans<<endl;
}
return 0;
}
// END CUT HERE 
