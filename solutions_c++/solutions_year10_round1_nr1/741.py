#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define RFOR(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) RFOR(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll long long int
#define uli unsigned long long int
#define MAX (int)1e6

using namespace std;

ifstream fin ("A-large.in");
#define cin fin
ofstream fout ("A-large.out");
#define cout fout
int n,k;
char a[51][51],b[51][51];;
vs v;
void rotate() {
 REP(i,n) {
 int x;
 		string s="";
	 REP(j,n)
	  if(a[i][j]!='.') s+= a[i][j];
	 while(s.size()<n) s='.'+s;
//		 cout<<s<<endl<<endl;
	 REP(j,n) b[j][n-i-1]=s[j];
 }
 REP(i,51)REP(j,51) a[i][j]=b[i][j];
}
void hori() {
	REP(i,n)  {
		string s="";
		REP(j,n) 
		 s+=a[i][j];
		v.pb(s);
	}
	return;
}
void vert() {
	REP(j,n)  {
		string s="";
		REP(i,n) 
		 s+=a[i][j];
		v.pb(s);
	}
	return;
}
void diag1() {
	REP(i,2*n)  {
		string s="";
		if(i<n) {
			REP(j,i+1) s+=a[i-j][j];
			v.pb(s);
		}
		else {
			REP(j,2*n-i) s+=a[n-1-j][i-n+j];
			v.pb(s);
		}
	}
	return;
}
void diag2() {
	REP(i,n) REP(j,n) b[i][n-j-1]=a[i][j];
	REP(i,2*n)  {
		string s="";
		if(i<n) {
			REP(j,i+1) s+=b[i-j][j];
			v.pb(s);
		}
		else {
			REP(j,2*n-i) s+=b[n-1-j][i-n+j];
			v.pb(s);
		}
	}
	return;
}

int main() {
	int t=0;
	cin>>t;
	REP(T,t) {
		v.clear();
		cin>>n>>k;
		REP(i,n) cin>>a[i];
		//REP(i,n){ REP(j,n) cout<<a[i][j];cout<<endl;}
		//cout<<endl;
		rotate();
		//REP(i,n){ REP(j,n) cout<<a[i][j];cout<<endl;}
		//cout<<endl;
		hori();
		vert();
		diag1();
		diag2();
		string R="",B="";
		REP(i,k) R+='R',B+='B';
		bool rfound=false,bfound=false;
		REP(i,v.size()) if(v[i].find(R)!=string::npos) rfound=true;
		REP(i,v.size()) if(v[i].find(B)!=string::npos) bfound=true;
		if(rfound && bfound) cout<<"Case #"<<T+1<<": Both"<<endl;
		else if(rfound) cout<<"Case #"<<T+1<<": Red"<<endl;	
		else if(bfound) cout<<"Case #"<<T+1<<": Blue"<<endl;	
		else cout<<"Case #"<<T+1<<": Neither"<<endl;
		//cout<<"Case #"<<T+1<<": "<< <<endl;
	}
	return 0;
}
