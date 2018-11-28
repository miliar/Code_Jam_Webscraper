#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <cstdlib>
#include <utility>

using namespace std;


#define INF 10005 
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FILL(a) memset(a,0,sizeof(a))
#define FILL1(a) memset(a,-1,sizeof(a))
#define FILL2(a) memset(a,INF,sizeof(a))
#define MAX 10005
typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > ppi;
typedef vector<pii > VP;
typedef priority_queue<ppi > PQ;
typedef vector<string> VS;
typedef long double ld;
typedef long long ll;
int bitc(ll r) {return r == 0 ? 0 : (bitc(r>>1) + (r&1));}
ll gcd(ll x, ll y) {return x>0 ? gcd(y%x,x) : y;}

//template<class T> T& operator >?= (T& x, T y) {if(y>x) x=y; return x;}
//template<class T> T& operator <?= (T& x, T y) {if(y<x) x=y; return x;}
//template<class T> T operator >? (T x, T y) {return x>y?x:y;}
//template<class T> T operator <? (T x, T y) {return x<y?x:y;}


int H,W,N;
int d[105][105];
char b[105][105];
char basin='a';
char dfs(int i,int j){
	if(b[i][j]!=' ') return b[i][j];

	int v=d[i][j],ni,nj;
	for(int k=i-1;k<=i+1;k++)
		for(int z=j-1;z<=j+1;z++){
			if(k>=0 && k<H && z>=0 && z<W && (z==j || k==i)){
				if(d[k][z]<v){	v=d[k][z]; ni=k;nj=z;}
			}
		}
	if(v==d[i][j]){
		b[i][j]=basin;
		basin++;		
	}else 	b[i][j]=dfs(ni,nj);

	return b[i][j];
}

int main(int argc,char** argv){
	istream* tstream=&cin;
	if(argc==1) tstream=new ifstream("C:\\Documents and Settings\\Maksim Piriyev\\Desktop\\in.txt");
	istream& in=(*tstream);
	//istream& in=cin;
	in>>N;
	
	FOR(i,N){
		in>>H>>W;
		basin='a';
		FOR(k,H)FOR(j,W)in>>d[k][j];
		FOR(k,H)FOR(j,W)b[k][j]=' ';

		FOR(k,H)FOR(j,W)dfs(k,j);
		
			
		cout<<"Case #"<<(i+1)<<":"<<endl;
		FOR(k,H){FOR(j,W)cout<<b[k][j]<<" "; cout<<endl;}
		
	}
	

	
}
