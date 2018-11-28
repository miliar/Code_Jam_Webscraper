#include<stdio.h>
#include<string.h>
int main(){
	FILE *fi=fopen("input.in","r");
	FILE *fo=fopen("output.out","w");
	char a[1005],tl[30]={'Y','H','E','S','O','C','V','X','D','U','I','G','L','B','K','R','Z','T','N','W','J','P','F','M','A','Q'},ts[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int i,len,n,cnt=0;
	fscanf(fi,"%d\n",&n);
	while(1){
		if(cnt==n) break;
		fgets(a,105,fi);
		len=strlen(a);
		fprintf(fo,"Case #%d: ",cnt+1);
		for(i=0;i<len;i++){
			if(a[i]>='A' && a[i]<='Z') fprintf(fo,"%c",tl[a[i]-'A']);
			else if(a[i]>='a' && a[i]<='z') fprintf(fo,"%c",ts[a[i]-'a']);
			else fprintf(fo,"%c",a[i]);
		}
		cnt++;
	}
	return 0;
}
