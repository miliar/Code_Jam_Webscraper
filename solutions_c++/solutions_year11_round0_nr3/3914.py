#include <cstdio>
#include <algorithm>

int main()
{
	int testcase,cnt=1;
	FILE* fp;
	fp=fopen("output.out","w");
	scanf("%d",&testcase);

	while(testcase--)
	{
		int num,i,j;
		int arr[1550];
		int val[2000];
		int valpos=0;
		scanf("%d",&num);
		for(i=0;i<num;i++)
		{
			scanf("%d",&arr[i]);
		}
		std::sort(arr,arr+num);
		for(i=1;i<num;i++)
		{
			int r_sum=0,r_semi=0;
			int i_sum=0,i_semi=0;
			for(j=0;j<i;j++)
			{
				r_sum+=arr[j];
				i_sum^=arr[j];
			}
			for(j=i;j<num;j++)
			{
				r_semi+=arr[j];
				i_semi^=arr[j];
			}
			if(i_semi==i_sum)
			{
				val[valpos++]=(r_sum>r_semi)?r_sum:r_semi;
			}
		}
		if(valpos==0)
		{
			fprintf(fp,"Case #%d: NO\n",cnt++);
		}
		else
		{
			std::sort(val,val+valpos);
			fprintf(fp,"Case #%d: %d\n",cnt++,val[valpos-1]);
		}
	}
	fclose(fp);
	return 0;
}