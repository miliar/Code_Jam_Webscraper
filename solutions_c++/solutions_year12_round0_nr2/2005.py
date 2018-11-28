#include<iostream>
#include<string.h>
#include<stdio.h>

using namespace std;

bool isSur(int s,int p)
{
	if(s%3==0 && s && s!=30){
		return s/3+1>=p;	
	}
	else if(s%3==1 && s>1){
		return s/3+1>=p;
	}
	else if(s%3==2 && s!=29){
		return s/3+2>=p;
	}
	return false;
}
bool canSur(int s)
{
	if(s%3==0 && s && s!=30)
		return true;
	if(s%3==1 && s>1)
		return true;
	if(s%3==2 && s!=29)
		return true;
	return false;
}
bool isNotSur(int s,int p)
{
	if(s%3==0){
		return s/3>=p;	
	}
	else if(s%3==1){
		return s/3+1>=p;	
	}
	else{
		return s/3+1>=p;
	}
}

int main()
{
	int dp[110][110];
	int cas = 1;
	
	FILE * r = fopen("B-large.in","r");
	FILE * w = fopen("ans.txt","w");
	fscanf(r,"%d",&cas);
	int a[110];
	
	
	for(int cc = 1; cc <= cas ; cc++)
	{
		memset(dp,0,sizeof(dp));
		int ans;
		int n,s,p;
		fscanf(r,"%d%d%d",&n,&s,&p);
		for(int i=1;i<=n;i++)
			fscanf(r,"%d",&a[i]);		
		
		for(int i=1;i<=n;i++)
		{
			for(int j=0;j<i && j<=s;j++){
				dp[i][j] = max(dp[i][j],dp[i-1][j]);
				if(canSur(a[i])){
					dp[i][j+1]=max(dp[i][j+1],dp[i-1][j]);
				}
					if(isSur(a[i],p)){
						dp[i][j+1]=max(dp[i][j+1],dp[i-1][j]+1);
					}
					
				if(isNotSur(a[i],p)){
					dp[i][j]=max(dp[i][j],dp[i-1][j]+1);	
				}
			}
		}	
		ans = dp[n][s];
		fprintf(w,"Case #%d: %d\n",cc,ans);
	}

	
}