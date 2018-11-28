#include<stdio.h>
#include<math.h>
#include<string.h>

int t,n[10000],k[10000];
int main()
{

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	int i,j,p,q,l;



	fscanf(fp,"%d",&t);
	
for(i=0;i<t;i++)
{
	fscanf(fp,"%d%d",&n[i],&k[i]);

}
for(i=0;i<t;i++)
{
	  l=n[i];
	p=pow(2,l)-1;

	if(k[i]==p)
	fprintf(ofp,"\nCase #%d: ON",i+1);

	if(k[i]>p)
		  {
			  q=0;j=2;

			  while(q<k[i])
			  {


				  q= p*j+(j-1);

				  if(k[i]==q)
					  fprintf(ofp,"\nCase #%d: ON",i+1);



				  j++;
			  }
			 if(k[i]!=q)
				fprintf(ofp,"\nCase #%d: OFF",i+1);
		  }

			if(k[i]<p)
			fprintf(ofp,"\nCase #%d: OFF",i+1);





 }
	  fclose(fp);
 return 0;
}
