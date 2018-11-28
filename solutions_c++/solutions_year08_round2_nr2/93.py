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
#define For(i,a,b) for(i64 i=(a);i<(b);i++)
#define Rev(i,a,b) for(typeof(a) i=(a);i>=(b);i--)
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++)
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(x) x.begin(),x.end()

/**********************************************************************************/
const int maxn=1000100;
bool used[maxn];
i64 par[maxn],sz[maxn];
i64 G[maxn],P[maxn/10],pn;
void gen(){
	P[0]=2; pn=1;
	CLR(used,1); 
	for(int i=3;i<maxn;i+=2){
		used[i+1]=0;
		if (used[i]) P[pn++]=i;
		if (used[i]  && i <maxn/i){
			for(int j=i*i;j<maxn;j+=i)
				used[j]=0;					
		}
	}

}

int fin (int x){
	if (par[x]==x) return x;
	return par[x]=fin(par[x]);
}
i64 A,B,K;
void merge(int x, int y){
	assert(x>=0 && x<=B-A+1 && y>=0 && y<=B-A+1);
	if (x==y) return;
	//cout << sz[x] << ' ' << sz[y] << ' ';
	if (sz[x]>=sz[y]){
		par[y]=x;
		sz[x]+=sz[y];
	}
	else{
		par[x]=y;
		sz[y]+=sz[x];
	}	
	//cout << x+A << ' ' << y+A << ' ' << par[x] << ' ' << par[y] << endl;
}
int t;

int main(){
	freopen("input2.txt","r",stdin);
	gen();
	scanf("%d",&t);
	for(int cas=1;t--;cas++){
	map<i64,int> M;
		scanf("%lld%lld%lld",&A,&B,&K);
		//cout << A << ' ' << B << endl;
		For(i,A,B+1){
			G[i-A]=i;
			par[i-A]=i-A;
			sz[i-A]=1;
		}
		For(i,0,pn){
			int x=P[i];
			if (x>B) break;
			i64 prev=-1;
			//cout << x << ":";
			for(i64 j=x*((A+x-1)/x);j<=B;j+=x){
			//	cout << j <<  ' ';
				while (G[j-A]%x==0){
					G[j-A]/=x;						
				}
				if (x>=K && prev>=0)		merge(fin(prev-A),fin(j-A));
				prev=j;
			}
			//cout << endl;
		}
		For(i,0,B+1-A){
			if (G[i]>=K && M.count(G[i])){
				merge(fin(M[G[i]]),fin(i));
			}	
			M[G[i]]=i;
			fin(i);
		}
		sort(par,par+(B-A+1));
		int ret=1;
		
		For(i,1,B-A+1) ret+= (par[i]!=par[i-1]);
		int prev=-1;
		For(i,0,B-A+1){
			if (par[i]!=prev){
			//	cout << par[i]+A << ' ';
				prev=par[i];
			}
		}
		//cout << endl;
		printf("Case #%d: %d\n",cas,ret);	
	}
	return 0;
	
}

