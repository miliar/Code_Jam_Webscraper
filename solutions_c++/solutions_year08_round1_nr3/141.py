#include<cstdio>

using namespace std;

int a[100];
int b,n,i,I;

main(){
	FILE *r;
	r=fopen("c.std.txt","r");
	for (i=1;i<=30;++i) fscanf(r,"%d",&a[i]);
	scanf("%d",&n);
	for (i=0;i<n;++i) {
		scanf("%d",&b);
		printf("Case #%d: %03d\n",++I,a[b]);
	}
}
