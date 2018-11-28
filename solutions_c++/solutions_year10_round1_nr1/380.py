#include <stdio.h>
#include <utility>
#include <iostream>
#include <string>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <queue>
#include <sstream>
#include <vector>
#include <stack>


using namespace std;
#define lint long long
#define SZ(s) ((int)(s.size()))
#define FORN(i,x,y) for(i=x;i<y;++i)
#define FOR(i,x) FORN(i,0,x)
#define MP make_pair
#define PB push_back
#define FOREACH(it,vec) for(typeof(vec.begin()) it=vec.begin();it != vec.end();it++)
#define SET(x,a) memset(x,a,sizeof x)
#define FIR first
#define SEC second
#define ALL(x) x.begin(),x.end()
#define vi vector<int >
#define vvi vector<vi >
#define VS vector<string >
#define checkmax(a,b) a=max(a,b)
#define checkmin(a,b) a=min(a,b)

VS rotate(VS b){
	int n = SZ(b),i,j;
	VS ret(n,string(n,'.'));
	FOR(i,n)FOR(j,n)
		ret[j][n-1-i]=b[i][j];
	return ret;
}
VS gravitate(VS b){
	int n = SZ(b),i,j;
	FOR(i,n){
		for(j=n-1;j>=0;j--)if(b[j][i]!='.'){
			int k,k2;
			FORN(k,j+1,n)if(b[k][i]!='.')
				break;
			k--;
			b[k][i]=b[j][i];
			FORN(k2,j,k)b[k2][i]='.';
		}
	}
	return b;
}
int N,K;

int sol(VS b,char c){
	int i,j,k;
	FOR(i,N)FOR(j,N)if(b[i][j]==c){
		FORN(k,j,N)if(b[i][k]!=c)break;
		if(k-j >= K)return true;
		FORN(k,i,N)if(b[k][j]!=c)break;
		if(k-i >= K)return true;
		FOR(k,min(N-i,N-j))if(b[i+k][j+k]!=c)break;
		if(k>=K)return true;
		FOR(k,min(N-i,j+1))if(b[i+k][j-k]!=c)break;
		if(k>=K)return true;
	}
	return false;
}

int main(){
	int cas,it;
	cin>>cas;
	FOR(it,cas){
		cin>>N>>K;
		VS b(N);
		int i;
		FOR(i,N)cin>>b[i];
		b=rotate(b);b=gravitate(b);
		//FOR(i,N)cout<<b[i]<<endl;
		cout<<"Case #"<<(it+1)<<": ";
		if(sol(b,'R') && sol(b,'B')){
			cout<<"Both"<<endl;
		}
		else if(!sol(b,'R') && !sol(b,'B')){
			cout<<"Neither"<<endl;
		}
		else if(sol(b,'R'))
		{
			cout<<"Red"<<endl;
		}
		else{
			cout<<"Blue"<<endl;
		}
	}
	return 0;
}
