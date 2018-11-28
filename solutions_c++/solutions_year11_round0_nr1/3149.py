#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <list>
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;


int main()
{
	int tmax,n,delta,t=0,k,temp;
	int posO,posB;
	char str[5];
	int orange[100],blue[100];
	ifstream input;
	ofstream output;
	
	input.open("A-large.in");
	output.open("output.dat");
	
	input>>tmax;
	
	for (int t1=1;t1<=tmax;t1++)
	{
		input>>n;
		
		
		for (int i=0;i<n;i++)
		{
			orange[i]=0;
			blue[i]=0;
		}
	
		for (int i=0; i<n;i++)
		{
			input>>str>>k;
			if (str[0]=='O')
				orange[i]=k;
			else
				blue[i]=k;
		}
		
		
		t=0;
		posO=1;
		posB=1;
		
		for (int i=0;i<n;i++)
		{
			if (orange[i]!=0)
			{
				delta=abs(posO - orange[i])+1;
				posO=orange[i];
				
				for (int j=i+1;j<n;j++)
				{
					if (blue[j]!=0) {temp=j;
					break;}
				}
				
				if ((i<(n-1)) && (abs(blue[temp] - posB)> delta))
					{
						if (blue[temp]>posB) posB+=delta;
						else posB-=delta;
					}
				else
					posB=blue[temp];
			}
			if (blue[i]!=0)
			{
				delta=abs(posB - blue[i])+1;
				posB=blue[i];
				
				for (int j=i+1;j<n;j++)
				{
					if (orange[j]!=0) {temp=j;
					break;}
				}
				
				if ((i<(n-1) && abs(orange[temp] - posO)> delta))
					{
						if (orange[temp]>posO) posO+=delta;
						else posO-=delta;
					}
				else
					posO=orange[temp];
				
			}
		
			t+=delta;
		}
		output<<"Case #"<<t1<<": "<<t<<"\n";
	}
	input.close();
	output.close();
	
	return 0;
}
