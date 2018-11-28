#include<cstdio>
#include<algorithm>
using namespace std;
int T,N;
struct node{
	int val, pos;
}a[1005];

bool cmp(node a, node b){
	return a.val < b.val;
}

int main(){
	scanf("%d",&T);
	for (int t=1;t<=T;++t){
		scanf("%d",&N);
		for (int i=0;i<N;++i){
			scanf("%d",&a[i].val);
			a[i].pos = i;
		}
		sort(a,a+N,cmp);
		int ans=0;
		for (int i=0;i<N;++i){
			if (a[i].pos!=i) ++ ans;
		}
		printf("Case #%d: %d.000000\n",t,ans);
	}
	

	return 0;
}
