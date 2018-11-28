#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <string>
#include <sstream>
#include <queue>
using namespace std;
typedef long long llong;

const int Max=64;
int X[Max],V[Max];
int main(){
	int TT;
	scanf("%d",&TT);
	for(int cas=1;cas<=TT;++cas){
		int N,K,B,T;
		scanf("%d %d %d %d",&N,&K,&B,&T);
		for(int i=0;i<N;++i) scanf("%d",X+i);
		for(int i=0;i<N;++i) scanf("%d",V+i);
		int cnt=0,late=0;
		for(int i=N-1;i>=0;--i){
			if(V[i]*T>=B-X[i]){
				cnt+=late;
				if((--K)<=0) break;
			}
			else ++late;
		}
		if(K>0) printf("Case #%d: IMPOSSIBLE\n",cas);
		else printf("Case #%d: %d\n",cas,cnt);
	}
	return 0;
}
