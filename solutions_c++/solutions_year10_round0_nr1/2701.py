#include<stdio.h>

FILE *inf=fopen("A-small.in","r"),*ouf=fopen("A-small.out","w");
int n,a,b,o,c,i;

main(){
	fscanf(inf,"%d",&n);
	while(n--){
		fscanf(inf,"%d%d",&a,&b);
		for(c=1,i=0;i<a&&c;i++,b>>=1)c=b&1;
		fprintf(ouf,"Case #%d: O%s\n",++o,(c?"N":"FF"));
	}
}
