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
int a[110][55];
int n,k,t;
bool g(int x, int y){
	For(i,0,k) if (a[x][i]<=a[y][i]) return false;
	return true;
}
bool used[110];
int deg[110],cur[110];
int mem[1<<16][17];
vector<int> best;
int doit(int mask,int prev){
	int &ret=mem[mask][prev];
	if (mask+1==(1<<n)) return ret=0;
	if (ret>=0) return ret;
	ret=n+n;
	For(i,prev,n){
		if (g(best[i],best[prev]))
			ret<?=doit(mask|(1<<i),i);
	}
	For(i,0,n){
		if (mask & (1<<i)) continue;
		ret<?=1+doit(mask|(1<<i),i);
	}
	return ret;
}
int main(){
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
		scanf("%d%d",&n,&k);
		For(i,0,n)
			For(j,0,k) scanf("%d",&a[i][j]);
		For(i,0,n){
			For(j,0,n)
				if (g(i,j)){
					deg[j]++;
					cur[j]++;
				}
		}
		best.clear();
		CLR(used,0);
		while (1){
			int X=-1;
			For(i,0,n){
				if (!cur[i] && !used[i]){
					if (X==-1 || deg[X]>deg[i]) X=i;

				}
			}
			//printf("Taking out %d\n",X);
			used[X]=1;
			best.pb(X);
			For(i,0,n) if (!used[i] && g(X,i)) cur[i]--;
			bool done=1;
			For(i,0,n) done&=used[i];
			if (done) break;
		}
		reverse(ALL(best));
		vector<int> cur;
		For(i,0,n) For(j,0,i) assert(!g(best[j],best[i]));
		CLR(mem,-1);
		int ret=1+doit(1,0);
/*		For(i,0,n){
			bool good=1;
			For(j,0,cur.size()){
				if (g(best[i],cur[j])){
					cur[j]=best[i];
					good=0;
					break;
				}
			}	
			if (good) 
				cur.pb(best[i]);
		}
		int ret=0;
		CLR(used,0);
		while (++ret){
			int cur=-1;
		 	For(i,0,n){
				if (!used[i]) { cur=i; break;}

			}
			if (cur==-1) break;
			int prev=cur;
			used[prev]=1;
			For(i,cur+1,n){
				if (g(best[i],best[prev])) { prev=i; used[i]=1;}

			}
		}
		//if (ret-1 != cur.size())
			//cerr  << ret-1 <<' ' << cur.size() <<  ' ' << n << endl;
		printf("Case #%d: %d\n",cas,ret-1);
		*/
		printf("Case #%d: %d\n",cas,ret);
	}
	return 0;
}
