#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int pl[1006];
int p[1006][1006];
int cmp(const void *a,const void *b)
{ 
	int a1 = *(int *)a; 
	int a2 = *(int *)b; 
	return a2 - a1; 
} 
int main()
{
	int c;
	int i,j,k,l;
	int max_j;
	int cs;
	int js;
	int ws;
	__int64 sum;
   freopen("A-small-attempt0.in","r",stdin);
   freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&c);
	for(i=0;i<c;i++)
	{
		sum=0;
		cs=0;
		memset(pl,0,sizeof(pl));
		memset(p,-1,sizeof(p));
		scanf("%d",&max_j);
		scanf("%d",&js);
		scanf("%d",&ws);

		for(j=0;j<ws;j++)
		{
			scanf("%d",&pl[j]);
		}
		qsort(pl,ws,sizeof(int),cmp); 
		int l=0;
        for(j=0;j<max_j;j++)
			for(k=0;k<js;k++)
			{
				sum+=pl[l]*(j+1);
				l++;
			}
	    printf("Case #%d: %I64d\n",(i+1),sum);
		
			
			
	}
	return 0;
}