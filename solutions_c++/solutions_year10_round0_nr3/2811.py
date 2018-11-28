#include<iostream.h>
#include<process.h>
#include<stdio.h>
#include<string.h>
char filename[32];
char infile[32], outfile[32];
long int rides,capacity,payment,arr[10000]={0},point,i,grp,t,tc,nogroups,cap,tempptr,riders;
int main()
{
	
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	fscanf(fp, "%ld",&t);
	for(tc=0;tc<t;tc++)
	{
		for(i=0;i<1000;i++)
			arr[i]=0;
		riders=0;
		fscanf(fp,"%ld",&rides);
		fscanf(fp,"%ld",&capacity);
        fscanf(fp,"%ld",&nogroups);
		for(grp=0;grp<nogroups;grp++)
		{
         fscanf(fp,"%ld",&arr[grp]);
		 riders=riders+arr[grp];
		}
	    if(riders<=capacity)
		{ 
		 payment=riders*rides;
		}
	    if(riders>capacity)
		{
		 payment=0;
	     point=0;
	      for(i=0;i<rides;i++)
		  {
		   cap=capacity;
		    while(cap>=0)
			{
			 cap=cap-arr[point];
             payment=payment+arr[point];
			 point++;
			 if(point>grp)
			 {
			  point=0;
			 }
		 
			}
		     if(point==0)
			 {
				 point=grp;
			 }
			 else
			 {
				 point--;
			 }
		     payment=payment-arr[point];
			 
		  }
	}

		fprintf(ofp, "Case #%d: %d  \n", tc+1,payment);
				
	}
    return 0;
}
