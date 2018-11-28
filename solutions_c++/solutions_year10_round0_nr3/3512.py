#include<stdio.h>
#include<string.h>
#include<memory.h>
int main()
{
	
	int t,h=1,i,k,n,j,ch,r,temp,sum,a[10];
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile,filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	fscanf(fp,"%d",&t);
	while(h<=t)
	{
		sum=0;
		fscanf(fp,"%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
		fscanf(fp,"%d",&a[i]);
		j=0;
		for(i=1;i<=r;i++)
		{  
		temp=0; 
		ch=0;	
			while((temp+a[j]<=k)&&(ch<n))
			{
				temp+=a[j];
				ch++;
			j=(j+1)%n;
			}
		sum+=temp;	
		}
		fprintf(ofp,"Case #%d: %d\n",h,sum);	
	h++;
		
	}
	
}
			
