#include<iostream.h>
#include<conio.h>
int front=0;
int back=0;
struct queue
{
	int a;
	
}q[5000];

void enqueue(int x)
{
	q[back++].a=x;
}

int dequeue()
{
	return q[front++].a;
}


int main()
{
	int t,r,k,n,i,a,j,sum=0,temp,var,count,c;	   	   	   //t denotes test cases,r times, k people, n groups
	FILE *in,*out;
	in=fopen("input.txt","r");
	out=fopen("output.txt","w");
	fscanf(in,"%d",&t);
	for(count=0;count<t;count++)
	{
		sum=0;
		front=0;
		back=0;
		fscanf(in,"%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
		{
				fscanf(in,"%d",&a);
				enqueue(a);
		}
		for(i=0;i<r;i++)
		{
			c=0;
			temp=0;
			while((temp+q[front].a)<=k&&(c<(back-front)))
			{
				c++;
				var=dequeue();
				temp+=var;
				enqueue(var);
			}
			sum+=temp;	  
		}
		
		fprintf(out,"Case #%d: %d\n",count+1,sum);
			
	}	 
    getch();	 	 
}

