#include <cstdio>

int main()
{
	int testcase,cnt=1;
	FILE* fp;
	fp=fopen("output.out","w");

	scanf("%d",&testcase);
	while(testcase--)
	{
		int N,L,H;
		scanf("%d%d%d",&N,&L,&H);
		int i,j;
		int arr[101];
		bool noanswer=true;
		
		for(i=0;i<N;i++)
		{
			scanf("%d",&arr[i]);
		}
		for(j=L;j<=H;j++)
		{
			bool flag=true;
			for(i=0;i<N;i++)
			{
				if((arr[i]%j!=0)&&(j%arr[i]!=0))
				{
					flag=false;
				}
			}
			if(flag)
			{
				fprintf(fp,"Case #%d: %d\n",cnt++,j);
				noanswer=false;
				break;
			}
		}
		if(noanswer)
		{
			fprintf(fp,"Case #%d: NO\n",cnt++);
		}
	}
	fclose(fp);
	return 0;
}
				
