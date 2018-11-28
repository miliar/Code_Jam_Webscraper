#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
#define MAX_TEST_CASES 10005
unsigned long int k[MAX_TEST_CASES];
int n[MAX_TEST_CASES];
int snapper[30];
int power[30];
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	printf("Enter input filename(excluding the .in extension)\n");
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	unsigned long int t,i;
	fscanf(fp, "%ld", &t);
	for(i=0;i<t;i++) {
		fscanf(fp, "%d%ld", &n[i],&k[i]);
		int j;
		for(j=0;j<30;j++) {
			snapper[j]=0;
			power[j]=0;
		}
		power[0]=1;
		int c1;
		for(c1=1;c1<=k[i];c1++) {
			int c;
			for(c=0;c<n[i];c++)	{
				if(power[c]==1){
					if(snapper[c]==0) snapper[c]=1; else snapper[c]=0;
				}
			}
			for(c=1;c<n[i];c++)	{
				if(snapper[c-1]==1){
					power[c]=1;
				} else {
					power[c]=0; break;
				}
			}
			int ac;
			for(ac=c+1;ac<n[i];ac++) {
				power[ac]=0;
			}
		}
		int c;
		int retVal=1;
		for(c=0;c<n[i];c++)	{
			if(snapper[c]==0){
				retVal=0;break;
			}
		}
		char ans[4];
		if (retVal==0) strcpy(ans,"OFF"); else strcpy(ans,"ON");
		fprintf(ofp, "Case #%ld: %s\n", i+1, ans);
	}
	fclose(fp);
	fclose(ofp);
	return 0;
}
