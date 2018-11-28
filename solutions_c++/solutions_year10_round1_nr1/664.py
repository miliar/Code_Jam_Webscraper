#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cassert>

using namespace std;

#define allof(c) ((c).begin()),((c).end())
#define debug(c) cerr<<"> "<<#c<<" = "<<(c)<<endl;
#define iter(c) __typeof((c).begin())
#define tr(i,c) for(iter(c) i=(c).begin();i!=(c).end();i++)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define REP(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define mp make_pair
#define fst first
#define snd second
#define pb push_back

typedef vector<int> vi;


int main(){
	int nCases; cin>>nCases;
	for(int iCase=1;iCase<=nCases;iCase++){
		int N,K; cin>>N>>K;
		vector<string> im(N),rm(N);
		rep(i,N) cin>>im[i];
		rep(i,N) rep(j,N) rm[i]+=im[N-j-1][i];
		rep(i,N){
			int sp=0;
			rep(j,N) if(rm[N-j-1][i]!='.') swap(rm[N-j-1][i],rm[N-1-sp++][i]);
		}
		bool rr=false,rb=false;
		rep(i,N) rep(j,N){
			int rh=0,bh=0,rv=0,bv=0,rs=0,bs=0,rss=0,bss=0;
			rep(k,K){
				if(j+k<N && rm[i][j+k]=='R') rh++;
				if(j+k<N && rm[i][j+k]=='B') bh++;
				if(i+k<N && rm[i+k][j]=='R') rv++;
				if(i+k<N && rm[i+k][j]=='B') bv++;
				if(i+k<N && j+k<N && rm[i+k][j+k]=='R') rs++;
				if(i+k<N && j+k<N && rm[i+k][j+k]=='B') bs++;
				if(i-k>=0 && j+k<N && rm[i-k][j+k]=='R') rss++;
				if(i-k>=0 && j+k<N && rm[i-k][j+k]=='B') bss++;
			}
			rr|=(rh==K)|(rv==K)|(rs==K)|(rss==K);
			rb|=(bh==K)|(bv==K)|(bs==K)|(bss==K);
		}
		cout<<"Case #"<<iCase<<": ";
		if(!rr && !rb) cout<<"Neither";
		if(rr && rb) cout<<"Both";
		if(rr && !rb) cout<<"Red";
		if(!rr && rb) cout<<"Blue";
		cout<<endl;
	}
	
	return 0;
}
