#include <cstdio>
#include <iostream>
using namespace std;

int main(){
	long cc,tt;
	long r,k,n,i;
	long g[1111],sum;
	long g20[1111];
	long t[1111];
	long long ans;
	long long sumweight;
	long nowpos,thisweight;
	scanf("%d",&tt);
	
	for(cc=0;cc<tt;cc++){
		
		scanf("%d%d%d",&r,&k,&n);
		sum=0;
		for(i=0;i<n;i++){
			scanf("%d",&g[i]);
			sum+=g[i];
		}

		i=0;
		g20[0]=0;
		for(i=0;i<20;i++)
			g20[0]+=g[i];
		i=1;
		while(i<n-20){
			g20[i]=g20[i-1]+g[i+20]-g[i-1];
			i++;	
		}

		if(sum<=k){
			ans=sum*(long long )r;
		}else{
			
			nowpos=0;
			long tp;
			tp=0;

			sumweight=0;
			do{
					thisweight=0;
					while((nowpos<n-20)&&thisweight+g20[nowpos]<=k){
						thisweight+=g20[nowpos];
						nowpos+=20;
					}

					while(thisweight+g[nowpos]<=k){
						thisweight+=g[nowpos];
						nowpos++;

						if(nowpos==n){
							nowpos=0;
						}
					}

					t[tp++]=thisweight;
					sumweight+=thisweight;

			}while(nowpos&&tp<=r);

			ans=(r/tp)*sumweight;

			for(i=0;i<r%tp;i++){
				ans+=t[i];
			}

			
		}

		cout<<"Case #"<<cc+1<<": "<<ans<<endl;

	}

	return 0;
}