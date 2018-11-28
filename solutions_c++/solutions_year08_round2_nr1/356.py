#include<iostream>
#include<cstdio>
#include<vector>
#include<stdio.h>

using namespace std;
int main()
{
	int t,count;
	long long int n,a,b,c,d,x0,y0,m;
	long long int x,y;
	long long int amod,bmod,cmod,dmod;
	long long int ans,p,i,j;
	
	FILE *f1,*f2;
	f1=fopen("A-small.in","r");
	f2=fopen("A-small.out","w");
	
	fscanf(f1,"%d\n",&t);
	count=1;
	while(t--)
	{
		fscanf(f1,"%lld %lld %lld %lld %lld %lld %lld %lld\n",&n,&a,&b,&c,&d,&x0,&y0,&m);
		int val[3][3]={0};
		
		amod=a%m;
		bmod=b%m;
		cmod=c%m;
		dmod=d%m;
		
		x=x0;
		y=y0;
		
		val[ x%3 ][ y%3 ]++;
		ans=0;
		for(i=1;i<=n-1;i++)
		{
			//x=(ax+b)%m
			
			x=(  ( (amod*(x%m))%m + bmod )%m );
			y=(  ( (cmod*(y%m))%m + dmod )%m );
			
			val[ x%3 ][ y%3 ]++;
		}
		
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				if(val[i][j]>=3)
				{
					p=val[i][j];
					ans = ans + (((p * (p-1) )/2)*(p-2)/3);
				}
			}
		}
		
		for(i=0;i<3;i++)
		{
			p=val[0][i]*val[1][i]*val[2][i];
			ans = ans + p;
			
			p=val[i][0]*val[i][1]*val[i][2];
			ans=ans + p;
			
		}
		
		ans = ans + val[0][0]*val[1][2]*val[2][1];
		ans = ans + val[0][1]*val[1][2]*val[2][0];
		ans = ans + val[0][1]*val[1][0]*val[2][2];
		ans = ans + val[0][2]*val[1][0]*val[2][1];
		ans = ans + val[0][2]*val[1][1]*val[2][0];
		ans = ans + val[0][0]*val[1][1]*val[2][2];
		
		
		fprintf(f2,"Case #%d: %lld\n",count,ans);
		
		
		count++;
		
	}
	fclose(f1);
	fclose(f2);
	return 0;
}	 
				
		
		
