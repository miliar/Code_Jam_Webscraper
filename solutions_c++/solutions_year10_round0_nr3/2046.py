#include <cstdio>
#include <cstring>

	 int began[1000];
         long long int end[1000];
	long long int pr[1000];
	int pos[1000];
	
	
int main()
{
int t;
scanf("%d",&t);

for(int ct=0;ct<t;ct++)
{
	int r,k,n;
memset(began,-1,sizeof(long long int)*1000);
	memset(end,-1,sizeof(long long int)*1000);
	scanf("%d %d %d",&r,&k,&n);
	
	int* q=new int[n];
	int front=0;

	for(int i=0;i<n;i++)
	scanf("%d",&q[i]);
	long long int profit=0;

	for(int f=0;f<n;f++)
	{
		int rem=k;
		long long int tprof=0;
		int j;
			for( j=f;; )
			{	
			if(rem-q[j] < 0) break;
			tprof+=q[j]; rem-=q[j];
			j=(j+1)%n;
			if(j==f) break;
			}
		began[f]=tprof; end[f]=j;
	}	

memset(pos,-1,1000*sizeof(int));
	long long int dpr=0;
	
		front=0;
		int i;
		for(i=0;i<r;i++)
		{

                if(pos[front]!=-1)
		{
		   dpr=profit-pr[front];
                   break;
		}
		pos[front]=i;
                pr[front]=profit;
		profit+=began[front];
		front=end[front];		

		}
if(i<r) 
{
int numrem=r-i;
int loop= i-pos[front];  
long long dd=numrem/loop;
profit+= dpr * dd;
numrem=numrem%loop;
	for(int p=0;p<numrem;p++)
	{
	profit+=began[front];
	front=end[front];
	}
}


printf("Case #%d: %lld\n",ct+1, profit);

}

return 0;
}
