
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
int cas ;cin>>cas;
fup(i,1,cas){
	cout<<"Case #"<<i<<": ";
	int k ;;
	cin>>k;
	vector<int> perm;
	fup(i,1,k)perm.PB(i-1);
	string s; 
	cin>>s;
	string smaly;
	string s2; 
	int n= siz(s);
	int best=inf;
	do {	
		s2="";
		fup(i,1,n/k){
			smaly="";
			fup(v,0,k-1){
				smaly+= s[ (i-1)*k + perm[v] ];
			}
			s2+= smaly;
		}
		int ile=1;
		fup(i,1,siz(s2)-1){
			if(s2[i]!=s2[i-1])ile++;
		}
		best=min(best,ile);
	}
	while( next_permutation( perm.begin(), perm.end() ));
	cout<<best<<endl;

}




return 0;
}
