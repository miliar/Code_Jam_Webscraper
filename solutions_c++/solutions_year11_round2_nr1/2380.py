#include<stdio.h>

void main()
	{
	 int t,tc=1,n;
	 char matrix[10][10];
	 float wp[10],tempwin,temploose,owp[10],win[10],loose[10],oowp[10],rpi[10];
	  for(scanf("%d",&t);tc<=t;tc++)
		{
        printf("Case #%d:\n",tc);
		  scanf("%d",&n);
		  //printf("%d",n);
			 for(int j=0;j<n;j++)
			 {

				tempwin=0;
				temploose=0;
				scanf("\n");
				for(int i=0;i<n;i++)
				{
					scanf("%c",&matrix[j][i]);
					 if(matrix[j][i]=='1')
						tempwin++;
					 else if(matrix[j][i]=='0')
						temploose++;

				}

				win[j]=tempwin;
				loose[j]=temploose;
			  wp[j]=tempwin/(tempwin+temploose);
			  //	printf("\nWin per of %d is %f   %d  %d",j,wp[j],tempwin,temploose);
			  }

			 for(j=0;j<n;j++)
			 {
				float count,tempwin,sum;

				count=0,sum=0;
				for(int i=0;i<n;i++)
				{
					if(matrix[j][i]=='1')
					  {
						 tempwin=win[i]/(win[i]+loose[i]-1);
						 count++;
						 sum=sum+tempwin;
					  }
					else if(matrix[j][i]=='0')
					  {
						 tempwin=(win[i]-1)/(win[i]+loose[i]-1);
						 count++;
						 sum=sum+tempwin;
					  }

				}
				owp[j]=sum/count;

				//wp[j]=tempwin/(tempwin+temploose);
				//printf("\nowp per of %d is %.7f",j,owp[j]);
			  }

			  for(j=0;j<n;j++)
			 {
				float count,sum;

				count=0,sum=0;
				for(int i=0;i<n;i++)
				{

					if(matrix[j][i]!='.')
					  {
						 count++;
						 sum=sum+owp[i];
					  }

				}
				oowp[j]=sum/count;
				rpi[j]=((0.25*wp[j])+(0.50*owp[j])+(0.25*oowp[j]));
				//wp[j]=tempwin/(tempwin+temploose);
				//printf("\noowp per of %d is %.7f",j,owp[j]);
            printf("%.8f\n",rpi[j]);
			  }


		}

	}
