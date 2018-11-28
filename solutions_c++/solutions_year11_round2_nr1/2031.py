#include <cstdio>

int main()
{
	int testcase,cnt=1;
	FILE* fp;
	fp=fopen("output.out","w");
	
	scanf("%d",&testcase);
	while(testcase--)
	{
		int N,i,j;
		char map[105][105];
		scanf("%d",&N);
		double WP[105]={0},OWP[105]={0},OOWP[105]={0};

		for(i=0;i<N;i++)
		{
			int div=0;

			scanf("%s",map[i]);
			for(j=0;j<N;j++)
			{
				if(map[i][j]=='1')
				{
					WP[i]+=1.0;
				}
				if(map[i][j]!='.')
				{
					div++;
				}
			}
			if(div!=0)
			{
				WP[i]/=div*1.0;
			}
			else
			{
				WP[i]=0;
			}
		}
		for(i=0;i<N;i++)
		{
			int div=0;

			for(j=0;j<N;j++)
			{
				if(map[i][j]!='.')
				{
					int k,tdiv=0;;
					double twp=0.0;

					for(k=0;k<N;k++)
					{
						if((k!=i)&&(map[j][k]=='1'))
						{
							twp=twp+1;
						}
						if((k!=i)&&(map[j][k]!='.'))
						{
							tdiv++;
						}
					}
					twp/=tdiv*1.0;
					OWP[i]+=twp;
				}
				if(map[i][j]!='.')
				{
					div++;
				}
			}
			if(div!=0)
			{
				OWP[i]/=div*1.0;
			}
		}
		for(i=0;i<N;i++)
		{
			int div=0;

			for(j=0;j<N;j++)
			{
				if(map[i][j]!='.')
				{
					OOWP[i]+=OWP[j];
					div++;
				}
			}
			if(div!=0)
			{
				OOWP[i]/=div*1.0;
			}
		}
		fprintf(fp,"Case #%d:\n",cnt++);
		for(i=0;i<N;i++)
		{
			fprintf(fp,"%.12lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
		}
	}
	return 0;
}

