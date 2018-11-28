#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long LL;

const int N=1000001;

int F[N];

int main(){
	F[1]=2;
	F[2]=4;
	int i;
	for(i=3;i<N;i++){
		F[i]=i+(upper_bound(F+1,F+i,i)-F);
	}
	//for(i=0;i<100;i++) printf("%d\t",F[i]);
	int cas,ic;
	scanf("%d",&cas);
	for(ic=1;ic<=cas;ic++){
		int a1,a2,b1,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		LL ans=0;
		for(i=a1;i<=a2;i++){
			if(b1>=F[i]) ans+=b2-b1+1;
			else if(b2>=F[i]) ans+=b2-F[i]+1;
		}
		for(i=b1;i<=b2;i++){
			if(a1>=F[i]) ans+=a2-a1+1;
			else if(a2>=F[i]) ans+=a2-F[i]+1;
		}
		printf("Case #%d: %I64d\n",ic,ans);
	}
	return 0;
}
