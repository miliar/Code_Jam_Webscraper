#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cassert>

using namespace std;

#define allof(c) ((c).begin()),((c).end())
#define debug(c) cerr<<"> "<<#c<<" = "<<(c)<<endl;
#define iter(c) __typeof((c).begin())
#define tr(i,c) for(iter(c) i=(c).begin();i!=(c).end();i++)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define REP(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define mp make_pair
#define fst first
#define snd second
#define pb push_back

typedef vector<int> vi;


int main(){
	int T; cin>>T;
	for(int iCase=1;iCase<=T;iCase++){
		int R,C; cin>>R>>C;
		vector<string> map(R);
		rep(i,R) cin>>map[i];
		
		rep(i,R-1) rep(j,C-1){
			if(map[i][j]=='#'){
				bool flg=true;
				rep(dx,2) rep(dy,2){
					flg&=(map[i+dy][j+dx]=='#');
				}
				if(flg){
					map[i][j]='/';
					map[i+1][j+1]='/';
					map[i+1][j]='\\';
					map[i][j+1]='\\';
				}
			}
		}
		
		cout<<"Case #"<<iCase<<":"<<endl;
		int bcnt=0;
		rep(i,R) rep(j,C) if(map[i][j]=='#') bcnt++;
		if(bcnt!=0) cout<<"Impossible"<<endl;
		else{
			rep(i,R) cout<<map[i]<<endl;
		}
		
	}
	
	return 0;
}
