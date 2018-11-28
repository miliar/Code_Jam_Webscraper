#include<stdio.h>
#include<string.h>]
#include<math.h>
int n;
  unsigned long power;
 unsigned long no;

int ans=0;
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j, tc;
	int cnt;
	fscanf(fp, "%d",&n);
	for(i=1;i<=n;i++)
	{ ans=0;
	fscanf(fp, "%d %d", &power,&no);
	if(no==0)
	{char arr[]="OFF";
	fprintf(ofp, "Case #%d: %s\n", i, arr);
	continue;
	}
	if((no+1)%(int)pow(2,power)==0)
		ans=1;

	       if(ans==1)
	       {
	       char arr2[]="ON";
		fprintf(ofp, "Case #%d: %s\n", i, arr2);
		}
		else
		{   char arr3[]="OFF";
			fprintf(ofp, "Case #%d: %s\n", i, arr3);
		}
	}
	return 0;
}
