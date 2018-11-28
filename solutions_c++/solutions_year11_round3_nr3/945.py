/*
 *  harmony.cpp
 *  
 *
 *  Created by Shobhit Srivastava on 22/05/11.
 *  Copyright 2011 IIT Rajisthan. All rights reserved.
 *
 */



#include <vector>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <math.h>

using namespace std;
int fre[10000];
int main() 
{
	freopen("C-small.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for(int test=1;test<=t;test++) 
	{
		int n,l,h,i,j,flag=0;
		scanf("%d %d %d",&n,&l,&h);
		for(i=0;i<n;i++)
		{
			cin>>fre[i];
			//scanf("%d ",fre[i]);
		}
		for(i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
			{
				if((fre[j]%i)!=0)
					if((i%fre[j])!=0)
						break;
				if(j==(n-1))
					flag=1;
			}
			if(flag==1)
				break;
		}
		if(flag==1)
			cout<<"Case #"<<test<<": "<<i<<endl;
		else
			cout<<"Case #"<<test<<": NO"<<endl;
	}
}