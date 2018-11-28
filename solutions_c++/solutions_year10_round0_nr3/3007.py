#include<stdio.h>
#include <iostream>
#include <queue>

using namespace std;
FILE *fin=fopen("small.in","r");
FILE *fout=fopen("output.out","w");
int main ()
{
	int R,N,k,i,j,temp,no,sum,ans;
	
	fscanf(fin,"%d",&no);
	for(j=0;j<no;j++)
	{
		queue <int> q,q1;
		sum=0,ans=0;
	fscanf(fin,"%d %d %d",&R,&k,&N);
	for(i=0;i<N;i++)
	{
		fscanf(fin,"%d",&temp);
		q.push(temp);
	}
	int h=0;
	for(i=0;i<R;i++)
	{
			while(sum<=k && q.size()!=0)
			{
				//printf("yay%d\n",i);
				sum=sum+q.front();
				h=q.front();
				if(sum>k || q.size()==0)
				break;
				
				q1.push(q.front());
				q.pop();
				//printf("%d \n",sum);
			}
			if(q.size()==0)
			h=0;
		ans=ans+sum-h;
		sum=0;
	//	printf("\n");
		while(q1.size()!=0)
		{
			q.push(q1.front());
			q1.pop();
		}
		
	}fprintf(fout,"Case #%d: %d\n",j+1,ans);}
	return 0;
}
		
	
	
	