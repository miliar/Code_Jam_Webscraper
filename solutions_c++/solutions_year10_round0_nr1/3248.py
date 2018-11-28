#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<fstream>

#define RFILE(fp,name) ifstream fp(name); if (!fp) {cout<<"Error in file "<<name; return;}
#define WFILE(fp,name) ofstream fp(name); if (!fp) {cout<<"Error in file "<<name; return;}

#define sz size()
#define pb push_back

#define FOR(i,a,b) for ( int i = a; i <= b ; i ++ )
#define REV(i,a,b) for ( int i = a; i >= b ; i -- )
#define FRV(i,v) FOR(i,0,v.sz-1)

#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))

using namespace std;

void main (){
	string rname = "files/A-large.in";
	string oname = "files/A-large.out";

	RFILE(rf,rname.c_str());
	WFILE(wf,oname.c_str());

	int T;
	rf>>T;

	FOR(i,1,T){
		int N,K;
		rf >> N >> K;

		int res = 0;
		FOR(j,1,N){
			res = K%2;
			if (!res ) break;
			K /= 2;
		}
		string r = res ? "ON":"OFF";

		stringstream ss;
		ss << "Case #"<<i<<": "<<r<<endl;
		cout << ss.str() ;
		wf << ss.str();
	}

	wf.close();
	rf.close();
}