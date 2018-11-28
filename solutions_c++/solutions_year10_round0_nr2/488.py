#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list> 
using namespace std; 

#define PB push_back 
#define MP make_pair 
#define SZ(v) ((int)(v).size()) 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) REP(i,SZ(v)) 
typedef long long ll; 

char buff[100];

string mydiff(const string &a,const string &b) {
	ll A,B; sscanf(a.c_str(),"%lld",&A); sscanf(b.c_str(),"%lld",&B);
	ll ret=A-B; if(ret<0) ret=-ret;
	sprintf(buff,"%lld",ret); return buff;
}

string mygcd(const string &a,const string &b) {
	ll A,B; if(SZ(a)==0) A=0; else sscanf(a.c_str(),"%lld",&A); if(SZ(b)==0) B=0; else sscanf(b.c_str(),"%lld",&B);
	ll ret=__gcd(A,B);
	sprintf(buff,"%lld",ret); return ret==0?"":buff;
}

string mymod(const string &a,const string &b) {
	ll A,B; if(SZ(a)==0) A=0; else sscanf(a.c_str(),"%lld",&A); if(SZ(b)==0) B=0; else sscanf(b.c_str(),"%lld",&B);
	ll ret=A%B;
	sprintf(buff,"%lld",ret); return ret==0?"":buff;
}

string mysub(const string &a,const string &b) {
	ll A,B; if(SZ(a)==0) A=0; else sscanf(a.c_str(),"%lld",&A); if(SZ(b)==0) B=0; else sscanf(b.c_str(),"%lld",&B);
	ll ret=A-B;
	sprintf(buff,"%lld",ret); return ret==0?"":buff;
}


void run(int casenr) {
	int n; scanf("%d",&n);
	vector<string> t(n); REP(i,n) { scanf("%s",buff); t[i]=buff; }
	sort(t.begin(),t.end()); t.erase(unique(t.begin(),t.end()),t.end());
	string T=mydiff(t[0],t[1]);
	FORSZ(i,2,t) T=mygcd(T,mydiff(t[0],t[2]));
	string x=mymod(t[0],T);
//	printf("T=%s x=%s\n",T.c_str(),x.c_str());
	string ret;
	if(SZ(x)==0) ret="0"; else ret=mysub(T,x);
	printf("Case #%d: %s\n",casenr,ret.c_str());
}

int main() {
	int ncases; scanf("%d",&ncases); FORE(i,1,ncases) run(i);
	return 0;
}

