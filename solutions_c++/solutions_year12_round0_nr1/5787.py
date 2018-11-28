#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<sstream>
#include<queue>
#include <fstream>
using namespace std;
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define ALL(a) (a).begin(), (a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
#define REPR(i,n) for(int i=(n-1);i>=0;--i)	
#define REPN(i,n) for(int i=0;i<=(n);++i)
#define FOR(i,a,b) for(int i=a;i<(b);++i)
#define FORN(i,a,b) for(int i=a;i<=(b);++i)
#define FORV(i,v) for(size_t i=0;i<(v).size();++i)
#define INF 1000000000
using namespace std;
typedef vector<int>  vi;
typedef vector<vector<int> >  vvi;
typedef long long LL;
typedef unsigned long long ULL;

int main(){
	freopen("a.in","r",stdin); //input
	
	freopen("1out.txt","w",stdout);
	int n,c=1;
	cin>>n;
	string f;
	getline(cin, f);
	REP(i,n){
	getline(cin, f);
	cout<<"Case #"<<c<<": ";
	c++;
	for(int i=0; i<f.length(); i++){
		switch ( f[i] ){
			case 'a' : {cout<<'y'; continue;}
			case 'b' : {cout<<'h'; continue;}
			case 'c' : {cout<<'e'; continue;}
			case 'd' : {cout<<'s'; continue;}
			case 'e' : {cout<<'o'; continue;}
			case 'f' : {cout<<'c'; continue;}
			case 'g' : {cout<<'v'; continue;}
			case 'h' : {cout<<'x'; continue;}
			case 'i' : {cout<<'d'; continue;}
			case 'j' : {cout<<'u'; continue;}
			case 'k' : {cout<<'i'; continue;}
			case 'l' : {cout<<'g'; continue;}
			case 'm' : {cout<<'l'; continue;}
			case 'n' : {cout<<'b'; continue;}
			case 'o' : {cout<<'k'; continue;}
			case 'p' : {cout<<'r'; continue;}
			case 'r' : {cout<<'t'; continue;}
			case 's' : {cout<<'n'; continue;}
			case 't' : {cout<<'w'; continue;}
			case 'u' : {cout<<'j'; continue;}
			case 'v' : {cout<<'p'; continue;}
			case 'w' : {cout<<'f'; continue;}
			case 'x' : {cout<<'m'; continue;}
			case 'y' : {cout<<'a'; continue;}
			//
			case 'z' : {cout<<'q'; continue;}
			case 'q' : {cout<<'z'; continue;}
			default :  cout<<' ';
		}
	}
	cout<<endl;	
}

	return 0;
}
