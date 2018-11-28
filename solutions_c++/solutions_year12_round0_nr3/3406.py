#include "stdio.h"
#include "string.h"

int main(void){
	char buf[100];
	int t;
	int a[50];
	int b[50];
	int i;
	int j;
	int k;
	int l;
	int m;
	int score[50];
	FILE *fp;

	fp=fopen("C-small-attempt0.in","r");
	
	fgets(buf,100,fp); 
	sscanf(buf,"%d",&t);

	for(i=0;i<t;i++){
		fgets(buf,100,fp); 
		sscanf(buf,"%d %d",&a[i],&b[i]);
	}
	
	for(i=0;i<t;i++){
		score[i]=0;
	}

	for(i=0;i<t;i++){
		if(a[i]>0 && b[i]<10){
			score[i]=0;
		}else if(a[i]>=10 && b[i]<100){
			for(j=a[i]/10;j<(b[i]/10)+1;j++){
				for(k=0;k<10;k++){
					if(a[i] <= j*10+k && j*10+k < k*10+j &&  k*10+j <= b[i]){
						score[i]++;
					}
				}
			}
		}else if(a[i]>=100 && b[i]<1000){
			for(j=a[i]/100;j<(b[i]/100)+1;j++){
				for(k=0;k<10;k++){
					for(l=0;l<10;l++){
						if(a[i] <= j*100+k*10+l && j*100+k*10+l < l*100+j*10+k && l*100+j*10+k <= b[i]){
							score[i]++;
						}
						if(a[i] <= j*100+k*10+l && j*100+k*10+l < k*100+l*10+j && k*100+l*10+j <= b[i] && l*100+j*10+k != k*100+l*10+j){
							score[i]++;
						}
					}
				}
			}
		}else if(a[i]>=1000 && b[i]<10000){
			for(j=a[i]/1000;j<(b[i]/1000)+1;j++){
				for(k=0;k<10;k++){
					for(l=0;l<10;l++){
						for(m=0;m<10;m++){
							if(a[i] <= j*1000+k*100+l*10+m && j*1000+k*100+l*10+m < m*1000+j*100+k*10+l && m*1000+j*100+k*10+l <= b[i]){
								score[i]++;
							}
							if(a[i] <= j*1000+k*100+l*10+m && j*1000+k*100+l*10+m < l*1000+m*100+j*10+k && l*1000+m*100+j*10+k <= b[i] && m*1000+j*100+k*10+l != l*1000+m*100+j*10+k){
								score[i]++;
							}
							if(a[i] <= j*1000+k*100+l*10+m && j*1000+k*100+l*10+m < k*1000+l*100+m*10+j && k*1000+l*100+m*10+j <= b[i] && m*1000+j*100+k*10+l != k*1000+l*100+m*10+j && l*1000+m*100+j*10+k != k*1000+l*100+m*10+j){
								score[i]++;
							}
						}
					}
				}
			}
		}
	}

	fp=fopen("result.txt","w");

	for(i=0;i<t;i++){
		fprintf(fp,"Case #%d: %d\n",i+1,score[i]);
	}

	fclose(fp);

	return 0;
}



