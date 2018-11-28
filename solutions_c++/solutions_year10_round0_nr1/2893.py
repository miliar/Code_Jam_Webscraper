#include<iostream.h>
#include<stdio.h>
#include<memory.h>
#include<string.h>
long int k,n,t,ans,arr[31],arrcount,tempsnaps,deducednumber;
long int i,tc;
int main()
{
    long int data[10000][2]={0,0};
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	fscanf(fp, "%ld",&t);
	for(i=0;i<t;i++) 
	{
	fscanf(fp, "%ld", &data[i][0]);
	fscanf(fp, "%ld", &data[i][1]);
	}
	arr[0]=1;
	for(i=1;i<31;i++)
	{
     arr[i]=arr[i-1]*2;  
	}
    for(tc=0;tc<t;tc++)
	{
		deducednumber=0;
        n=data[tc][0];
		k=data[tc][1];
		cout<<n<<"\n"<<k<<"\n";
	    for(i=0;i<n;i++)
		{
		deducednumber=deducednumber+arr[i];
		}
		if(k==0)
		{
			k=-1;
		}
        while(k>0)
		{
			k=k-deducednumber;
			if(k==0)
			{
				break;
			}
			else
			{
				k--;
			}
			if(k==0)
			{
				k=-1;
			}
        } 
		if(k==0)
		fprintf(ofp, "Case #%d: ON \n", tc+1);
		else
        fprintf(ofp, "Case #%d: OFF \n", tc+1);
		} 
	return 0;
}
