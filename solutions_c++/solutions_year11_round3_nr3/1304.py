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

long long int euclid(long long int a,long long int b)
{
   if(b==0)
        return a;
   else
        return euclid(b,a%b);
}

long long int lcm(long long int a,long long int b)
{
	long long int res=(a*b)/euclid(a,b);
}
void run(int casenr) {
	long long int n,l,h,i,res,j;
	int found=0;
	scanf("%lld %lld %lld",&n,&l,&h);
	long long int arr[n+5];
	for(i=0;i<n;i++)
		scanf("%lld",&arr[i]);
	if(l==1)
	{
		printf("\nCase #%d: 1",casenr);
		return;
	}	
	for(i=l;i<=h;i++)
		{
		found=0;
		for(j=0;j<n;j++)
		{
			if(i%arr[j]==0 || arr[j]%i==0)
			{
			found++;	
			}
		}
		if(found==n)
			break;
		}
	if(found==n)
			printf("\nCase #%d: %lld",casenr,i);
	else
			printf("\nCase #%d: NO",casenr);	
}

int main() {
	int num; scanf("%d",&num); 
	freopen("success","w",stdout); 
	for(int i=1;i<=num;i++)	
	{
	run(i);
	}
	return 0;
}

 
