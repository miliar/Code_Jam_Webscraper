#include <stdio.h>
#include <string.h>
FILE * in = fopen("input.txt","r");
FILE * out = fopen("output.txt","w");
int d[1000][20],n,len;
char str[20]="welcome to code jam";
char inp[1000];
char outp[5];
int main(){
	int k,i,j;
	fscanf(in,"%d\n",&n);
	
	for(k=1;k<=n;k++){
		fgets(inp,1000,in);
		len=strlen(inp);
		for(i=0;i<=len;i++)d[i][0]=1;

		for(i=1;i<=len;i++){
			for(j=1;j<=19;j++){
				if (str[j-1]==inp[i-1])
					d[i][j]=d[i-1][j]+d[i-1][j-1];	
				else
					d[i][j]=d[i-1][j];
				d[i][j]%=10000;
			}
		}
		strcpy(outp,"0000");
		outp[0]+=(d[len][19]/1000)%10;
		outp[1]+=(d[len][19]/100)%10;
		outp[2]+=(d[len][19]/10)%10;
		outp[3]+=(d[len][19]/1)%10;
		fprintf(out,"Case #%d: %s\n",k,outp);
	}
	
	return 0;
}