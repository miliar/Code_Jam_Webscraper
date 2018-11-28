
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
#include<stack>
#include<cassert>

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
typedef long long ll;
using namespace std;
#define maxn 100005
ll t[5][5];
ll X[maxn];
ll Y[maxn];
int n;

int main(){
int cas;cin>>cas;
fup(i,1,cas){
	int prz=i;
	ll x0,y0; 
	cin>>n;
	ll a,b,c,d; ll mod;
	cin>>a>>b>>c>>d>>x0>>y0>>mod;
	X[1]=x0;	
	Y[1]=y0;
	ll x= x0; 
	ll y= y0;
	fup(i,2,n){
	 	x= (a*x+b)%mod;
		y= (c*y+d)%mod;
		X[i]=x;
		Y[i]=y;
	}
	
	fup(i,1,n){
	 	ll modx= X[i]%3;
		ll mody= Y[i]%3;
		t[modx][mody]++;
	}
	ll w=0;
	fup(a,0,2) fup(b,0,2)
		fup(c,0,2) fup(d,0,2)
			fup(e,0,2) fup(g,0,2){
				if((a+c+e)%3!=0)continue;
				if((b+d+g)%3!=0)continue;
				pair<ll,ll> p1,p2,p3;
				p1=MP(a,b);
				p2=MP(c,d);
				p3=MP(e,g);
				ll ile1= t[p1.first][p1.second];
				ll ile2= t[p2.first][p2.second];
				ll ile3= t[p3.first][p3.second];

				if( p1==p2 && p2==p3 ){
					if(t[p1.first][p1.second]>=3){
						w+= ile1*(ile1-1)*(ile1-2) ;	
					}		
				}
				else {
					if( p1==p3 && ile1>0) { w+= ile1*(ile1-1) * ile2; }
					if( p1==p2 && ile1>0) w+= ile1*(ile1-1) * ile3;
					if( p2==p3 && ile2>0) w+= ile2*(ile2-1) * ile1;
					
					if(p1!=p3 && p1!=p2 && p2!=p3 ) w+= ile1*ile2*ile3;
				}
			}

	cout<<"Case #"<<prz<<": "<<w/6<<endl;
	fup(a,0,3) fup(b,0,3) t[a][b]=0;

}


return 0;
}
