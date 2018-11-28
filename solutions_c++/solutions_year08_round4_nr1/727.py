#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define eps 1e-8
#define PI 3.14159265358979323846
using namespace std;

int g[10001];
int c[10001];
int v[10001];
int gg[10001];
int ret[2][10001];
int m,V;
int best;


void getac(int d){
	if(d==(m-1)/2+1){
		int cnt=0;
		int i;
		for(i=(m-1)/2;i>=1;i--){
			if(gg[i]!=g[i])
				cnt++;
			if(gg[i]==1)
				v[i]=v[i*2]&v[i*2+1];
			else
				v[i]=v[i*2]|v[i*2+1];
		}
		if(v[1]==V){
			if(cnt<best)
				best=cnt;
		}
	}else{
		if(c[d]){
			gg[d]=1;
			getac(d+1);
			gg[d]=0;
			getac(d+1);
		}else{
			gg[d]=g[d];
			getac(d+1);
		}
	}
}

int op(int o, int n1, int n2){
	if(o==1)
		return n1&n2;
	else
		return n1|n2;
}

int main(){
	int T,TT;
	scanf("%d",&T);
	for(TT=1;TT<=T;TT++){
		int i;
		scanf("%d%d",&m,&V);
		for(i=0;i<(m-1)/2;i++){
			scanf("%d%d",&g[i+1],&c[i+1]);
			ret[0][i+1]=ret[1][i+1]=1000000;
		}
		for(i=(m-1)/2;i<m;i++){
			scanf("%d",&v[i+1]);
			ret[v[i+1]][i+1]=0;
			ret[1-v[i+1]][i+1]=1000000;
		}
		for(i=(m-1)/2;i>=1;i--){
			for(int kk=0;kk<=1;kk++)
				for(int pp=0;pp<=1;pp++){
					if(ret[op(g[i],kk,pp)][i]>ret[kk][i*2]+ret[pp][i*2+1])
						ret[op(g[i],kk,pp)][i]=ret[kk][i*2]+ret[pp][i*2+1];
				}
			if(c[i]){//¿É±ä
				for(int kk=0;kk<=1;kk++)
					for(int pp=0;pp<=1;pp++){
						if(ret[op(1-g[i],kk,pp)][i]>ret[kk][i*2]+ret[pp][i*2+1]+1)
							ret[op(1-g[i],kk,pp)][i]=ret[kk][i*2]+ret[pp][i*2+1]+1;
					}
			}
		}
		if(ret[V][1]==1000000)
			printf("Case #%d: IMPOSSIBLE\n",TT);
		else
			printf("Case #%d: %d\n",TT,ret[V][1]);
	}
}