#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
int TestNo;
int N; //Run Times
int AB[1000][2]; // Capacity
int i,j,k;
long length;
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
       length = 0;
       fscanf(fp, "%d", &N);
       for (j = 0; j<N ; j++)
       {
        fscanf(fp, "%d%d",&AB[j][0],&AB[j][1]);
       }
       for (j = 0; j<N ; j++)
       {
          for (k = j + 1; k<N ; k++)
            if (((AB[j][0] > AB[k][0]) && (AB[j][1]<AB[k][1])) || ((AB[j][0] < AB[k][0]) && (AB[j][1] > AB[k][1])))
            {
                length++;
            }
       }
       fprintf(ofp, "Case #%d: %d\n", i,length);
    }
	return 0;
}
