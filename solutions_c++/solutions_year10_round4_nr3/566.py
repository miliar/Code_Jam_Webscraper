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
	int nCases; cin>>nCases;
	for(int iCase=1;iCase<=nCases;iCase++){
		int r; cin>>r;
		vector<vi> m(110,vi(110,0));
		int w=0,h=0;
		rep(i,r){
			int x1,y1,x2,y2; cin>>x1>>y1>>x2>>y2;
			w=max(w,x2);
			h=max(h,y2);
			REP(x,x1,x2) REP(y,y1,y2){
				m[y-1][x-1]=1;
			}
		}
		
		int res=0;
		for(;;){
//			vector<vi> nm(h,vi(w,0));
			int cnt=0;
			res++;
/*			REP(i,1,h-1) REP(j,1,w-1){
				if(m[i-1][j] && m[i][j-1]){
					nm[i][j]=1;
					cnt++;
				}
				if(m[i][j] && (m[i-1][j] || m[i][j-1])){
					nm[i][j]=1;
					cnt++;
				}
			}
			m=nm;
*/			
			for(int i=h-1;i>=0;i--) for(int j=w-1;j>=0;j--){
				if(i==0 || j==0){
					m[i][j]=0;
				}
				else if(m[i-1][j] && m[i][j-1]){
					m[i][j]=1;
					cnt++;
				}
				else if(m[i][j] && (m[i-1][j] || m[i][j-1])){
					m[i][j]=1;
					cnt++;
				}
				else{
					m[i][j]=0;
				}
			}
			if(cnt==0) break;
		}
		cout<<"Case #"<<iCase<<": ";
		cout<<res<<endl;
	}
	
	return 0;
}
