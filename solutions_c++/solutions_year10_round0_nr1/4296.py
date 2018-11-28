#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
#define MAX_TEST_CASES 10005
unsigned long int k[MAX_TEST_CASES],tc,ns;
int n[MAX_TEST_CASES];
int snapper[30];
int power[30];
void reset_snapper() 
{
	int i;
	for(i=0;i<30;i++) {
                snapper[i]=0;
                power[i]=0;
        }
	 power[0]=1;
}

int checkstat(int nsnapper)
{
	int c;
	int retVal=1;
	for(c=0;c<nsnapper;c++)
	{
		if(snapper[c]==0){
			retVal=0;break;
		}
	}
	return retVal;
}

void toggle(int nsnapper)
{
	int c;
	for(c=0;c<nsnapper;c++)
	{
		if(power[c]==1){
			if(snapper[c]==0) snapper[c]=1; else snapper[c]=0;
		}
	}
}

void setPower(int nsnapper)
{

	int c;
	for(c=1;c<nsnapper;c++)
	{
		if(snapper[c-1]==1){
			power[c]=1;
		} else {
		 power[c]=0; break;
		}
	}
	int ac;
	for(ac=c+1;ac<nsnapper;ac++) {
		power[ac]=0;
	}
}

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
	printf("Test Cases=%d\n",t);
	for(i=0;i<t;i++) {
		fscanf(fp, "%d%ld", &n[i],&k[i]);
	}
	for(tc=0;tc<t;tc++)
	{
		int c=0;
		printf("%d %ld\n", n[tc],k[tc]);
		reset_snapper();
		printf("Snap No=%d---", c);
		int t1;
		for(t1=0;t1<n[tc];t1++) {
			printf("%d(%d) ",snapper[t1],power[t1]);
		}
		printf("\n");
		for(c=1;c<=k[tc];c++) {
			int t1;		
			toggle(n[tc]);		
			setPower(n[tc]);  
			printf("Snap No=%d---", c);
			for(t1=0;t1<n[tc];t1++) {
				printf("%d(%d) ",snapper[t1],power[t1]);
			}
			printf("\n");
		}
		int retval=checkstat(n[tc]);
		char ans[4];
		if (retval==0) strcpy(ans,"OFF"); else strcpy(ans,"ON");
		fprintf(ofp, "Case #%d: %s\n", tc+1, ans);
	}
	fclose(fp);
	fclose(ofp);
	return 0;
}
