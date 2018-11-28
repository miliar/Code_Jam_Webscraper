#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#define N 10010
using namespace std;
int a[N],temp[N];
/*int compare(const void * a,const void * b)
{
	return (*(int *a) - *(int *b));
}*/

int compare (const void * a, const void * b)
{
	return ( *(int*)a - *(int*)b );
}


int main()
{
	int tc,l,t,n,c,time,i,j;
	scanf("%d",&tc);
	for(int tt=0;tt<tc;tt++)
	{
		scanf("%d%d%d%d",&l,&t,&n,&c);
		for(i=0;i<c;i++)
			scanf("%d",&a[i]);
		for(i=c;i<n;i+=c)
			for(j=0;j<c;j++)
				a[i+j]=a[j];
		int dist=t/2;
		time=t;
		i=0;
		while(dist>0)
		{
			dist=dist-a[i];
			i++;
		}
		int cnt=0;
		if(dist<0) temp[cnt++]=-dist;
		while(i<n)
		{
			temp[cnt++]=a[i];
			i++;
		}
		qsort(temp,cnt,sizeof(int),compare);
	
		for(i=cnt-1,j=0;i>=0 && j<l;i--,j++)
			time+=temp[i];
		while(i>=0)
		{
			time+=temp[i]*2;
			i--;
		}
		printf("Case #%d: %d\n",tt+1,time);
	}
return 0;
}
