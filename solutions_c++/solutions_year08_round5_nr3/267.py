#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <cctype>
#include <assert.h>
#include <list>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace __gnu_cxx;
using namespace std;

#define MP(a,b) make_pair(a,b)
#define i64 long long
#define pb push_back
#define For(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define Rev(i,a,b) for(typeof(a) i=(a);i>=(b);i--)
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++)
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(x) x.begin(),x.end()

/**********************************************************************************/
const int maxn=650;
int hei[maxn],a[maxn][maxn],_SINK,n,m,t,N;
vector<int> e[maxn];
char buf[88][88];
void connect(int x, int y, int x1, int  y1,int sp){
	if (buf[x][y]=='x') return;
	if (buf[x1][y1]=='x') return;
	if (!(y&1) && sp!=1)
		swap(x,x1),swap(y,y1);
		
	a[x*m+y][x1*m+y1]=sp;
	e[x*m+y].pb(x1*m+y1);
	e[x1*m+y1].pb(x*m+y);
}


int dfs(int x,int F){
	if (!F|| x==_SINK) return F;
	int ret=0;
	For(i,0,e[x].size()){
		int y=e[x][i];
		if (hei[y]!=hei[x]+1) continue;
		int k= min(F,a[x][y]);
		k=dfs(y,k);
		ret+=k; F-=k;
		a[x][y]-=k; a[y][x]+=k;
		if (!F) break;
	}
	//cout << x << ' ' << ret << endl;
	return ret;
}
queue<int> Q;
int flow(int src,int SINK){
	_SINK=SINK; int ret=0;
	while (1){
		while (!Q.empty()) Q.pop(); Q.push(src); CLR(hei,0x5F); hei[src]=0;
		while(!Q.empty()){
			int x=Q.front(); Q.pop();
			For(i,0,e[x].size()){
				int y=e[x][i];
				if (a[x][y]>0 && hei[y]>hei[x]+1){ hei[y]=hei[x]+1; Q.push(y);}
			}				
		}
		//For(i,0,N) cout << hei[i] << endl;
		if (hei[SINK]>n*m+2) break;
		ret+=dfs(src,9999999);
		//cout << ret << endl;
	}
	return ret;
}
const int inf=999999;
int main(){
	freopen("input3.txt","r",stdin);
	freopen("output3.txt","w",stdout);
	scanf("%d",&t);
	for(int cas=1;t--;cas++){
		scanf("%d%d",&n,&m); CLR(buf,'.');
		For(i,0,n) 
			scanf("%s",&buf[i]);
		CLR(a,0);
		For(i,0,maxn) e[i].clear();
		CLR(hei,0);
		int tot=0;
		For(i,0,n){
			For(j,0,m){
				if (buf[i][j]=='x') continue;
				tot++;
				if (j){
					connect(i,j-1,i,j,inf);
					if (i) connect(i-1,j-1,i,j,inf);
				}
				if (j<m-1){
					connect(i,j+1,i,j,inf);
					if (i) connect(i-1,j+1,i,j,inf);
				}
				if (j&1)
					connect(n,0,i,j,1);
				else
					connect(i,j,n,1,1);
			}
		
		}
		 N=n*m+2;
	//	cout << n << ' ' << m  << 
		printf("Case #%d: %d\n",cas,tot-flow(n*m,n*m+1));
	}

}