#include <iostream>
using namespace std;

int main()
{
	unsigned long long int res,sum,min,temp[1010];
	int num[1010],xyz[1010];
	int t,r,i,j,x,k,n,T,p,q,count;

	scanf("%d",&T);

	for(t=1;t<=T;t++){
		scanf("%d%d%d",&r,&k,&n);

		min=0;
		for(i=0;i<n;i++){
			scanf("%d",&num[i]);
			min=min+num[i];
		}

		if(min<=k)
			res=min*r;
		else{
			res=0;
			for(i=0;i<n;i++)
				temp[i]=0;

			i=0;
			j=-1;
			q=0;

			while(i<r){
				sum=0;
				
				p=(j+1)%n;

				while(1){
					j=(j+1)%n;
					sum=sum+num[j];
					if(sum>=k){
						if(sum>k){
							sum=sum-num[j];
							j=j-1;
						}
						break;
					}
				}

				temp[p]=sum;
				xyz[p]=(j+1)%n;

				res=res+sum;

				i=i+1;
				
				q=xyz[p];
					
				if(temp[q])
					break;
			}
			
			if(i<r){
				if(q==0){
					x=r/i;
					i=i*x;
					res=res*x;
				
					j=0;
					while(i<r){
						res=res+temp[j];
						j=xyz[j];
						i++;
					}
				}else{
					while(i<r){
						res=res+temp[q];
						q=xyz[q];
						i++;
					}
				}
			}
		}

		printf("Case #%d: %llu\n",t,res);
	}

	return 0;
}

