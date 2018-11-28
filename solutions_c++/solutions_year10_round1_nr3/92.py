#include <cstdio>
#include <algorithm>
#define LLD long long int
#define N 1000000
using namespace std;

int c,x1,x2,y1,y2,w,z;
int x[1000005],y[1000005];
int b[1000005];
long long int AC;

void add(int x,int y){
	if (y>=N) y=N;
	for (int i=y;i>0;i-=i&-i) b[i]++;
	for (int i=x-1;i>0;i-=i&-i) b[i]--;
}

int query(int x){
	int R=0;
	for (int i=x;i<=N;i+=i&-i) R+=b[i];
	return R;
}

int main(){
	x[1]=1;
	add(1,1);
	for (int i=2;i<=N;i++){
		if (query(x[i-1])==x[i-1]) x[i]=x[i-1]+1;
		else x[i]=x[i-1];
		add(x[i],x[i]+i-1);
	}
	for (int i=1;i<=N;i++) y[i]=x[i]+i-1;

	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){
		scanf("%d%d%d%d",&x1,&x2,&y1,&y2);
		AC=0;
		for (int i=x1;i<=x2;i++){
			w=max(y1,x[i]);
			z=min(y2,y[i]);
			if (z>=w) AC+=z-w+1;
		}
		printf("Case #%d: %I64d\n",tc,(LLD)(x2-x1+1)*(LLD)(y2-y1+1)-AC);
	}

	return 0;
}
