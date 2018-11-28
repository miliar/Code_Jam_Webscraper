/*
	Minimum Scalar Product
	Small Input
	Google Code Jam '08 - Round 1
	-trisha
	26th July 2008
*/

#include<stdio.h>
#include<string.h>
#include<conio.h>
#include<iostream.h>

#define V_MAX 8

int v1[V_MAX], v2[V_MAX], v3[V_MAX], num;

void sort()
{
	int i,j, temp, min, max;

	for(i=0; i<(num-1); i++)
	{
		min=i;

		for(j=i+1; j<num; j++)
		{
			if(v1[j]<v1[min])
				min=j;
		}
		temp=v1[i];
		v1[i]=v1[min];
		v1[min]=temp;
	}

	for(i=0; i<(num-1); i++)
	{
		max=i;

		for(j=i+1; j<num; j++)
		{
			if(v2[j]>v2[max])
				max=j;
		}
		temp=v2[i];
		v2[i]=v2[max];
		v2[max]=temp;
	}
}         

void main()
{
	int n, cases, n1, pdt;

	cin>>cases;

	for(n=1;n<=cases;n++)
	{
 		cin>>num;

		pdt=0;
		for(n1=0; n1<V_MAX; n1++)
		{
			v1[n1]=0;
			v2[n1]=0;
		}
      
		for(n1=0; n1<num; n1++)
			cin>>v1[n1];
	
		for(n1=0; n1<num; n1++)
			cin>>v2[n1];
	
		sort();

		for(n1=0; n1<num; n1++)
			pdt+=v1[n1]*v2[n1];
		
		cout<<"Case #"<<n<<": "<<pdt<<"\n";
	}
}




