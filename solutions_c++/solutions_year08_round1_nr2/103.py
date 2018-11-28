#include <stdio.h>


int need[2001][2001];
int num[2001];
int ipos[2001];
int manzu[2001];
int result[2001];

//0==unm 1=m 2=weizhi 3=manzu 4=bumanzhu
int main()
{
    freopen("B-large.in.txt","r",stdin);
    freopen("B-large.out.txt","w",stdout);

	int i,j,t,p,n,m,t1,t2,ni,nj;
    bool tag;
	scanf("%d",&t);
	for(p=0;p<t;p++)
	{
		scanf("%d%d",&n,&m);
        
		for(i=0;i<n;i++)
			result[i]=2;

		for(j=0;j<m;j++)
            for(i=0;i<n;i++)
			{
				need[j][i]=2;
				ipos[j]=0;
				manzu[j]=0;
            }
        
		for(j=0;j<m;j++)
		{
            scanf("%d",&num[j]);
			for(i=0;i<num[j];i++)
			{
				scanf("%d%d",&t1,&t2);
				need[j][t1-1]=t2;
			}

		}

	  /*  for(j=0;j<m;j++)
		{
            printf("%d ",num[j]);
			for(i=0;i<n;i++)
				if(need[j][i]!=2)
					printf("%d %d ",i+1,need[j][i]);

		}
        */
		tag=true;
       while(1)
	   {
           for(i=0;i<m;i++)
		   if(manzu[i]==0)
		   {
			   if(num[i]-ipos[i]-manzu[i]==1)
			   {
                   for(j=0;j<n;j++)
					   if(need[i][j]==1)
						   break;
                   
                   if(j!=n)
				      break;
			   }
		   }

		   if(i==m)
		   { 
               tag=true;
			   break;
		   }
         //  printf("** %d %d\n",i,j);             
		   ni=i;
		   nj=j;
           need[ni][nj]=3;
		   manzu[ni]++;
		   result[nj]=1;

		   for(i=0;i<m;i++)
			   if(i!=ni)
			   {
		           if(need[i][nj]==1)
				   {
                       need[i][nj]==3;
					   manzu[i]++;
				   }
				   else if(need[i][nj]==0)
				   {
                       need[i][nj]==4;
					   ipos[i]++;
				   }
			   }

           for(i=0;i<m;i++)
			   if(ipos[i]==num[i])
				   break;
           
		   if(i!=m)
		   {
               tag=false;
			   break;
		   }
	   }
       
	   printf("Case #%d:",p+1);
	    
       if(tag)
	   {
		   for(i=0;i<n;i++)
		   {
			   if(result[i]==2||result[i]==0)
				   printf(" 0");
			   else
				   printf(" 1");
		   }
		   printf("\n");
	   }
	   else
	   {
           printf(" IMPOSSIBLE\n");
	   }

	}
//	need[1999][1999]=1;
//	printf("%d\n",need[1999][1999]);
  //  getchar();
}