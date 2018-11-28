#include<iostream>
#include<math.h>
using namespace std;
int main(){
	FILE *in=fopen("A-large.in","r"),*out=fopen("A-large.out","w");
	int T,n,k,t;
	fscanf(in,"%d",&T);
	for(int i=1;i<=T;i++){
		fscanf(in,"%d%d",&n,&k);
		k++;
		t=(int)floor(pow(2,n)+0.5);
		printf("Case #%d: %s\n",i,k%t?"OFF":"ON");
		fprintf(out,"Case #%d: %s\n",i,k%t?"OFF":"ON");
	}
	system("pause");
	return 0;
}
