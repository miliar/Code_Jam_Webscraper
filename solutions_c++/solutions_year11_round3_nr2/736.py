#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;

int c[1005];
int a[100005];
int xx[105],k;

bool cmp(int a,int b){
	return a>b;
}

int main(){
	int T;
	int cas=1;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B1.txt","w",stdout);

	scanf("%d",&T);
	while(T--){
		int L,t,N,C;
		int i,j;
		scanf("%d %d %d %d",&L,&t,&N,&C);
		for(i=0;i<C;++i){
			scanf("%d",&c[i]);
		}
		for(i=0;i<N;++i){
			a[i]=c[i%C];
		}
		int x=0,limit=t/2;
		for(i=0;i<N;++i){
			x=x+a[i];
			if(x>limit)
				break;
		}
		xx[k=0]=x-limit;
		k++;

		for(i++;i<N;++i){
			xx[k++]=a[i];
		}

		sort(xx,xx+k,cmp);

		int ans=t;
		i=0;
		while(L--){
			ans=ans+xx[i++];
		}
		for(;i<k;++i){
			ans=ans+xx[i]*2;
		}
		printf("Case #%d: %d\n",cas++,ans);
	}
	return 0;
}