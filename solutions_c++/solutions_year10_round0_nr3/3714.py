#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
	unsigned long long int res,sum,min;
	int r,k,n,i,j,t,T;
	int num[1010];

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
			j=-1;
			while(r--){
				sum=0;
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
				res=res+sum;
			}
		}

		printf("Case #%d: %llu\n",t,res);
	}

	return 0;
}



