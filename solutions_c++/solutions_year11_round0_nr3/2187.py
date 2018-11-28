#include<stdio.h>
#include<string.h>
inline int abs(int a){
	if(a<0)return -a;
	else return a;
}
#define max(a,b) ((a>b) ? (a) : (b))
int solve(){
	int n,i;
	int xor=0,mini=0,sum=0;
	int a[1024];
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",a+i);
		xor=xor^a[i];
		if(a[i]<a[mini])mini=i;
		sum+=a[i];
	}

	if(xor){
		printf("NO");
		return 1;
	}
	printf("%d",sum-a[mini]);



	return 0;
}
int main(){
	int t;
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	scanf("%d",&t);
	for(int I=1;I<=t;I++){
		printf("Case #%d: ",I);
		solve();
		putchar('\n');
	}
	return 0;
}