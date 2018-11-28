#include <stdio.h>
#include<memory.h>

int main(){

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i,t,n,j;
    int a[1002],eor,min,sum;

	fscanf(fp,"%d", &t);
	for(i = 1; i <= t; ++i)
    {
		fscanf(fp,"%d",&n);
		sum=0;
        eor = 0;
        for(j=0;j<n;j++)
        {
            fscanf(fp,"%d",&a[j]);
            if( a[j]<min || j==0)
                min = a[j];
            eor = eor^a[j];
            sum+= a[j];
        }
        if (eor!=0)
            fprintf(ofp,"Case #%d: NO\n",i);
        else
            fprintf(ofp,"Case #%d: %d\n",i,sum- min);
    }

	return 0;
}
