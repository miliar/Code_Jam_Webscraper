#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <cstdio>
#include <climits>
#include <cmath>
using namespace std;

int search(int A,int B)
{
	int x=max(A,B);
	int y=min(A,B);
//	fprintf(stderr,"%d,%d > ",x,y);
	if(x==y)
		return 1;
	
	int res=-1;
	int r=x%y;
	if(r==0)
	{
		res=search(y,r+y);
	}
	else if(r+y<x)
	{
		res=search(y,r);
		if(res%2==0)
			res++;
	}
	else
	{
		res=search(y,r);
	}
	return res+1;
}

int main()
{
	int T; cin>>T;
	for(int ds=1;ds<=T;ds++)
	{
		int A1,A2,B1,B2; cin>>A1>>A2>>B1>>B2;
		
		int ans=0;
		for(int b=B1;b<=B2;b++)
		for(int a=A1;a<=A2;a++)
		{
//			fprintf(stderr,"(%d,%d):  ",a,b);
			
			int res=search(a,b);
//			fprintf(stderr,"(%d)\n",res);
			if(res%2==0)
				ans++;
		}
		printf("Case #%d: %d\n",ds,ans);
		fprintf(stderr,"-------------------------------\n");
	}
	return 0;
}
