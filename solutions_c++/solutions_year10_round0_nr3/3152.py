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

#define FOR(i,a,b) for ( int i = a; i <= b ; i ++ )
#define REV(i,a,b) for ( int i = a; i >= b ; i -- )
#define FRV(i,v) FOR(i,0,v.sz-1)

#define vi vector <int>
#define vs vector <string>

#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define RL(v,n) rotate(v.begin(),v.begin()+n,v.end())
#define RR(v,n) rotate(v.begin(),v.end()-n,v.end())

using namespace std;

void main (){
	string rname = "files/C-small-attempt2.in";
	string oname = "files/C-small-attempt2.out";
	//string rname = "files/test.in";
	//string oname = "files/test.out";

	RFILE(rf,rname.c_str());
	WFILE(wf,oname.c_str());

	int T;
	rf>>T;

	FOR(i,1,T){
		int R,k,N;

		rf>>R>>k>>N;

		vi gs;
		FOR(j,1,N){
			int g;
			rf>>g; gs.pb(g);
		}

		vi loop_in(N,0);
		vi rounds;

		int index = 0;

		while ( !loop_in[index] ){
			loop_in[index] = rounds.sz+1;

			int sum_index = index;
			int sum = 0;

			do{
				if ( sum + gs[sum_index] > k ) {break;}
				sum += gs[sum_index++];
				sum_index %= N ;
			}while (sum_index != index );

			rounds.pb(sum);
			index = sum_index;
		}

		int diff = loop_in[index] - 1;
		int rs = rounds.sz - diff;
		R -= diff;
		int crounds = R/rs;

		rs = R % rs;

		unsigned int nrsum = 0 ;
		unsigned int crsum = 0 ;
		unsigned int prsum = 0 ;

		FRV(l,rounds){
			if ( l < diff ) nrsum += rounds[l];
			else {
				if ( l < rs + diff ) prsum += rounds[l];
				crsum += rounds[l];
			}
		}

		unsigned int result = nrsum + crsum * crounds + prsum;
		stringstream ss;
		ss << "Case #"<<i<<": "<<result<<endl;
		cout << ss.str() ;
		wf << ss.str();
	}

	wf.close();
	rf.close();
}