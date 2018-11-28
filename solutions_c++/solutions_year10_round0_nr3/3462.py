#include<stdio.h>
#include<string.h>
#include<conio.h>
#include<math.h>
int n;
unsigned long r;
unsigned long arr[1000];
unsigned long k;
long ans;
int main()
{       int a;
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	int ppl;
	int i, j, tc;
	int cnt=0;
	long sum=0,fsum=0;
	fscanf(fp, "%d",&tc);
	for(i=1;i<=tc;i++)
	{fscanf(fp, "%d %d %d", &r,&k,&n);
		for(a=0;a<n;a++)
		{fscanf(fp,"%d",&arr[a]);
//		 printf("%d\t",arr[a]);
		 }
  //	     getch();	 getch();
		fsum=0;
		cnt=0;

		for(a=0;a<r;a++)
		{sum=0;
		 ppl=0;
			while(sum+arr[cnt]<=k)
			{  //   printf("%d\t",sum);
			sum+=arr[cnt];
			ppl++;
			cnt++;
			if(cnt==n)
			cnt=0;
			if(ppl>=n)
			break;
			}

		fsum+=sum;
	     //	printf("\n\n\t\t%d",fsum);
	     //			getch();
		}

		fprintf(ofp, "Case #%d: %ld\n", i, fsum);
	}
	return 0;
}
