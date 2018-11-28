#include<stdio.h>


int main(){
int i,j,n,l,h,t,flag,k,error;
int a[100000];
FILE *pt=fopen("out.txt","w");
scanf("%d",&t);
			for(i=0;i<t;i++){
			scanf("%d %d %d",&n,&l,&h);
			
			for(j=0;j<n;j++){
			scanf("%d",&a[j]);
			}
			for(j=l;j<=h;j++){flag=0;
			for(k=0;k<n;k++){
			if(a[k]%j==0){
			flag=0;
			}
			else if(j%a[k]==0)
			flag=0;
			else{
			flag=1;break;}
			}
			
			if(flag==0){error=0;
			break;}
			else
			error=1;
			
			}
			
			
			
			
			
			
			
								if(error==1)
			fprintf(pt,"Case #%d: NO\n",i+1);
			else{
			fprintf(pt,"Case #%d: %d\n",i+1,j);
	
			}
			}

}
