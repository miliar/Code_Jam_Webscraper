#include<iostream>
#include<cstdio>
using namespace std;

int main(){
int t,n,s,p,i,count,cc;
FILE *fin;
FILE* fo;
fin=fopen("C.in","r");
fo=fopen("C.out","w");
fscanf(fin,"%d",&t);
for (i=0;i<t;i++){
	count=0,cc=0;
	fscanf(fin,"%d %d %d",&n,&s,&p);
	int sum[n],k[n];
	for (int j=0;j<n;j++){
		fscanf(fin,"%d ",&sum[j]);
	}
	//printf("%d %d %d \n",n,s,p);
	
	for (int j=0;j<n;j++){
		k[j]=sum[j]/3;
		
		if(sum[j]%3==0 && sum[j]!=0 && sum[j]!=30){
			if(k[j]>=p){
				count+=1;
			}
			else if(k[j]==p-1){
				cc+=1;
			}
		}
		else if(sum[j]%3==1 && sum[j]!=1 ){
			if(k[j]+1>=p){
				count=count+1;
			}
		}
		else if(sum[j]%3==2 && sum[j]!=29){
			if(k[j]+1>=p){
				count+=1;
			}
			else if(k[j]==p-2){
				cc+=1;
			}
		}
		if(sum[j]==0){
			if(p==0){
				count=count+1;
			}
		}
		if(sum[j]==30 || sum[j]==29){
			if(p<=10){
				count=count+1;
			}
		}if(sum[j]==1){
			if(p<=1){
				count=count+1;
			}
		}
	}
	//printf("count: %d, cc %d, s %d \n",count,cc,s);
	if(cc>s){
		count=count+s;
	}
	else if(cc<=s){
		count=count+cc;
	}
	fprintf(fo,"Case #%d: %d\n",i+1,count);
}
fclose(fin);
fclose(fo);
return 0;
}
