
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
#define maxn 100005
int w[maxn];
bool change[maxn];
int ile[maxn][3];
int n; 
int vv;
int main(){
int cas; cin>>cas;
fup(v,1,cas){
	cout<<"Case #"<<v<<": ";
	cin>>n>>vv; 
	fup(i,1,(n-1)/2){
		cin>>w[i]>>change[i];
	}
	int kt= (n-1)/2 +1;
	fup(i,1,(n+1)/2){
		int x;cin>>x;
		if(x==1){
			ile[kt][1]=0;
			ile[kt][0]=inf;
		}	
		else{
			ile[kt][1]=inf;
			ile[kt][0]=0;
		}
		kt++;
	}
	
	fdo(i,(n-1)/2,1){
		int l,p; 
		l=i*2;
		p=i*2+1;
		int ile10 =  min ( ile[l][0]+ile[p][1], ile[l][1]+ile[p][0]);
		int ile11= ile[l][1]+ile[p][1];
		int ile00= ile[l][0]+ile[p][0];
		int iand=0;
		int ior=0;
		if( w[i]==0 ){
			if(change[i]) iand=1;
			else iand= inf;
		}
		if( w[i]==1 ){
			if(change[i]) ior=1;
			else ior= inf;
		}
		ile[i][1]= min(ior+ile10 , ior+ile11 );
		ile[i][1]= min(ile[i][1] , iand+ ile11 );
		
		ile[i][0]= min(iand+ ile10 , iand+ ile00 );
		ile[i][0]= min(ile[i][0] , ior+ ile00 );
		if(ile[i][0]>inf) ile[i][0]=inf;
		if(ile[i][1]>inf) ile[i][1]=inf;
	}

	int wyn= ile[1][vv];
	if(wyn==inf) cout<<"IMPOSSIBLE"<<endl;
	else cout<<ile[1][vv]<<endl;

	fup(i,1,n){
		ile[i][0]=ile[i][1]=0;
		w[i]=0;
		change[i]=0;
	}

}


return 0;
}
