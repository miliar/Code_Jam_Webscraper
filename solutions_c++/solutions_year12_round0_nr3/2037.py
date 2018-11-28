#include<iostream>
#include<string.h>
#include<stdio.h>

using namespace std;

bool dp[2000010];

int getTen(int m)
{
	int n = 1;
	while(m/n)
		n*=10;
	return n;
}
int main()
{
	int cas,cc;
	
	FILE * r = fopen("C-large.in","r");
	FILE * w = fopen("ans.txt","w");
	
	fscanf(r,"%d",&cas);
	
	for(cc=1;cc<=cas;cc++){
		
		memset(dp,0,sizeof(dp));
		int a,b;
		int ans = 0;
		fscanf(r,"%d%d",&a,&b);
		
		for(int i=a;i<=b;i++){
			if(!dp[i]){
				int t = 1;
				int n = 1;
				int m = getTen(i);
				while(i/n){
					int j = i/n+i%n*m;
					if(j>i && j<=b && !dp[j]){
						dp[j]=true;
						t++;
					}
					n*=10;	
					m/=10;
				}
				if(t>1)
				//cout<<i<<" "<<t<<endl;
				ans+=t*(t-1)/2;
			}
		}
		fprintf(w,"Case #%d: %d\n",cc,ans);
	}	
	
}