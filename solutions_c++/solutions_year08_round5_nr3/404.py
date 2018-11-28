
#include<algorithm>
#include<bitset>
#include<iostream>
#include<string>
#include<cstdio>
#include<sstream>
#include<vector>
#include<stack>
#include<deque>
#include<map>
#include<iterator>
#include<cmath>
#include<complex>
#include<queue>
#include <ext/hash_map>
#include<cassert>
#include<set>

#define FOREACH(it ,c ) for( typeof((c).begin()) it= (c).begin();it!=(c).end();++it) 
#define debug(x) cerr<< #x << " = " << x << "\n";
#define debugv(x) cerr<< #x << " = " ; FOREACH(it,(x)) cerr << *it << "," ; cerr<< "\n" ;
#define MP make_pair
#define PB push_back
#define siz(w) (int)w.size()
#define fup(i,st,ko) for(int i=st;i<=ko;i++)
#define fdo(i,st,ko) for(int i=st;i>=ko;i--)
#define REP(i,w) for(int i=0;i<siz(w);i++)
#define inf 100000000
//__gnu_cxx::hash_map< int ,int> best;
typedef long long ll;
using namespace std;
bool bad[15][15];
int Y,X;
int dp[ (1<<12) ][ 12 ];
bool good( bitset<10> a ){
	fup(i,1,10){ if(a[i] && a[i-1]) return false; }
	return true;
}


bool dwad( bitset<10> a , bitset<10> b ){
	if( !good(b) ) return false;
	REP(i,b ){
		fup(j,-1,1){
			if(j==0) continue;
			if( i+j>=0 && i+j< X && a[i+j] && b[i]) return false;
		}
	}
	return true;
}

bool nazlam( bitset<10> a , int pp ){
	REP(i,a){
		if(a[i] && bad[pp][i]) return true;
	}
	return false;
}

int solve( bitset<10> a , int poz ){
	if( nazlam( a, poz) ) return 0;
	if( poz==Y-1 ){
		if( good(a ))return a.count();
		else return 0;
	}		
	int num = a.to_ulong();
	if( dp[num][poz]!=-1 ) return dp[num][poz];
	int w=0;
	fup(i,0,(1<<X)-1){
		bitset<10> b = i;
		if( dwad(a,b) ) w=max(w, solve( b, poz+1 ) );
	}
	dp[num][poz]= a.count()+w;
	return a.count()+ w;
}

int main(){
int cas;cin>>cas;
fup(vv,1,cas){
cin>>Y>>X;
fup(i,0,11) fup(j,0,11) bad[i][j]=false;

fup(i,0,Y-1){
	string s; cin>>s;
	REP(j,s){
		if(s[j]=='x') bad[i][j]=true;
	}
}

memset(dp,-1,sizeof(dp));
int w=0;
fup(i,0,(1<<X)-1){
	bitset<10> a= i;
	if( nazlam(a,0))continue;
	if( !good(a)) continue;
	w= max(w, solve(a,0));
}
cout<< "Case #"<<vv<<": "<<w<<endl;

}


return 0;
}
