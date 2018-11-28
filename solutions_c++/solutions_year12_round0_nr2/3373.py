#include "stdio.h"
#include "string.h"

int main(void){
	char buf[100];
	int t;
	int	n[100];
	int s[100];
	int p[100];
	int ti[100][100];
	int i;
	int j;
	int count[100];
	
	FILE *fp;

	fp=fopen("B-large.in","r");
	 
	fscanf(fp,"%d",&t);

	for(i=0;i<t;i++){
		fscanf(fp,"%d %d %d",&n[i],&s[i],&p[i]);
		for(j=0;j<n[i];j++){
			fscanf(fp,"%d",&ti[i][j]);
		}
	}
	
	fclose(fp);
	
	for(i=0;i<t;i++){
		count[i]=0;
	}
	
	for(i=0;i<t;i++){
		for(j=0;j<n[i];j++){
			if(ti[i][j]==0){
				if(p[i]==0){
					count[i]++;
				}
				continue;
			}
			if(ti[i][j]==1){
				if(p[i]<=1){
					count[i]++;
				}
				continue;
			}else if(ti[i][j]==2){
				if(p[i]<=1){
					count[i]++;
				}else if(p[i]==2 && s[i]>0){
					count[i]++;
					s[i]--;
				}
				continue;
			}
			if(ti[i][j]%3==0){
				if((ti[i][j]/3)>=p[i]){
					count[i]++;
				}else if((ti[i][j]/3)==p[i]-1 && s[i]>0){
					count[i]++;
					s[i]--;
				}
			}else if(ti[i][j]%3==1){
				if(((ti[i][j]/3)+1)>=p[i]){
					count[i]++;
				}
			}else if(ti[i][j]%3==2){
				if(((ti[i][j]/3)+1)>=p[i]){
					count[i]++;
				}else if(((ti[i][j]/3)+1)==p[i]-1 && s[i]>0){
					count[i]++;
					s[i]--;
				}
			}
		}
	}

	fp=fopen("result.txt","w");

	for(i=0;i<t;i++){
		fprintf(fp,"Case #%d: %d\n",i+1,count[i]);
	}

	fclose(fp);
	
	/*
	printf("%d \n",t);
	for(i=0;i<t;i++){
		printf("%d %d %d ",n[i],s[i],p[i]);
		for(j=0;j<n[i];j++){
			printf("%d ",ti[i][j]);
		}
		printf("\n");
	}
	*/
	
	return 0;
}