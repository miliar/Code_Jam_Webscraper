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
	freopen("c.in","r",stdin); //input
	freopen("Cout.txt","w",stdout);
	int a,b,n,c=1;
	cin>>n;
	int res=0;
	
	REP(i,n){
		cin>>a>>b;
		res=0;
		cout<<"Case #"<<c<<": ";
		c++;
		if(b<10||b==1000) {cout<<"0"<<endl; continue; }
		if(b<100&& a>9){
			for(int n=a; n<b; n++)
				for(int m=n+1; m<=b; m++){
					int f,v,s;
					f=n/10;
					s=n%10;
					v=s*10+f;
					if(v==m) res++;
					}
			cout<<res<<endl;
			}
		if(a>99 && b<1000){
			for(int n=a; n<b; n++){
				for(int m=n+1; m<=b; m++){
					int n1,n2,n3, v1,v2;
					n1=n/100;
					n2=(n-n1*100)/10;
					n3=n%10;
					v1=n3*100+n1*10+n2;
					v2=n2*100+n3*10+n1;
					if(v1==m  || v2==m) res++;
					}
					}
			cout<<res<<endl;
			}
}
	return 0;
}
