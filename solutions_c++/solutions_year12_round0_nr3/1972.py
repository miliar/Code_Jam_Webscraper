#include<string.h>
#include<stdio.h>
#include<stdlib.h>

int main(){
	int i,j,k=0,n,min,max,temp,e;
	char data[20],to;
	freopen("C-large.in","r",stdin);
	//freopen("re")
	freopen("result.txt","w",stdout);
	scanf("%d",&n);
	for(e=0;e<n;e++){
		k=0;
	scanf("%d%d",&min,&max);
	for(i=min;i<=max;i++)
		{
			temp=i;
			//data=itoa(i);
			itoa(temp,data,10);
			while(1){
				to=data[0];
			for(j=0;j<strlen(data)-1;j++)
			{
				data[j]=data[j+1];	
			}
			data[j]=to;
			temp=atoi(data);
			if(temp==i)
				break;
			if((temp>=min)&&(temp<=max))
				k++;
			}
			
			
		}
			printf("Case #%d: ",e+1);
			printf("%d\n",k/2);
	}

	
	
}