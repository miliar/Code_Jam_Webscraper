#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	FILE * r = fopen("A-large.in","r");
	FILE * w = fopen("dfdf.txt","w");
	int t;
	fscanf(r,"%d",&t);
	int d[10010],l[10010];
	int dp[10010];
	
	int n,len;
	for(int cas =1; cas<=t;cas++)
	{
		fscanf(r,"%d",&n);
		for(int i=0;i<n;i++){
			fscanf(r,"%d%d",&d[i],&l[i]);
		}		
		fscanf(r,"%d",&len);
		memset(dp,0,sizeof(dp));
		dp[0]=2*d[0];
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
				if(d[j]<=dp[i] )
					dp[j]=max(dp[j],min(2*d[j]-d[i],d[j]+l[j]));
		}	
		bool s = false;
		for(int i=0;i<n;i++)
			if(dp[i]>=len)
				s = true;
		fprintf(w,"Case #%d: ",cas);
		if(s)
			fprintf(w,"YES\n");
		else fprintf(w,"NO\n");
	}
	fclose(w);
	fclose(r);
}
