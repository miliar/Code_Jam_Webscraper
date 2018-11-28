#include<stdio.h>
#include<stdlib.h>


int N,n,Cas,t,i,j,ans,lastB,lastO;
int x[101];
char c[101][2];
	
int main()
{
	freopen("outputABig.txt","w",stdout);
	scanf("%d",&N);
	//Cas=1;
	for (Cas=1;Cas<=N;Cas++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
			scanf(" %s %d",&c[i],&x[i]);
		ans=0;
		lastB=lastO=1;		
		for (i=0;i<n;i++)
		{
			if (c[i][0]=='O')
			{
				t=abs(x[i]-lastO)+1;
				ans+=t;
				for (j=i+1;j<n;j++)
					if (c[j][0]=='B')
					{
						if (t>=abs(x[j]-lastB))
							lastB=x[j];
						else
						{
							if (x[j]>lastB)
								lastB+=t;
							else
								lastB-=t;
						}								
						break;
					}
				lastO=x[i];		
			}
			else
			{
				t=abs(x[i]-lastB)+1;
				ans+=t;
				for (j=i+1;j<n;j++)
					if (c[j][0]=='O')
					{
						if (t>=abs(x[j]-lastO))
							lastO=x[j];
						else
						{
							if (x[j]>lastO)
								lastO+=t;
							else
								lastO-=t;
						}								
						break;
					}
				lastB=x[i];			
			}
		}
		printf("Case #%d: %d\n",Cas,ans);
	}	
}
