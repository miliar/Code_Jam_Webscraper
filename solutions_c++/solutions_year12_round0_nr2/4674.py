// codejam2.cpp : main project file.

//#include "stdafx.h"
#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
int arr[110];
int Max[110][2];
int num,s,p;

int L[110][2];
int R[110][2];

void merge(int p,int q,int r)
{
     int n1=q-p+1;
     int n2=r-q;
     
     L[n1][0]=1010;
		 R[n2][0]=1010;
     
     int i,j,k;
     for(i=0;i<n1;i++)
     {
		 L[i][0]=Max[p+i][0];
		 L[i][1]=Max[p+i][1];
	 }
     for(j=0;j<n2;j++)
	 {
		R[j][0]=Max[q+j+1][0];
		R[j][1]=Max[q+j+1][1];
	 }
     i=j=0;
     for(k=p;k<=r;k++)
     {                
                    if(L[i][0]<R[j][0]||(L[i][0]==R[j][0]&&L[i][1]<R[j][1]))
                    {
						Max[k][0]=L[i][0];
						Max[k][1]=L[i][1];
						i++;
					}
					
                    else
                    {
                    Max[k][0]=R[j][0];
					Max[k][1]=R[j][1];
					j++;
                    
                    //icount+=n1-i;
                    }
                    
     }
         
     
}
void mergesort(int i,int j)
{
     if(i<j)
     {      
            int k=i+(j-i)/2;
            mergesort(i,k);
            mergesort(k+1,j);
            merge(i,k,j);
     }
     return;
     
 }
int main()
{
	int tests;
	scanf("%d",&tests);
	for(int l=1;l<=tests;l++)
	{
		
		scanf("%d%d%d",&num,&s,&p);
//		Maxcount=0;
		//count=0;
		int i,j,k;
		for(i=0;i<num;i++)
			{
				scanf("%d",&arr[i]);
				if(arr[i]<2)
				{
					Max[i][0]=arr[i];
					Max[i][1]=-1;
				}
				else if(arr[i]>=29)
				{
					Max[i][0]=10;
					Max[i][1]=-1;
				}
				else if(arr[i]%3==0)
				{
					Max[i][0]=arr[i]/3;
					Max[i][1]=arr[i]/3+1;
				}
				else if(arr[i]%3==1)
				{
					Max[i][0]=(arr[i]+2)/3;
					Max[i][1]=(arr[i]-1)/3+1;
				}
				else if(arr[i]%3==2)
				{
					Max[i][0]=(arr[i]+1)/3;
					Max[i][1]=(arr[i]+4)/3;
				}
		}
		int count1=0,count2=0;
		mergesort(0,num-1);
		bool flag[110]={false};
		for(i=0;i<num;i++)
		{
			if(Max[i][1]!=-1)
			{
				for(j=0;j<s;j++)
				{
					flag[i+j]=true;
					if(Max[i+j][1]>=p)
					
					count1++;
				}
				break;
			}
		}
		for(i=0;i<num;i++)
		{
			if(!flag[i]&&(Max[i][0]>=p))
				count1++;
		}

		memset(flag,false,num);
		for(i=num-1;i>=0;i--)
		{
			if(Max[i][1]!=-1)
			{
				for(j=0;j<s;j++)
				{
					flag[i-j]=true;
					if(Max[i-j][1]>=p)
					
					count2++;
				}
				break;
			}
		}
		for(i=0;i<num;i++)
		{
			if(!flag[i]&&(Max[i][0]>=p))
				count2++;
		}
		count1=count1>count2?count1:count2;
		printf("Case #%d: %d\n",l,count1);
	}
    return 0;
}
