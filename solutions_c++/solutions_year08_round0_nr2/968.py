
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

struct zd{
	bool odjazd; 
	int czas;
	bool A ;
	int li;
	zd(){ odjazd=0; czas=0;A=0; }
	zd(bool odj, int cz, bool a,int num){ 
		odjazd= odj;
		czas= cz;
		A=a;
		li=num;
	}
};

bool operator<(const zd&l,const zd&r){
	if(l.czas==r.czas){
		if(l.odjazd==r.odjazd)return l.li > r.li;    
		return l.odjazd > r.odjazd;
	}
	return l.czas > r.czas ;
}

int change( string s){
	stringstream pp;
	REP(i,s) if(s[i]==':')s[i]=' ';
	pp<<s;
	int d,m; 
	pp>>d>>m;
	return d*60+m;
}

priority_queue< zd > kol;

int main(){
int cas; cin>>cas;
fup(i,1,cas){
	int num=0;
	int przypadek=i;
	int dol; cin>>dol;
	int A,B;
   	cin>>A>>B;
	fup(i,1,A){
		string st,ko; 
		cin>>st>>ko;	
		kol.push( zd(1,change(st),1,++num) );
		kol.push( zd(0,change(ko)+dol,0,++num) );
	}	
	fup(i,1,B){
		string st,ko;
		cin>>st>>ko;
		kol.push( zd(1,change(st),0,++num) );
		kol.push( zd(0,change(ko)+dol,1,++num) );
	}

int ileA=0;
int ileB=0; 
int jestA= 0;
int jestB= 0;

while(!kol.empty()){
	zd ruch = kol.top();
	kol.pop();
//	cout<< ruch.czas <<" "<<ruch.A<<" "<<ruch.odjazd<<" "<<ruch.li<<endl;
	if( ruch.A ){
		if( ruch.odjazd ){
			if(jestA==0){
				ileA++;jestA++;
			}
			jestA--;
		}
		else jestA++;
	}
	else {
		if( ruch.odjazd ){
			if(jestB==0){
				ileB++;jestB++;
			}
			jestB--;
		}
		else jestB++;
	}	
}

cout<<"Case #"<<przypadek<<": "<<ileA<<" "<<ileB<<endl;
}

return 0;
}
