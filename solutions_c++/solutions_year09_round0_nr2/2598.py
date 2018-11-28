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
#define ok(a,b) ((a>=0) && (b>=0) && (a<n) && (b<m))
const int dx[]={0,-1,1,0};
const int dy[]={1,0,0,-1};
const int maxn=101;

struct node{
	int x,y,hei;
	node(int x1=0,int y1=0,int h1=0):x(x1),y(y1),hei(h1){}
};
bool operator<(const node &a, const node &b){
	return a.hei>b.hei|| ( a.hei==b.hei && ( a.x>b.x || a.x==b.x && (a.y>b.y)));
}

int a[maxn][maxn],fin[maxn][maxn];
int used[50];
int n,m,t;
int main(){
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){	
		scanf("%d%d",&n,&m);
		For(i,0,n) For(j,0,m) scanf("%d",&a[i][j]);
		priority_queue<node> PQ;
		For(i,0,n)
			For(j,0,m){
				PQ.push(node(i,j,a[i][j]));
			}
		int cur=0;
		CLR(fin,-1);
		while (!PQ.empty()){
			node T=PQ.top(); PQ.pop();
			if (fin[T.x][T.y]==-1) 
				fin[T.x][T.y]=cur++;
			//cout << T.x << ' ' << T.y << ' '<< fin[T.x][T.y] << endl;
			Rev(i,3,0){
				int tx=T.x+dx[i],ty=T.y+dy[i];
				if (!ok(tx,ty) || a[tx][ty]<=a[T.x][T.y]) continue;
				if (fin[tx][ty]==-1){
					fin[tx][ty]=fin[T.x][T.y];
					PQ.push(node(tx,ty,a[tx][ty]));
				}
			}
		}
		CLR(used,-1);
		cur=0;
		For(i,0,n) For(j,0,m) if (used[ fin[i][j]]==-1) used[fin[i][j]]=cur++;
		printf("Case #%d:\n",cas);
		For(i,0,n)
			For(j,0,m){
				printf("%c%c",used[fin[i][j]]+'a',(j==m-1?'\n':' '));
			}

	}
	return 0;
}
