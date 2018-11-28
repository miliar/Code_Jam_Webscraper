#include<stdio.h>
#include<string.h>
#include<algorithm>

void merge( int *array,int low, int mid, int high )
{ 
int temp[16];
int i = low;
int j = mid +1 ;
int k = low ;

while( (i <= mid) && (j <=high) )
{
if(array[i] <= array[j])
temp[k++] = array[i++] ;
else
temp[k++] = array[j++] ;
}
while( i <= mid )
temp[k++]=array[i++];
while( j <= high )
temp[k++]=array[j++];

for(i= low; i <= high ; i++)
array[i]=temp[i];
}

void merge_sort( int *array,int low, int high )
{
int mid;
if( low != high )
{
mid = (low+high)/2;
merge_sort( array,low , mid );
merge_sort( array,mid+1, high );
merge( array,low, mid, high );
}
}
int main()
{
	int *array,n,i,t,k,j,p;
	scanf("%d",&t);
	k=1;
	while(k<=t)
	{
	scanf("%d",&n);
	array=(int*)malloc(sizeof(int)*n);
	for(i = 0; i < n;i++)
	{
		scanf("%d",&array[i]);
	}
	merge_sort(array,0,n-1);
	j=0;p=0;
	j=array[0]^j;
	for(i = 1; i < n;i++)
	{
	 j=array[i]^j; 
	 p=p+array[i]; 
     }
	if(j!=0)
	{ 
	  printf("Case #%d: NO\n",k);
 	  }
 	  else 
	   printf("Case #%d: %d\n",k,p);
	k++;
	}
	
	return 0;
}
