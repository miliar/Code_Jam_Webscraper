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
	int r,c,i,j,found=1;
	long int count=0;
	string str;
	scanf("%d %d",&r,&c);
	char arr[r+5][c+5];
	for(i=0;i<r;i++)
	{	cin>>str;	
		for(j=0;j<c;j++)
		{
			arr[i][j]=str[j];
			if(arr[i][j]=='#')
				count++;
		}
	}
	if(count%4!=0)
	{
		printf("\nCase #%d: ",casenr);
		printf("\nImpossible");		
		return;
	}
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			if(arr[i][j]=='#')
			{
				if((i-1)>=0 && (j-1)>=0 && arr[i-1][j-1]=='#' && arr[i-1][j]=='#' && arr[i][j-1]=='#')
				{
					arr[i-1][j-1]='/';
					arr[i-1][j]='\\';
					arr[i][j-1]='\\';
					arr[i][j]='/';
					continue;
				}
				if((i+1)<r && (j-1)>=0 && arr[i][j-1]=='#' && arr[i+1][j]=='#' && arr[i+1][j-1]=='#')
				{
					arr[i][j-1]='/';
					arr[i+1][j]='/';
					arr[i+1][j-1]='\\';
					arr[i][j]='\\';
					continue;
				}
				if((i-1)>=0 && (j+1)<c && arr[i-1][j]=='#' && arr[i-1][j+1]=='#' && arr[i][j+1]=='#')
				{
					arr[i-1][j]='/';
					arr[i-1][j+1]='\\';
					arr[i][j+1]='/';
					arr[i][j]='\\';
					continue;
				}
				if((i+1)<r && (j+1)<c && arr[i+1][j+1]=='#' && arr[i+1][j]=='#' && arr[i][j+1]=='#')
				{
					arr[i+1][j+1]='/';
					arr[i+1][j]='\\';
					arr[i][j+1]='\\';
					arr[i][j]='/';
					continue;
				}
				found=0;				
				break;
				
			}
		}
	if(found==0)
		break;
	}
	if(found==0)
	{		
		printf("\nCase #%d: ",casenr);
		printf("\nImpossible");			
		return;
	}	
	printf("\nCase #%d: ",casenr);
	for(i=0;i<r;i++)
		{		
		printf("\n");
		for(j=0;j<c;j++)
			printf("%c",arr[i][j]);
		}
}

int main() {
	freopen("in","r",stdin);
	int num; scanf("%d",&num); 
	freopen("success","w",stdout); 
	for(int i=1;i<=num;i++)	
	{
	run(i);
	}
	return 0;
}

 
