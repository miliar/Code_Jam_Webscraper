#include<stdio.h>
#include<conio.h>
void
main()
{
      FILE *fp,*qp;
      int sum,t,case_id,i,j,remain;
      long int r,k,n,a[15],money;
      fp=fopen("c.in","r");
      qp=fopen("sol.in","w");
     fscanf(fp,"%d",&t);
     if(fp==NULL) {
     printf("file not found \n"); getch();
     return;   }
      for(case_id=1;case_id<=t;case_id++)
      {
					 money=0;


	 fscanf(fp,"%ld%ld%ld",&r,&k,&n);
	 for(i=0;i<n;i++)
	 {fscanf(fp,"%ld",&a[i]);	}

	 j=0;
	 for(i=0;i<r;i++)
	 {  sum=0;remain=n;

			while(((sum+a[j])<=k)&&remain)
			{
					   sum=sum+a[j];

			j=(j+1)%(n);remain--;
			}

			money=money+sum;
			}
			fprintf(qp,"Case #%d: %ld\n",case_id,money);


					 }













      fclose(fp);
      fclose(qp);

      }
