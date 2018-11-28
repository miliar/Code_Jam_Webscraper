#include<stdio.h>

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("b_codejam.out","w",stdout);
	//freopen("b_large_codejam.out","w",stdout);

	int cas,cc;
	int numG, surprise, targetP;
	int score[200];
	int A[200],B[200],C[200];
	int i,j;
	int ans;
	int temp;

	scanf("%d",&cas);

	for(cc=1;cc<=cas;cc++)
	{
		scanf("%d %d %d",&numG,&surprise,&targetP);
		for(i=0;i<numG;i++)
		{
			scanf("%d",&score[i]);
		}

		//result checking
		for(i=0;i<numG;i++)
		{
			temp=score[i];

			if(temp%3==0)
			{
				A[i]=temp/3;
				B[i]=temp/3;
				C[i]=temp/3;
			}

			if((temp+1)%3==0)
			{
				A[i]=((temp-2)/3)+1;
				B[i]=((temp-2)/3)+1;
				C[i]=((temp-2)/3)+0;
			}

			if((temp+2)%3==0)
			{
				A[i]=((temp-1)/3)+1;
				B[i]=((temp-1)/3)+0;
				C[i]=((temp-1)/3)+0;
			}

			//printf("%d %d %d\n",A[i],B[i],C[i]);
		}

		//process the output
		ans=0;
		for(i=0;i<numG;i++)
		{
			//printf("%d %d %d\n",A[i],B[i],C[i]);

			if(A[i]>=targetP)
			{
				if(A[i]>=0 && B[i]>=0 && C[i]>=0)
				{
					ans++;
				}
			}
			else
			{
				if(A[i]+1==targetP)
				{
					A[i]++;
					B[i]--;

					if(A[i]>=targetP)
					{
						if(surprise>0)
						{
							if(A[i]>=0 && B[i]>=0 && C[i]>=0)
							{
								if(A[i]-C[i]<=2 && A[i]-B[i]<=2)
								{
									ans++;
									surprise--;
								}
							}
						}
					}
				}
			}
		}


		printf("Case #%d: ",cc);
		printf("%d\n",ans);
	}

	return 0;
}
