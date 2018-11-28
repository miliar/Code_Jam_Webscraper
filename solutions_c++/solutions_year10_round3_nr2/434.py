#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
int TestNo;
long L; //Run Times
long P; // Capacity
int C;
double temp;
int length,i;
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	fscanf(fp, "%d", &TestNo);
	for(i=1;i<=TestNo;i++)
    {
       fscanf(fp, "%d%d%d", &L,&P,&C);
       if (((double)P / (double)L) <= (double)C )
       {
          length = 0;
       }
       else
       {
              temp = ((log((double)P/(double)L))/log((double)C));
              temp = ((log(ceil(temp))) / (log((double)2) ));
                     length = (int)(ceil(temp));
                     }
       fprintf(ofp, "Case #%d: %d\n", i,length);
    }
	return 0;
}
