#include <cstdio>
#include <cmath>
#include <iostream>
#include <sstream>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <string.h>
#include <limits.h>
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORR(i,n) for(int i=(n)-1;i>=0;i--)
#define MAX 120
#define MOD 1000000
#define LL long long
#define PR pair<int,int>
#define MAP map<int,int>
#define VI vector<int>
#define PQUEUE priority_queue<PR >
#define FORM(i,n) for(MAP::iterator i=n.begin();i!=n.end();i++)
using namespace std;



int M,N,T;
char dp[MAX][MAX];
int solve(){
	char ch[2]={'X','O'};
	FOR(c,2){
		FOR(i,N){
			int cnt=0;
			FOR(j,N) 
				if(dp[i][j]==ch[c] || dp[i][j]=='T') cnt++;
			if(cnt==N)	return c==0?0:1;
			cnt=0;
			FOR(j,N) 
				if(dp[j][i]==ch[c] || dp[j][i]=='T') cnt++;
			if(cnt==N)	return c==0?0:1;
		}
		int cnt=0;
		FOR(i,N) if(dp[i][i]==ch[c] || dp[i][i]=='T') cnt++;
		if(cnt==N)	return c==0?0:1;			
		int j=N-1;
		cnt=0;
		FOR(i,N){ 
			if(dp[i][j]==ch[c] || dp[i][j]=='T') cnt++;
			j--;
		}
		if(cnt==N)	return c==0?0:1;						
	}
	FOR(i,N)FOR(j,N) if(dp[i][j]=='.') return 3;
	return 2;
}
int main(){
	N=4;
	//scanf("%d",&T);
	cin>>T;
	FOR(test,T){		
		FOR(i,N)
			FOR(j,N)
			//scanf("%c",&dp[i][j]);			
			cin>>dp[i][j];

		
		
		int r=solve();
		cout<<"Case #"<<(test+1)<<": ";
		if(r==0) cout<<"X won"<<endl;
		else if(r==1) cout<<"O won"<<endl;
		else if(r==2) cout<<"Draw"<<endl;
		else if(r==3) cout<<"Game has not completed"<<endl;
	}
	
}
