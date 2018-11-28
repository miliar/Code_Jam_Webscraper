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

int main(){
int cas; cin>>cas;
fup(i,1,cas){
	cout<<"Case #"<<i<<": ";
	int n,m; int pole;
	int N,M;
	cin>>N>>M>>pole;
	bool sw= 0; 
/*	if( n > m ) { sw=1; swap(n,m); };
	bool jest=false;
	for(int i=1;i*i<= pole; i++) if( pole%i==0){
		int dr= pole/i;
		if( n>= i && m>= dr ){
			jest=true;
			cout<<0<<" "<<0<<" ";
			if( !sw ) cout<< i <<" "<< 0 <<" ";
			else cout<< dr <<" "<< 0 <<" ";
		
			if( !sw)cout<< 0 <<" "<< dr <<endl;
			else cout<< 0 <<" " << i <<endl;
			break;
		}
	}
	if( !jest) cout<<"IMPOSSIBLE"<<endl;			
*/
	bool jest=0;
	fup(i,0,N) fup(j,0,M){
		fup(k,0,N) fup(l,0,M){
			if( abs( i*l - j*k ) == pole && !jest){
				cout<<0<<" "<<0<<" "<<i<<" "<<j<<" "<<k<<" "<<l<<endl;
				jest=true;
				break;
			}
			if(jest)break;
		}
		if(jest)break;
	}
	if( !jest) cout<<"IMPOSSIBLE"<<endl;
}


return 0;
}
