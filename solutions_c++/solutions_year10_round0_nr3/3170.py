#include<iostream>
#include<stdio.h>
#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<numeric>

using namespace std;

int main()
{
	int test,r,k,n;
	scanf("%d",&test);
	int i;
	for(i=1;i<=test;i++){
		int money=0,counter=0,j,t=0,l,tmp=0;	
		vector<int>v;
		
		scanf("%d%d%d",&r,&k,&n);
		
		int a[n+1];
		
		for(j=0;j<n;j++)
			scanf("%d",&(a[j]));

		int acc=accumulate(a,a+n,0);
		if(k>acc)
			printf("Case #%d: %d\n",i,acc*r);
		else{
		
			int b[n+1];

			memset(b,-1,sizeof(b));
			int cp=-1;
			while(1){
				counter++;
				for(l=t;;l++){
					if(l>=n)
						l=l%n;
					tmp+=a[l];
					if(tmp>k)
						break;
				}
				t=l;
				if(b[t]!=-1){
					
					v.push_back(tmp-a[t]);
					break;
				}
				cp++;
				b[t]=cp;
				v.push_back(tmp-a[t]);
			
				tmp=0;
			}
			
			acc=0;
			int bk=v.size();
			for(int h=b[t]+1;h<bk;h++)
				acc+=v[h];
				
			if(r>=counter){
				int sum=accumulate(v.begin(),v.end(),0);
				int sub=b[t]+1;
				if((r-sub)!=(bk-sub)){
					money+=((r-sub)/(bk-sub))*acc+(sum-acc);
					bk=(r-sub)%(bk-sub);
				}
				else{
					money+=sum;
					bk=0;
				}
			}
			else{
				bk=r;
				t=0;
			}
			for(int h=0;h<bk;h++){
				tmp=0;	 
 				for(l=t	;;l++){
	               	        if(l>=n)
                       	                 l=l%n;
                       	         tmp+=a[l];
                       	         if(tmp>k)
                        	                break;
                          	}
				money+=(tmp-a[l]);
				t=l;
		
			}

		printf("Case #%d: %d\n",i,money);
		}
	}
}
			
		
			
		
			
		
	
