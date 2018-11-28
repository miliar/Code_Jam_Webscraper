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
int t;
int n,m;
char mem[(1<<17)+55][40];
vector<int> dx,dy;
#define ok(x,y) (x>=0 && y>=0 && x<n && y<m && !a[x][y])
inline int C(int x, int y){
 return x*m+y;
}
char doit(int mask,int st){
	char &ret=mem[mask][st];
	if (ret>0) return ret;
	char a[4][4];
	For(i,0,n)
		For(j,0,m){
		  a[i][j]= ((mask& (1<<C(i,j)))>0);
		}
	int x=st/m,y=st%m;
	For(i,0,8){
		int tx=x+dx[i],ty=y+dy[i];
		if (ok(tx,ty) && doit(mask|(1<<(C(tx,ty))),C(tx,ty))==2)
		    return ret=1;
		   
	}
	//cout << mask << ' ' << st << ' ' << ret << endl;
	return ret=2;
}
char buf[5];
int main(){
   freopen("D.in","r",stdin);
   For(i,-1,2) For(j,-1,2){
    if (!i &&!j) continue;
	dx.pb(i); dy.pb(j);
   }
   scanf("%d",&t);
   for(int cas=1;cas<=t;cas++){
	scanf("%d%d",&n,&m);
	int mask=0,st=0;
	For(i,0,n){
		scanf("%s",buf);
		For(j,0,m){
			if (buf[j]=='#') mask|= (1<<(C(i,j)));
			if (buf[j]=='K') st= C(i,j);
		}
	}
	//cout << st << endl;
	CLR(mem,0);
	printf("Case #%d: %c\n",cas,(doit(mask|(1<<st),st)%2==1?'A':'B'));   
   }
return 0;
} 
