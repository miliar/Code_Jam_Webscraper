#include<stdio.h>
#include<iostream>
#include<stdlib.h>
using namespace std;
main()
{
	long long int testcases,N,i,j,l,flag;//testcases is the # of testcases N is number of groups 
	long long int R,k,p,sum; // R is the number of rides ; k is the size of roller caster 
	cin >> testcases;	
	for(i=0;i<testcases;i++)
	{
		p=0;
		flag=0;
		long long int *sums,*A,*B;
		cin >> R;cin >> k;cin >>N;
		A=(long long int *)malloc(sizeof(long long int)*N);
		B=(long long int *)malloc(sizeof(long long int)*N);
		sums=(long long int *)malloc(sizeof(long long int)*N);
		for(j=0;j<N;j++)
		{
			cin >> A[j];
		}
		for(j=0;j<N;j++)
		{
			sum=0;
			for(l=j;l<N;l++)
			{
				sum=sum+A[l];
				if(sum>k)
				{    sums[j]=sum-A[l];B[j]=l-1;break;}			
				if(A[l]>k)
				{flag=2;break;}
			}	
			if(flag==2)
				break;
			if(j==0&&sum<=k)
			{
				p=0;
				for(l=0;l<R;l++)
				p=p+sum;
				flag=1;
	//			cout << "Case #"<<i+1<<":  "<< p<< endl;
				break;
			}
			if(sum==k)
			{sums[j]=sum;B[j]=l-1;}
			if(sum<k)
			{
				for(l=0;l<N;l++)
				{
					sum=sum+A[l];
					if(sum>k)
					{sums[j]=sum-A[l];B[j]=l-1;break;}
				}
			}
		}
//		for(j=0;j<N;j++)
//			cout << sums[j] <<" "<< B[j]<< endl;
		if(flag==0||flag==2){
			l=0;
			for(j=0;j<R;j++)
			{
				if(flag==2&&A[l]>k)
				{break;}
				p=p+sums[l];l=B[l]+1;
				if(l>=N)
				    l=0;	
			}
		}
		cout << "Case #"<<i+1<<": "<< p<< endl;
	}
}
