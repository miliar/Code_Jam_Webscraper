#include<iostream>
#include<cstdio>
#include<stdio.h>
#include<map>
#include<vector>
using namespace std;

int main()
{
 	FILE *f1;
 	f1=fopen("C-large.in","r");
 	FILE *f2;
 	f2=fopen("Output.txt","w+");
 	int t;
 	fscanf(f1,"%d",&t);
 	for(int i=1;i<=t;i++)
 	{
	 		int n;
	 		fscanf(f1,"%d",&n);
	 		int min=100000000;
	 		int sum=0,xorsum=0;
	 		for(int i=0;i<n;i++)
	 		{
			 		int x;
			 		fscanf(f1,"%d",&x);
			 		if(min>x) min=x;
			 		sum+=x;
			 		xorsum^=x;
	 		}
	 		if(xorsum!=0) fprintf(f2,"Case #%d: NO\n",i);//cout<<"Case #"<<i<<": NO";
	 		else fprintf(f2,"Case #%d: %d\n",i,sum-min);//cout<<"Case #"<<i<<": "<<sum-min;
	}
	fclose(f1);
	fclose(f2);
}
