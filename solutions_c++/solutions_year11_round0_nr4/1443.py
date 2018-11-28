#include<cstdio>
using namespace std;
int main()
{
	int temp,num_cases,i,j,k,l,count1,count2,count3,count4,n;
		int org[1200],sort1[1200],sort2[1200];
	float res[110];
	scanf("%d",&num_cases);
	for(i=1;i<=num_cases;i++)
	{
		count1=count2=count3=count4=0;
		scanf("%d",&n);
	
		for(j=0;j<n;j++)
		{
			scanf("%d",&temp);
			//printf("%d\n",temp);
			org[j]=sort1[j]=sort2[j]=temp;		
		}	
		for(k=0;k<n;k++)
				for(l=k+1;l<n;l++)
				{
					if(sort1[k]<sort1[l])
					{
					temp=sort1[k];
					sort1[k]=sort1[l];
					sort1[l]=temp;
					count1++;
					}
					if(sort2[k]>sort2[l])
					{
					temp=sort2[k];
					sort2[k]=sort2[l];
					sort2[l]=temp;
					count2++;
					}
				}
		for(k=0;k<n;k++)
		{
			//printf("%d\t%d\t%d\n",org[k],sort1[k],sort2[k]);
			/*if(org[k]!=sort1[k])
				count3++;*/
			if(org[k]!=sort2[k])
				count4++;
		}
		//printf("%d\n%d\n",count3,count4);
		/*if(count3>count4)
			res[i]=count3;
		else*/
			res[i]=count4;
			
	}
	for(i=1;i<=num_cases;i++)
		printf("Case #%d: %f\n",i,res[i]);
	return 0;
}
