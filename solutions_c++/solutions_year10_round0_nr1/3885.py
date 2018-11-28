#include<fstream.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<process.h>

 int main(void)
 {
  unsigned int n,value1,t,count=1;
  long int i,k,value=0,value2=0;

  FILE *ifp, *ofp;
  char *mode="r";
  char outputfilename[]="asmall.out";
  ifp=fopen("input.in",mode);

  if(ifp== NULL)
  {fprintf(stderr,"cant open the input file\n");
   exit(1);
  }

  ofp=fopen(outputfilename, "w");

  if(ofp == NULL)
  {
   fprintf(stderr,"cant open the output file %s\n", outputfilename);
   exit(1);
  }
  fscanf(ifp,"%d",&t);

  while(fscanf(ifp, "%d%ld",&n,&k)!= EOF)
  {

   value=pow(2,n)-1;
   value1= k-value;
   value2=pow(2,n);

   if(k<value)
   {
    fprintf(ofp,"Case #%d: OFF\n",count );
   }
   else
       {
	 if((value1%value2)!=0)
	 {
	 fprintf(ofp,"Case #%d: OFF\n",count);
	 }
	 else
	 {
	 fprintf(ofp,"Case #%d: ON\n",count);
	 }
	}
	count++;
	 printf("\n");

 }            //End of while

  fclose(ifp);
  fclose(ofp);

  getch();
  return 0;
}             //End of main