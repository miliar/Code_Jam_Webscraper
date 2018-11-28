#include <cstdio>
#include <algorithm>

const int maxn=1024;
using namespace std;

int A[maxn],B[maxn];
int N;

void solve(int cas){
	int i,res;
	scanf("%d",&N);
	for (i=0;i<N;i++) scanf("%d",A+i);
	for (i=0;i<N;i++) scanf("%d",B+i);
	sort(A,A+N);
	sort(B,B+N);
	res=0;
	for (i=0;i<N;i++)
		res+=A[i]*B[N-1-i];
	printf("Case #%d: %d\n",cas,res);
}

int main(){
	int t,cas;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		solve(cas);
	return 0;
}

