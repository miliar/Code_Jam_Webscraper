#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cassert>

using namespace std;

#define allof(c) ((c).begin()),((c).end())
#define debug(c) cout<<"> "<<#c<<" = "<<c<<endl;
#define iter(c) __typeof((c).begin())
#define tr(i,c) for(iter(c) i=(c).begin();i!=(c).end();i++)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define repd(i,n) for(int i=(int)(n-1);i>=0;i--)
#define repi(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define mp make_pair
#define fst first
#define snd second
#define pb push_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef pair<double,double> pdd;

#define INFTY 1000000000

char go(int x,int y,char &c,vvi &m,vector<vector<char> > &ans){
	int dx[]={0,-1,1,0};
	int dy[]={-1,0,0,1};
	int mini=m[y][x];
	int next_x,next_y;
	rep(i,4){
		int tx=x+dx[i],ty=y+dy[i];
		if(tx>=m[0].size() || tx<0 || ty>=m.size() || ty<0){
			continue;
		}
		if(ans[ty][tx]==-2){
			continue;
		}
		if(mini>m[ty][tx]){
			mini=m[ty][tx];
			next_x=tx;
			next_y=ty;
		}
	}
	if(mini==m[y][x]){
		return ans[y][x]=c;
	}
	if(ans[next_y][next_x]!=0){
		return ans[y][x]=ans[next_y][next_x];
	}
	ans[y][x]=-2;
	ans[y][x]=go(next_x,next_y,c,m,ans);
	return ans[y][x];
}

int main(){
	int T; cin>>T;
	rep(iCases,T){
		int H,W; cin>>H>>W;
		vvi m(H,vi(W));
		rep(i,H) rep(j,W){
			cin>>m[i][j];
		}
		vector<vector<char> > ans(H,vector<char>(W,0));
		char cur_c='a';
		rep(i,H) rep(j,W){
			if(isalpha(ans[i][j])){
				continue;
			}
			char c=go(j,i,cur_c,m,ans);
			if(c==cur_c){
				cur_c++;
			}
		}
		printf("Case #%d:\n",iCases+1);
		rep(i,H) rep(j,W){
			if(j==W-1){
				cout<<ans[i][j]<<endl;
			}
			else{
				cout<<ans[i][j]<<" ";
			}
		}
	}
	return 0;
}
