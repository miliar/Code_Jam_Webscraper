// B.cpp

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

using namespace std;

int D,I,M,N;
int v[1280];

int ct[1280][256]; // the cost[ith][value]

int add(int i,int j){
	if (i==j) return 0;
	return (abs(i-j)-1)/M;
}

void solve(int cas){
	int i,j,k;
	scanf("%d%d%d%d",&D,&I,&M,&N);
	for (i=0;i<N;i++) scanf("%d",v+i);
	memset(ct,0x7f,sizeof(ct));

	for (i=0;i<256;i++){
		ct[0][i]=abs(v[0]-i);
	}
	k=0;
//	printf("ct[%d][%d]=%d\n",k,v[k],ct[k][v[k]]);
	for (k=1;k<N;k++){
		for (i=0;i<256;i++) ct[k][i]=min(ct[k][i],ct[k-1][i]+D);
		for (i=0;i<256;i++){
			for (j=0;j<256;j++){
			if (M==0 && i!=j) continue;
				ct[k][j]=min(ct[k][j],ct[k-1][i]+ add(i,j)*I + +abs(v[k]-j));
			}
		}
//		printf("ct[%d][%d]=%d\n",k,v[k],ct[k][v[k]]);
	}
	int ret = ct[N-1][0];
	for (i=0;i<256;i++){
//		printf("ct[%d] = %d\n",i,ct[N-1][i]);
		ret = min(ret,ct[N-1][i]);
	}
	printf("Case #%d: %d\n",cas,ret);
}

int main(){
	int t,cas;
	freopen("B-small-attempt0.in","r",stdin); freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-large.in","r",stdin); freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		solve(cas);
	return 0;
}
