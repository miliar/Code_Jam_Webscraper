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
		int a=1;
		rep(i,N) a*=2;
		cout<<"Case #"<<iCase<<": ";
		cout<<(a-1==K || (K+1)%a==0?"ON":"OFF")<<endl;
	}
	
	return 0;
}
