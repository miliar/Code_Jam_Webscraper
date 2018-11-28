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

int dr[]={-1,-1,-1,0,0,1,1,1};
int dc[]={-1,0,1,-1,1,-1,0,1};

map<pair<pair<int,int>,string> ,bool> mm;

int R,C;
int pos(int r,int c) {
	return r*C+c;
}
bool win(int r,int c,string board) {
	 pair<pair<int,int>,string> key=make_pair(make_pair(r,c),board);
	 if (mm.find(key)!=mm.end()) return mm[key];
	 if (board.size()!=R*C){ 
//cout<<"?";
	 }
	 int moves=0;
	 for(int i=0; i<8; i++) {
		 if (r+dr[i]>=0 && r+dr[i]<R && c+dc[i]>=0 && c+dc[i]<C) {
			 int next=pos(r+dr[i],c+dc[i]);
			 if (next>=R*C) {
				 cout<<r<<" "<<c<<" "<<dr[i]<<" "<<dc[i]<<" "<<i;
			 }
			 if (board[next]=='.') {
				 moves++;
				 string board2=board;
				 board2[next]='#';
				 if (!win(r+dr[i],c+dc[i],board2)) {
// cout<<"win("<<r<<","<<c<<",'"<<board<<") = true)"<<endl;;
					 return mm[key]=true;
				 }
			 }
		 }
	 }
//cout<<"win("<<r<<","<<c<<",'"<<board<<") = false)"<<endl;
	return mm[key]=false;
}
int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	for (int ca=0; ca<N; ca++) {
		mm.clear();
		cin>>R>>C;
		string board,s;
		int sr=-1,sc=-1;
		FN(r,R){ 
			cin>>s;
			board+=s;
			FN(c,C)if (s[c]=='K') { sr=r; sc=c; }
		}
		board[pos(sr,sc)]='#';
		//cout<<"board: "<<board<<" start: "<<sr<<","<<sc<<endl;
		bool bwin=win(sr,sc,board);
		cout<<"Case #"<<ca+1<<": "<<(bwin?'A':'B')<<endl;
	}
	return 0;
}
// END CUT HERE 
