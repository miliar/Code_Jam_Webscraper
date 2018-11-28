#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<fstream>
#include<algorithm>

#define RFILE(fp,name) ifstream fp(name); if (!fp) {cout<<"Error in file "<<name; return;}
#define WFILE(fp,name) ofstream fp(name); if (!fp) {cout<<"Error in file "<<name; return;}

#define sz size()
#define pb push_back
#define ll unsigned long int

#define FOR(i,a,b) for ( ll i = a; i <= b ; i ++ )
#define REV(i,a,b) for ( ll i = a; i >= b ; i -- )
#define FRV(i,v) FOR(i,0,v.sz-1)

#define vi vector <int>
#define vs vector <string>
#define vll vector <ll>


#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define RL(v,n) rotate(v.begin(),v.begin()+n,v.end())
#define RR(v,n) rotate(v.begin(),v.end()-n,v.end())

using namespace std;

void main (){
	string rname = "files/A-large.in";
	string oname = "files/A-large.out";

	//string rname = "files/test.in";
	//string oname = "files/test.out";

	RFILE(rf,rname.c_str());
	WFILE(wf,oname.c_str());

	int C;
	rf>>C;

	FOR(c,1,C){
		int N;
		rf >> N;
		vi ms;

		vi v1s;
		vi v2s;

		FOR(i,1,N){
			int v1,v2;
			rf>>v1>>v2;
			v1s.pb(v1);
			v2s.pb(v2);
			ms.pb(v2-v1);
		}
		//SORT(ms);
		int res = 0;
		FRV(j,ms){
			FOR(k,j+1,ms.sz -1 ){
				if ( ms[j] != ms[k] ){
					int d1 = v1s[j] - v1s[k] ;
					int d2 = v2s[j] - v2s[k] ;
					if ( (d1 > 0 && d2 < 0 ) || ( d1<0 && d2 > 0 ) )
						res ++;
				}
			}
		}

		stringstream ss;
		ss << "Case #"<<c<<": "<<res<<endl;
		cout << ss.str() ;
		wf << ss.str();
	}
	wf.close();
	rf.close();
}
