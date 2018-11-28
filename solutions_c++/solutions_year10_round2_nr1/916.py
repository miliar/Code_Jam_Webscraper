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
		int N,M;
		rf>>N>>M;

		vs list;

		FOR(i,1,N){
			string line;
			rf>>line;
			int idx = 0;
			string dr ="";

			while ( idx < line.size()){
				dr = line.substr(0,idx+1);
				idx ++;
				if ( line [idx] == '/' ){
					list.push_back(dr);
				}
			}
			list.push_back(dr);
		}

		int res = 0;

		FOR(j,1,M){
			string line="";
			rf>>line;
			int idx = 0;
			string dr ="";

			while ( idx < line.size()){
				dr = line.substr(0,idx+1);
				idx++;

				if ( line [idx] == '/' ){
					if ( find(ALL(list),dr) == list.end() ){ list.push_back(dr);res++;}
				}
			}
			if ( find(ALL(list),dr) == list.end() ){ list.push_back(dr);res++;}
		}

		stringstream ss;
		ss << "Case #"<<c<<": "<<res<<endl;
		cout << ss.str() ;
		wf << ss.str();
	}
	wf.close();
	rf.close();
}
