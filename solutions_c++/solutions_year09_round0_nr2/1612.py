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

PII delta[4]={make_pair(-1,0), make_pair(0,-1), make_pair(0,1), make_pair(1,0) };

vector<vector<int> > board;
vector<vector<int> > color;
int H,W;

bool isSink(PII p) {
	FN(i,4) {
		PII p2=p+delta[i];
		if (board[p2.first][p2.second]<board[p.first][p.second]) return false;
	}
	return true;
}
PII sinkTo(PII p) {
	int mi=1000001;
//cout<<"??"<<p<<endl;
	FN(i,4) mi=min(mi,board[p.first+delta[i].first][p.second+delta[i].second]);
	FN(i,4) { PII p2=p+delta[i]; if (mi==board[p2.first][p2.second]) return p2; }
cout<<"error";exit(1);
}
#include "stdio.h"
int main(int argc, char* argv[])
{
int T;
cin >> T;
FN(ca,T) {
	cin>>H>>W;
//cout<<"H="<<H<<" W="<<W<<endl;
	board=vector<vector<int> >(H+2, vector<int>(W+2));
	color=vector<vector<int> >(H+2, vector<int>(W+2,-1));
	FN(i,H+2) board[i][0]=board[i][W+1]=1000000;
	FN(i,W+2) board[0][i]=board[H+1][i]=1000000;
	FN(r,H) FN(c,W) cin>>board[r+1][c+1];
	vector<PII>sinks;
	FN(r,H)FN(c,W)if(isSink(make_pair(r+1,c+1))) {
		sinks.push_back(make_pair(r+1,c+1));
		color[r+1][c+1]=100;
//		cout<<"sink: "<<r<<","<<c<<endl;
	}
 	cout<<"Case #"<<(ca+1)<<":"<<endl;

/*FN(r,H){
	FN(c,W) {
	cout<<sinkTo(make_pair(r+1,c+1))<< " ";
	}
	cout<<endl;
}*/

	FN(s,sinks.size()) {
		int col=s+1;
		vector<PII> q; q.push_back(sinks[s]); color[sinks[s].first][sinks[s].second] = col;
		while (q.size()) {
			PII pos = q.back();
//cout<<"unqueue "<<pos<<", col "<<col<<endl;
			q.pop_back();
			FN(i,4) { 
				PII p2 = pos+delta[i];
				if (p2.first>0 && p2.first<=H && p2.second>0 && p2.second<=W && color[p2.first][p2.second]<0) {
					PII to=sinkTo(p2);
					if(to==pos) {
						q.push_back(p2);
//cout<<"  queue "<<p2<<", col "<<col<<endl;
						color[p2.first][p2.second]=col;
					}
				}
			}
		}
	}

	map<int,char> colormap;
	char letter='a';
	FN(r,H) {
		FN(c,W) {
			int cc=color[r+1][c+1];
			if (colormap.find(cc)==colormap.end()) {
				colormap[cc]=letter++;
			}
			cout<<colormap[cc]<<" ";
//			cout<<color[r+1][c+1]<<" ";
		}
		cout<<endl;
	}
}

	return 0;
}
// END CUT HERE 
