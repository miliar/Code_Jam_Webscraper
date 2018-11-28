#include<iostream>
#include<stdio.h>
using namespace std;
int sum[101];
int main(){
	int t,cas;
	int n,s,p,i,k,m;
	int num;
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		num=0;
		scanf("%d %d %d",&n,&s,&p);
		for(i=0;i<n;i++){
			scanf("%d",&sum[i]);
			k=sum[i]/3;
			m=sum[i]%3;
			if(k>=p)
				num++;
			else{
				if(m==0&&k>0){
					k++;
					if(k==p&&s>0){
						s--;
						num++;
					}
				}
				if(m==1){
					k++;
					if(k==p)
						num++;
				}
				if(m==2){
					k++;
					if(k==p)
						num++;
					else{
						k++;
						if(s>0&&k==p){
							s--;
							num++;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",cas,num);
	}
	return 0;
}
 




	
	


	

