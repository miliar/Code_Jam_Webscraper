#include <stdio.h>

int main(void)
{
	int n,sl,na,nb,fa,fb;
	int c,a,b,tsh,tsm,teh,tem,i,j,temp,flag;
	FILE *fp,*fpo;
	if((fp= fopen("d:\\codejam\\B-large.in","r"))==NULL)
	{printf("Error oprning file input.in");return 0;}

	if((fpo= fopen("d:\\codejam\\B-largeOP.txt","w"))==NULL)
	{printf("Error oprning file output.txt");return 0;}

	fscanf(fp,"%d",&n);

	for (c=0; c<n; c++)
	{
	  int as[101],ae[101],bs[101],be[101];
	  fscanf(fp,"%d",&sl);
	  fscanf(fp,"%d %d",&na,&nb);
	  fa=0;fb=0;
	  for (a=0;a<na;a++)
	  {
	    fscanf(fp,"%d:%d %d:%d",&tsh,&tsm,&teh,&tem);
	    as[a]=tsh*60+tsm;
	    ae[a]=teh*60+tem+sl;
	  }

	  for (b=0;b<nb;b++)
	  {
	    fscanf(fp,"%d:%d %d:%d",&tsh,&tsm,&teh,&tem);
	    bs[b]=tsh*60+tsm;
	    be[b]=teh*60+tem+sl;
	  }

	 for (i=0;i<na-1;i++)
	 {
	    for (j=i+1;j<na;j++)
		{
		  if (as[j]<as[i])
		  {
		    temp=as[i];
			as[i]=as[j];
			as[j]=temp;
			
			temp=ae[i];
			ae[i]=ae[j];
			ae[j]=temp;
		  }
		}
	 }
	 
	 for (i=0;i<nb-1;i++)
	 {
	    for (j=i+1;j<nb;j++)
		{
		  if (bs[j]<bs[i])
		  {
		    temp=bs[i];
			bs[i]=bs[j];
			bs[j]=temp;
			
			temp=be[i];
			be[i]=be[j];
			be[j]=temp;
		  }
		}
	 }
	 
	 for (a=0;a<na;a++)
	 {
	   flag=0;
	   for (b=0;b<nb;b++)
	   {
	     if(be[b]<=as[a])
	     {
		   be[b]=2000;
		   flag = 1;
		   break;
	     }		 
	   }
	   if (flag!=1)
			fa++;
	 }

	 for (b=0;b<nb;b++)
	 {
	   flag=0;
	   for (a=0;a<na;a++)
	   {
	     if(ae[a]<=bs[b])
	     {
			flag=1;
			ae[a]=2000;
			break;
	     }		 
	   }
	   if (flag!=1)
			fb++;
	 }

	   if (c!=n-1)
		fprintf (fpo,"Case #%d: %d %d\n",c+1,fa,fb);
	   else
		fprintf (fpo,"Case #%d: %d %d",c+1,fa,fb);

	}
fclose(fp);
fclose(fpo);
return 1;
}