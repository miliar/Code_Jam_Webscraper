#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int t,p,i,j,k,n,len,m;
	scanf("%d\n",&t);
	char arr[501];
	char ref[20]="welcome to code jam";
	for(p=1;p<=t;p++)
	{
		fgets(arr,500,stdin);
		len=strlen(arr);
		m=len;
		m--;
		int *A[m];
		//printf("YO%d\n",m);
		for(i=0;i<m;i++)
		{
			A[i]=new int[20];
		}
		for(i=0;i<m;i++)
			A[i][19]=1;
		for(j=0;j<19;j++)
		{
			A[m-1][j]=0;
		}
		if(arr[m-1]==ref[18])
		{
			A[m-1][18]=1;
		}
		for(i=m-2;i>=0;i--)
		{
			for(j=0;j<19;j++)
			{
				A[i][j]=A[i+1][j];
				if(arr[i]==ref[j])
				{
					A[i][j]+=A[i+1][j+1];
				}
				if(A[i][j]>=10000)
					A[i][j]-=10000;
			}
		}	
		printf("Case #%d: ",p);
		k=A[0][0];
		j=0;
		if(k==0)
			j=1;
		while(k>0)
		{
			k/=10;
			j++;
		}
		for(;j<4;j++)
			printf("0");
		printf("%d\n",A[0][0]);
	}
	return 0;
}