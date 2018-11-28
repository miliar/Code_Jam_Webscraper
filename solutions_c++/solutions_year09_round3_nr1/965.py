#include <stdio.h>
#include <string.h>
#include <math.h>
FILE * in = fopen("input.txt","r");
FILE * out = fopen("output.txt","w");
int d[100];
int main(){
	int T,i,j,k,len,Base,V,cnt;
	int inp[1000];
	char str[1000];

	fscanf(in,"%d",&T);
	
	for(k=1;k<=T;k++){
		fscanf(in,"%s",&str);
		len=strlen(str);
		for(i=0;i<40;i++)d[i]=0;
		
		for(i=0;i<len;i++){
			if ( '0'<=str[i] && str[i]<='9'){
				d[str[i]-'0']++;
				inp[i]=str[i]-'0';
			}
			else if( 'a'<=str[i] && str[i]<='z'){
				d[str[i]-'a'+10]++;
				inp[i]=str[i]-'a'+10;
			}
		}
		Base=0;
		for(i=0;i<40;i++){
			if (d[i])Base++;
			d[i]=-1;
		}
		if (Base<=1)Base=2;
		V=0;
		cnt=0;
		for(i=0;i<len;i++){
			if (d[inp[i]]==-1){
				if (i==0)
					d[inp[i]]=1;
				else if (cnt==0){
					d[inp[i]]=0;
					cnt=2;
				}
				else{
					d[inp[i]]=cnt++;
				}
			}
			V+=pow((double)Base,len-i-1)*d[inp[i]];
		}
		fprintf(out,"Case #%d: %d\n",k,V);
	}
	return 0;
}