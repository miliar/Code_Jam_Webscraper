#include<iostream>
#include<cstdio>
using namespace std;

#define FRR(i,p,n) for(int i=p; i<(int)n; i++)

int main()
{
	int t=0;
	cin>>t;
	
	int h=t;
	while(t--){
		
		int n=0;
		long long int k=0;
	
		cin>>n;
		cin>>k;
		
		int snapper[30];
	
		FRR(i,0,30){
		   snapper[i]=0;
		}
	
		FRR(i,0,n){
			long long int div=1;
			
			div=div << i+1;
			
			if(k%div >= div/2){
				snapper[i]=1;
			}
		}
		int fg=1;

		FRR(i,0,n){
			if(snapper[i]==0){
				fg=0;
			}
		}
		if(fg){
			printf("Case #%d: ON\n",h-t);
		}else{
			printf("Case #%d: OFF\n",h-t);
		}
	}

	return 0;
}

