#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <list>
#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
using namespace std;


int main()
{
	int tmax,n,temp1[2],temp2[2],res,p=0,r,total;
	int a[15];
	vector<int> x;
	ifstream input;
	ofstream output;
	
	input.open("C-small-attempt1.in");
	output.open("output.dat");
	
	input>>tmax;
	
	for (int t1=1;t1<=tmax;t1++)
	{
		x.clear();
		res=0;
		temp1[0]=0,temp1[1]=0;
		temp2[0]=0; temp2[1]=0;
		input>>n;
		for (int i=0; i<n;i++)
		{
			input>>a[i];
			x.push_back(0);
		}
		
		p=int(pow(2,n));
		
		for (int i=0; i<p; i++)
		{	
			r=1;
			total=0;
			for (int j=n-1;j>=0;j--)
			{if (r==1)
			{
				if (x[j]==1) {x[j]=0; r=1;total++;}
				else {x[j]=1; r=0;}
			}
			}
		
			temp1[0]=0,temp1[1]=0;
			temp2[0]=0; temp2[1]=0;

			for (int j=0; j<n; j++)
			{
				if (x[j]==1)
					{temp1[0]=temp1[0] ^ a[j];
					temp1[1]=temp1[1] + a[j];}
				else 
				{temp2[0]=temp2[0] ^ a[j];
				temp2[1]=temp2[1] + a[j];}
			}
			if (temp1[0]==temp2[0] && (total!=n && total!=0))
			{if (temp2[1]>=temp1[1] && temp2[1]>res) res= temp2[1];
			if (temp2[1]<temp1[1] && temp1[1]>res) res=temp1[1];}
		}
		
		if (res!=0) output<<"Case #"<<t1<<": "<<res<<"\n";
		else output<<"Case #"<<t1<<": NO\n";
		
	}
	input.close();
	output.close();
	
	return 0;
}
