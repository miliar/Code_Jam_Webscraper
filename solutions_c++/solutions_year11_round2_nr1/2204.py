#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list> 
using namespace std;  

void run(int casenr) {
	int n;
	scanf("%d",&n);
	char arr[n+5][n+5];
	float wp[n+5];
	float owp[n+5];
	float oowp[n+5];
	float cnt,tot,res,avg;
	string str;
	int i,j,k;	
	for(i=0;i<n;i++)
		{
		cnt=tot=0;
		cin>>str;
		for(j=0;j<n;j++)
			{
			arr[i][j]=str[j];
			if(arr[i][j]=='1')
				cnt++;
			if(arr[i][j]=='1' || arr[i][j]=='0')
				tot++;						
			}
		wp[i]=cnt/tot;
		//printf("%f\n",wp[i]);
		}
	for(i=0;i<n;i++)
		{
		res=0;
		avg=0;
		for(j=0;j<n;j++)
			{
			if((j==i) || (arr[i][j]=='.'))
				continue;
			cnt=tot=0;
			for(k=0;k<n;k++)
				{
					if(k!=i)
					{
					if(arr[j][k]=='1')
						cnt++;
					if(arr[j][k]=='1' || arr[j][k]=='0')
						tot++;			
					}
				}
			avg++;
			res=res+(cnt/tot);			
			}
		owp[i]=res/avg;
		}
	for(i=0;i<n;i++)
		{
		res=0;
		avg=0;
		for(j=0;j<n;j++)
			{
				if(arr[i][j]=='0' || arr[i][j]=='1')
				{
					res=res+owp[j];
					avg++;
				}
			}
		oowp[i]=res/avg;
		}	
	printf("\nCase #%d: ",casenr);
	for(i=0;i<n;i++)
	{
		res=(0.25 * wp[i]) + (0.50 * owp[i]) + (0.25 * oowp[i]);
		printf("\n%f",res);
		
	}
}

int main() {
	int num; scanf("%d",&num); 
freopen("success","w",stdout); 
	for(int i=1;i<=num;i++)	
	{
	//printf("\n");
	run(i);
	}
	return 0;
}

 
