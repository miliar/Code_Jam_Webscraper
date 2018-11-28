
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
typedef long long ll;
using namespace std;

#define maxn 2005
///Zainicjowanie struktury o n elementach w roznych zbiorach to funkcja start
//findset znajduzje reprezentanta zbioru w kturym jest podany element 
//polocz laczy zbiory w kturych jes 1 i 2 argument w jeden.
//prewritten code 
struct dset{
	int przodek[maxn];
	int waga[maxn];

	void start(int n){
		fup(i,1,n){
			przodek[i]=i;
		}
	}

	int findset( int x){
		int w; 
		if(x!=przodek[x]){
			w = findset(przodek[x]);
			przodek[x]=w;			
			return w;
		}
		else return x;
	}

	void polocz( int x, int y){
		int p1, p2;
		p1= findset(x);
		p2= findset(y);
		if( p1 == p2 )return;
		if(	waga[p1] < waga[p2] )swap(p1,p2);
		przodek[p2]= p1;
		if( waga[p1]==waga[p2] )waga[p1]++;
	}
};

int P;
bool share( int x, int y){
	int xstart=x;
	for(int i=2;i*i<=xstart;i++){
		if( (x%i==0) && (y%i==0) && i>=P){  return true; }
		if( (x%i)==0) x/=i;
		if( (y%i)==0) y/=i;
	}
	if( x >1 && (y%x==0) && x>=P) return true;
	return false;
}

vector<int> rozloz( int x){
	int xstart=x;
	vector<int> w;
	for(int i=2;i*i<=xstart;i++){
		if(x%i==0) w.PB(i);
		while(x%i==0){
			x/=i;
		}
	}
	if(x>1)w.PB(x);
//	cout<<xstart<<endl;
//	debugv(w);
	return w;
}

vector<int> rozk[1055];
bool share2(int x,int y){
	REP(i,rozk[x]){
		REP(j,rozk[y]){
			if(rozk[x][i]==rozk[y][j] && rozk[y][j]>=P)return true;
		}
	}
	return false;
}

set<int> jakie;
dset zbior;
int main(){
int cas;cin>>cas;
fup(i,1,1005) rozk[i]= rozloz(i);
fup(i,1,cas){
	fup(k,0,1005){
		zbior.przodek[k]=zbior.waga[k]=0;
	}
	int a,b;
	int prz=i;
	cin>>a>>b>>P;
	zbior.start(b);

	fup(i,a,b){
		fup(j,i+1,b){
			if(share2(i,j)) {
			   	zbior.polocz(i,j);
			}
		}
	}
	fup(i,a,b){
		jakie.insert( zbior.findset(i));
	}
	cout<<"Case #"<<prz<<": "<< jakie.size() <<endl;
	jakie.clear();
}

return 0;
}
