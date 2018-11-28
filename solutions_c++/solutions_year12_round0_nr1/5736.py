// cj11.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include<iostream>
#include<algorithm>
#include<iterator>
#include<cassert>
using namespace std;
//2009 Round1bp2 - start
int mini(char data[],int j)
{
	int p=j-1;
	bool bfirst=true;
	for(int m=j; m<21; m++)
	{
		if (data[m] > data[j-1])
		{
			if (bfirst)
			{
				bfirst=false;
				p=m;
			}
			else
			{
				if (data[m]<data[p])
					p=m;
			}
		}
	}				
	return p;
			
}
void r1bp209()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		char data1[21]={0};
		char data[21]={0};
		cin>>data1;
		int k=21-strlen(data1)-1;
		strncpy(&data[21-strlen(data1)],data1,strlen(data1));
		int j=20; 
		for(;j>k+1; j--)
		{
			int p=mini(data,j);
			if (p!=j-1)
			{
				char temp=data[j-1];
				data[j-1]=data[p];
				data[p]=temp;
				std::sort(&data[j],&data[21]);
				break;
			}
		}
		if (j==k+1)
		{
			int q=j;
			for(; q<21 && data[q] == '0';q++);
			if (q==21)
			{
				data[k]='1';
				data[k+1]='0';
			}
			else
			{
				int p=q;
				for(int m=p; m<21; m++)
					if (data[m] != '0' && data[m]<data[p])
						p=m;
				data[j-1]=data[p];
				data[p]=data[j];
				data[j]='0';
				std::sort(&data[j+1],&data[21]);
			}
			k--;
		}
		cout<<"Case #"<<i<<": ";
		ostream_iterator<char> out(cout);
		copy(&data[k+1],&data[21],out);
		cout<<endl;
	}
}


//*2009 Round1bp2 - end
int cost[100][100];
int seq[100][100];
int p,q;
bool op(int &a,int&b,int i,int j,int k)
{
	a=-1;b=p+1;
	for(int m=i-1;m>=0;m--)
	{
		if (k == seq[m][j])
			return true;
		else if (seq[m][j]<k && seq[m][j]>a)
			a=seq[m][j];
		else if (seq[m][j]>k && seq[m][j]<b)
			b=seq[m][j];
	}
	return false;
}
void r1cp309()
{
	int t;
	cin>>t;
	for(int n=1;n<=t;n++)
	{
		memset(cost,0,sizeof(cost));
		memset(seq,0,sizeof(cost));
		cin>>p>>q;
		int i,j,k,l,m;
		for(j=0;j<q;j++)
		{
			cin>>seq[0][j];
			cost[0][j]=p-1;
		}
		
		for(i=1; i<q;i++)
			for(j=0;j<q;j++)
			{
				int min=p; 
				int id=0;
				for(k=0;k<q;k++)
				{
					int a,b;
					if (op(a,b,i,j,seq[0][k])) 
						continue;
					int val=0;
					if (a==-1)
						val+= seq[0][k]-1;
					else
						val+=seq[0][k]-a-1;
					
					if (b==p+1)
						val+=p-seq[0][k];
					else
						val+=b-seq[0][k]-1;
					
					if (val<=min)
					{
						min=val;
						id=seq[0][k];
					}
				}
				assert(id!=0);
				cost[i][j]=min+cost[i-1][j];
				seq[i][j]=id;
			}
		int min=cost[q-1][0];
		for(i=1; i<q;i++)
			if (cost[q-1][i] < min)
				min=cost[q-1][i];
		cout<<"Case #"<<n<<": "<<min<<endl;
	}
}


int arr[10000];
int calval(int i)
{
	int val=0;
	int j=0;
	for(j=i-1;j>=0;j--)
		if (arr[j] != 0)
			break;
	if (j == -1)
		val+= arr[i]-1;
	else
		val+= arr[i]-arr[j]-1;

	for(j=i+1;j<q;j++)
		if (arr[j] != 0)
			break;

	if (j == q)
		val+= p - arr[i];
	else
		val+= arr[j]-arr[i]-1;

	return val;
}
void r1cp309_2()
{
	int t;
	cin>>t;
	int i,j,k;
	for(int n=1;n<=t;n++)
	{
		cin>>p>>q;
		for(j=0;j<q;j++)
			cin>>arr[j];
		
		
		int cost=0;
		for(i=0; i<q;i++)
		{
			int min=p; int id=0;
			for(j=0;j<q;j++)
			{
				if (!arr[j])continue;
				int val=calval(j);
				if (val <min)
				{
					min=val;
					id=j;
				}	
			}
			arr[id]=0;
			cost+=min;
		}
		cout<<"Case #"<<n<<": "<<cost<<endl;
	}
}


//----------------
bool op_permuate(int &a,int&b,int i,int seq[],int k)
{
	a=-1;b=p+1;
	for(int m=i-1;m>=0;m--)
	{
		if (arr[k] == seq[m])
			return true;
		else if (seq[m]<arr[k] && seq[m]>a)
			a=seq[m];
		else if (seq[m]>arr[k] && seq[m]<b)
			b=seq[m];
	}
	return false;
}
int func(int i, int seq[],int k)
{
	int a,b;
	if (op_permuate(a,b,i,seq,k))
		return 0;		
	int val=0;
	if (a==-1)
		val+= arr[k]-1;
	else
		val+=arr[k]-a-1;
	
	if (b==p+1)
		val+=p-arr[k];
	else
		val+=b-arr[k]-1;
	return val;
}
void perm()
{
	int abc[]={2,4,16,18};
	int size=4;
	int tot=50;
	int min=50;
	int cost=0;
	memcpy(arr,abc,sizeof(int)*size);
	p=tot;
	for(int i=0;i<size;i++)
	{
		for(int j=0; j<size;j++)
		{
			if (i != j)
			{
				for(int k=0; k<size;k++)
				{
					if (k != j && k != i)
					{
						for(int m=0; m<size;m++)
						{	
							if (m != j && m != i && m != k)
							{
								int cost=0;
								int arr2[4]={0};
								cost+=func(0,arr2,i);
								arr2[0]=arr[i];
								cost+=func(1,arr2,j);
								arr2[1]=arr[j];
								cost+=func(2,arr2,k);
								arr2[2]=arr[k];	
								cost+=func(3,arr2,m);
								arr2[3]=arr[m];	
								cout<<i<<","<<j<<","<<k<<","<<m<<" = "<<cost<<endl;
							}
						}
					}
				}	
			}
		}
	}
}


