#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <queue>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <set>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;



string mat[5];

bool vst[5][5];
bool suc;
int R,C;

void dfs(int state,int x,int y,int &nx,int &ny){
	int wei=x*C+y;
	bool flag=state&(1<<wei);
	if( mat[x][y]=='-' ){
		if( flag ){
			nx=x;
			ny=y-1;
		}else{
			nx=x;
			ny=y+1;
		}
	}else if( mat[x][y]=='|' ) {
		if( flag ) {
			nx=x-1;
			ny=y;
		}else{
			nx=x+1;
			ny=y;
		}
	}else if( mat[x][y]=='/' ){
		if( flag ) {
			nx=x-1;
			ny=y+1;
		}else{
			nx=x+1;
			ny=y-1;
		}
	}else if( mat[x][y]=='\\' ){
		if( !flag ) {
			nx=x+1;
			ny=y+1;


		}else{
			nx=x-1;
			ny=y-1;

		}
	}else{
		cout<<"fuck"<<endl;
	}
	nx=(nx+R)%R;
	ny=(ny+C)%C;
}


int main(){
	freopen("C-small-attempt0(2).in","r",stdin);
	freopen("C-small-attempt0(2).out","w",stdout);

	int cas,Te=1;
	cin>>cas;
	while( cas-- ){
		cin>>R>>C;
		for(int i=0;i<R;i++) cin>>mat[i];
		int ans=0;
		for(int state=0;state<(1<<(R*C));state++){
			bool suc=true;
			memset(vst,false,sizeof(vst));
			for(int i=0;i<R;i++){
				for(int j=0;j<C;j++){
					int nx,ny;
					dfs(state,i,j,nx,ny);
					if( vst[nx][ny] ) suc=false;
					vst[nx][ny]=true;
				}
			}
			if( suc ) ans++;
		}
		printf("Case #%d: %d\n",Te++,ans);
		//for(int i=1;i<G;i++) printf("%.8lf\n",ans[i]);
	}
}