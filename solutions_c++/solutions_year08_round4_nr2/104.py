// B.cc

#include <stdio.h>
#include <string.h>
#include <map>

using namespace std;

typedef pair<int,int> PI;
map<int,PI> S;
map<int,PI>::iterator it;
int M,N,A;

// A*B-C*D=X

void solve(int cas){
	S.clear();
	PI X;
	int key,i,j;
	int found=0;
	scanf("%d%d%d",&N,&M,&A);
	for (i=0;i<=N && !found;i++){
		for (j=0;j<=M && !found;j++){
			it=S.find(i*j-A);
			if (it!=S.end()) found=1;
			if (found==0){
				it=S.find(i*j+A);
				if (it!=S.end()) found=1;
			}
			if (found==1){
				printf("Case #%d: 0 0 %d %d %d %d\n",cas,i,it->second.first,it->second.second,j);
			}
			X.first=i; X.second=j;
			if (S.find(i*j)==S.end()) S[i*j]=X;
		}
	}
	if (!found) printf("Case #%d: IMPOSSIBLE\n",cas);
}

int main(){
	int cas,t;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		solve(cas);
	return 0;
}
